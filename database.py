import sqlite3

DATABASE = "askme.db"

def init_db():
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS pdf_files (id INTEGER PRIMARY KEY, filename TEXT)''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")

def save_pdf_record(filename):
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pdf_files (filename) VALUES (?)", (filename,))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Database error saving record: {e}")

# Example usage (optional):
if __name__ == "__main__":
    init_db()
    save_pdf_record("example.pdf")
    save_pdf_record("another_example.pdf")

    # Example of reading the data.
    try:
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pdf_files")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Database error reading data: {e}")
