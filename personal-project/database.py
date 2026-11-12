from pathlib import Path
import sqlite3

# Keep the database in the same folder as this file.
DATABASE_PATH = Path(__file__).resolve().parent / "art_gallery.db"


def get_connection():
    """Open a database connection and enable foreign-key enforcement."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_database():
    """Create the artists and art_pieces tables if they do not exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS art_pieces (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                artist_id INTEGER NOT NULL,
                art_piece_link TEXT NOT NULL DEFAULT '',
                published_year INTEGER,
                FOREIGN KEY (artist_id) REFERENCES artists(id)
                    ON UPDATE CASCADE
                    ON DELETE RESTRICT
            )
        """)


if __name__ == "__main__":
    create_database()
    print(f"Database ready: {DATABASE_PATH}")
