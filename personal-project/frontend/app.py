from flask import Flask, render_template, request, redirect, url_for, flash
from main import (
    create_database, get_artists, get_art_pieces,
    create_artist, update_artist, delete_artist,
    create_art_piece, update_art_piece, delete_art_piece
)

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

create_database()


@app.route("/")
def dashboard():
    artists = get_artists()
    pieces = get_art_pieces()
    return render_template("dashboard.html", artists=artists, pieces=pieces)


@app.route("/artists")
def artists_page():
    return render_template("artists.html", artists=get_artists())


@app.route("/artists/add", methods=["POST"])
def add_artist():
    try:
        create_artist(request.form.get("name", ""))
        flash("Artist added successfully.", "success")
    except Exception as exc:
        flash(str(exc), "error")
    return redirect(url_for("artists_page"))


@app.route("/artists/<int:artist_id>/edit", methods=["POST"])
def edit_artist(artist_id):
    try:
        if update_artist(artist_id, request.form.get("name", "")):
            flash("Artist updated successfully.", "success")
        else:
            flash("Artist not found.", "error")
    except Exception as exc:
        flash(str(exc), "error")
    return redirect(url_for("artists_page"))


@app.route("/artists/<int:artist_id>/delete", methods=["POST"])
def remove_artist(artist_id):
    try:
        if delete_artist(artist_id):
            flash("Artist deleted.", "success")
        else:
            flash("Artist not found.", "error")
    except Exception:
        flash("This artist cannot be deleted while artworks are assigned to them.", "error")
    return redirect(url_for("artists_page"))


@app.route("/artworks")
def artworks_page():
    return render_template(
        "artworks.html",
        pieces=get_art_pieces(),
        artists=get_artists()
    )


@app.route("/artworks/add", methods=["POST"])
def add_artwork():
    try:
        year_text = request.form.get("published_year", "").strip()
        year = int(year_text) if year_text else None
        create_art_piece(
            request.form.get("title", ""),
            int(request.form.get("artist_id", "")),
            request.form.get("art_piece_link", ""),
            year
        )
        flash("Artwork added successfully.", "success")
    except Exception as exc:
        flash(str(exc), "error")
    return redirect(url_for("artworks_page"))


@app.route("/artworks/<int:piece_id>/edit", methods=["POST"])
def edit_artwork(piece_id):
    try:
        year_text = request.form.get("published_year", "").strip()
        year = int(year_text) if year_text else None
        if update_art_piece(
            piece_id,
            request.form.get("title", ""),
            int(request.form.get("artist_id", "")),
            request.form.get("art_piece_link", ""),
            year
        ):
            flash("Artwork updated successfully.", "success")
        else:
            flash("Artwork not found.", "error")
    except Exception as exc:
        flash(str(exc), "error")
    return redirect(url_for("artworks_page"))


@app.route("/artworks/<int:piece_id>/delete", methods=["POST"])
def remove_artwork(piece_id):
    try:
        if delete_art_piece(piece_id):
            flash("Artwork deleted.", "success")
        else:
            flash("Artwork not found.", "error")
    except Exception as exc:
        flash(str(exc), "error")
    return redirect(url_for("artworks_page"))


if __name__ == "__main__":
    app.run(debug=True)
