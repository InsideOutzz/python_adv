# Painting shop

    pip install -r requirements.txt
    cp .env.example .env   # then fill it in and load it (or export the variables)
    flask --app app run

1. Put photos of your paintings in `static/paintings/` and list them in `paintings.json` (price in whole currency units).
2. In Stripe, create a webhook to `https://YOUR-DOMAIN/webhook` for `checkout.session.completed` and put its secret in `STRIPE_WEBHOOK_SECRET`. This marks a painting as sold after payment.
3. Use `sk_test_...` keys first (card 4242 4242 4242 4242), then switch to live keys.
4. Deploy with `gunicorn app:app` on any host that runs Python.
