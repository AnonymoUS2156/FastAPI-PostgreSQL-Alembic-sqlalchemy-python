import psycopg2
from config import DB_CONFIG

file_path = r'C:\Users\GribkovND\Documents\PythonCode\sinonymDB\Синонимы.txt'

def connect_to_database():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL:", e)
        return None


def insert_synonym(cur, conn, main_word, synonym):
    try:
        cur.execute("INSERT INTO synonyms (first_synonym, second_synonym) VALUES (%s, %s)", (main_word, synonym))
        cur.execute("DELETE FROM synonyms WHERE first_synonym IS NULL AND second_synonym IS NULL;")
        conn.commit()
    except psycopg2.Error as e:
        print("Error inserting synonym:", e)

def read_synonyms_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return []

def process_synonyms_file(cur, conn, file_path):
    lines = read_synonyms_from_file(file_path)
    for line in lines:
        main_word, synonyms = line.lower().strip().split('|')
        synonyms_list = synonyms.split(',')
        for synonym in synonyms_list:
            if "(" in synonym or ")" in synonym:
                continue
            insert_synonym(cur, conn, main_word, synonym)
def main():
    conn = connect_to_database()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS synonyms (first_synonym TEXT, second_synonym TEXT);")
            process_synonyms_file(cur, conn, file_path)
            conn.commit()
        finally:
            conn.close()

if __name__ == "__main__":
    main()
