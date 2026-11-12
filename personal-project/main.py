from database import create_database, get_connection


# -------------------------
# ARTIST CRUD
# -------------------------

def create_artist(name):
    name = name.strip()
    if not name:
        raise ValueError("Artist name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO artists (name) VALUES (?)",
            (name,)
        )
        return cursor.lastrowid


def get_artists():
    with get_connection() as connection:
        return connection.execute(
            "SELECT id, name FROM artists ORDER BY id"
        ).fetchall()


def update_artist(artist_id, new_name):
    new_name = new_name.strip()
    if not new_name:
        raise ValueError("Artist name cannot be empty.")

    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE artists SET name = ? WHERE id = ?",
            (new_name, artist_id)
        )
        return cursor.rowcount > 0


def delete_artist(artist_id):
    # The database prevents deleting an artist who still has art pieces.
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM artists WHERE id = ?",
            (artist_id,)
        )
        return cursor.rowcount > 0


# -------------------------
# ART PIECE CRUD
# -------------------------

def create_art_piece(title, artist_id, art_piece_link="", published_year=None):
    title = title.strip()
    art_piece_link = art_piece_link.strip()

    if not title:
        raise ValueError("Art piece title cannot be empty.")

    with get_connection() as connection:
        cursor = connection.execute(
            """INSERT INTO art_pieces
               (title, artist_id, art_piece_link, published_year)
               VALUES (?, ?, ?, ?)""",
            (title, artist_id, art_piece_link, published_year)
        )
        return cursor.lastrowid


def get_art_pieces():
    with get_connection() as connection:
        return connection.execute("""
            SELECT
                art_pieces.id,
                art_pieces.title,
                art_pieces.artist_id,
                artists.name AS artist_name,
                art_pieces.art_piece_link,
                art_pieces.published_year
            FROM art_pieces
            JOIN artists ON artists.id = art_pieces.artist_id
            ORDER BY art_pieces.id
        """).fetchall()


def update_art_piece(art_piece_id, title, artist_id,
                     art_piece_link="", published_year=None):
    title = title.strip()
    art_piece_link = art_piece_link.strip()

    if not title:
        raise ValueError("Art piece title cannot be empty.")

    with get_connection() as connection:
        cursor = connection.execute("""
            UPDATE art_pieces
            SET title = ?, artist_id = ?, art_piece_link = ?, published_year = ?
            WHERE id = ?
        """, (title, artist_id, art_piece_link, published_year, art_piece_id))
        return cursor.rowcount > 0


def delete_art_piece(art_piece_id):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM art_pieces WHERE id = ?",
            (art_piece_id,)
        )
        return cursor.rowcount > 0


# -------------------------
# CONSOLE USER INTERFACE
# -------------------------

def show_artists():
    artists = get_artists()
    print("\\nARTISTS")
    if not artists:
        print("No artists found.")
        return
    for artist in artists:
        print(f"{artist['id']}. {artist['name']}")


def show_art_pieces():
    pieces = get_art_pieces()
    print("\\nART PIECES")
    if not pieces:
        print("No art pieces found.")
        return
    for piece in pieces:
        year = piece["published_year"] if piece["published_year"] is not None else "Unknown"
        print(
            f"{piece['id']}. {piece['title']} | Artist: {piece['artist_name']} "
            f"(ID: {piece['artist_id']}) | Year: {year} | "
            f"Link: {piece['art_piece_link'] or 'None'}"
        )


def read_optional_year():
    value = input("Published year (leave blank if unknown): ").strip()
    if not value:
        return None
    return int(value)


def artist_menu():
    while True:
        print("\\n--- ARTIST MANAGEMENT ---")
        print("1. Create artist")
        print("2. View artists")
        print("3. Update artist")
        print("4. Delete artist")
        print("0. Back")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                name = input("Artist name: ")
                artist_id = create_artist(name)
                print(f"Artist created with ID {artist_id}.")
            elif choice == "2":
                show_artists()
            elif choice == "3":
                show_artists()
                artist_id = int(input("Artist ID to update: "))
                name = input("New artist name: ")
                print("Artist updated." if update_artist(artist_id, name)
                      else "Artist ID not found.")
            elif choice == "4":
                show_artists()
                artist_id = int(input("Artist ID to delete: "))
                print("Artist deleted." if delete_artist(artist_id)
                      else "Artist ID not found.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except Exception as error:
            print(f"Could not complete operation: {error}")
            print("Check that the artist exists and is not linked to art pieces.")


def art_piece_menu():
    while True:
        print("\\n--- ART PIECE MANAGEMENT ---")
        print("1. Create art piece")
        print("2. View art pieces")
        print("3. Update art piece")
        print("4. Delete art piece")
        print("0. Back")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                show_artists()
                title = input("Art piece title: ")
                artist_id = int(input("Artist ID: "))
                link = input("Art piece link (optional): ")
                year = read_optional_year()
                piece_id = create_art_piece(title, artist_id, link, year)
                print(f"Art piece created with ID {piece_id}.")
            elif choice == "2":
                show_art_pieces()
            elif choice == "3":
                show_art_pieces()
                piece_id = int(input("Art piece ID to update: "))
                title = input("New title: ")
                show_artists()
                artist_id = int(input("New artist ID: "))
                link = input("Art piece link (optional): ")
                year = read_optional_year()
                print("Art piece updated." if update_art_piece(
                    piece_id, title, artist_id, link, year
                ) else "Art piece ID not found.")
            elif choice == "4":
                show_art_pieces()
                piece_id = int(input("Art piece ID to delete: "))
                print("Art piece deleted." if delete_art_piece(piece_id)
                      else "Art piece ID not found.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except Exception as error:
            print(f"Could not complete operation: {error}")
            print("Check that the selected artist exists.")


def main():
    create_database()

    while True:
        print("\\n========== ART GALLERY DATABASE ==========")
        print("1. Manage artists")
        print("2. Manage art pieces")
        print("3. View all artists")
        print("4. View all art pieces")
        print("0. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            artist_menu()
        elif choice == "2":
            art_piece_menu()
        elif choice == "3":
            show_artists()
        elif choice == "4":
            show_art_pieces()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
