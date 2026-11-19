import json, os, threading
import stripe
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)
stripe.api_key = os.environ.get("STRIPE_SECRET_KEY", "")
WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", "")
SITE = {
    "artist": os.environ.get("ARTIST_NAME", "Your Name"),
    "email": os.environ.get("CONTACT_EMAIL", "you@example.com"),
    "currency": os.environ.get("CURRENCY", "eur"),
}
SYMBOLS = {"eur": "€", "usd": "$", "gbp": "£"}
SHIP_TO = os.environ.get("SHIP_TO", "US,GB,DE,FR,IT,NL,AT,CH").split(",")
HERE = os.path.dirname(os.path.abspath(__file__))
SOLD_FILE = os.path.join(HERE, "sold.json")
lock = threading.Lock()


def load_sold():
    try:
        with open(SOLD_FILE) as f:
            return set(json.load(f))
    except FileNotFoundError:
        return set()


def mark_sold(pid):
    with lock:
        sold = load_sold()
        sold.add(pid)
        with open(SOLD_FILE, "w") as f:
            json.dump(sorted(sold), f)


def load_paintings():
    with open(os.path.join(HERE, "paintings.json"), encoding="utf-8") as f:
        items = json.load(f)
    sold = load_sold()
    for p in items:
        p["sold"] = p["id"] in sold
    return items


@app.context_processor
def inject():
    return {"site": SITE, "symbol": SYMBOLS.get(SITE["currency"], "")}


@app.route("/")
def index():
    return render_template("index.html", paintings=load_paintings())


@app.post("/buy/<pid>")
def buy(pid):
    p = next((p for p in load_paintings() if p["id"] == pid), None)
    if not p:
        abort(404)
    if p["sold"]:
        return render_template("message.html", title="This one has found a home",
                               text="Someone bought this painting a moment ago."), 409
    base = request.url_root.rstrip("/")
    product = {"name": p["title"], "description": f'{p["size"]}, {p["medium"]}'}
    if base.startswith("https"):  # Stripe can only show public images
        product["images"] = [base + url_for("static", filename="paintings/" + p["image"])]
    try:
        session = stripe.checkout.Session.create(
            mode="payment",
            line_items=[{"quantity": 1, "price_data": {
                "currency": SITE["currency"],
                "unit_amount": int(p["price"]) * 100,
                "product_data": product}}],
            shipping_address_collection={"allowed_countries": SHIP_TO},
            metadata={"painting_id": pid},
            success_url=base + url_for("thanks"),
            cancel_url=base + url_for("index"),
        )
    except Exception:
        return render_template("message.html", title="Payment didn't start",
                               text="Something went wrong connecting to the payment page. Please try again."), 502
    return redirect(session.url, code=303)


@app.route("/thanks")
def thanks():
    return render_template("message.html", title="Thank you",
                           text="Your payment went through. You'll get a receipt by email, and I'll write to you when the painting ships.")


@app.post("/webhook")
def webhook():
    try:
        event = stripe.Webhook.construct_event(
            request.data, request.headers.get("Stripe-Signature", ""), WEBHOOK_SECRET)
    except Exception:
        abort(400)
    if event["type"] == "checkout.session.completed":
        s = event["data"]["object"]
        if s.get("payment_status") == "paid":
            mark_sold(s["metadata"]["painting_id"])
    return "", 200


if __name__ == "__main__":
    app.run(debug=True)
