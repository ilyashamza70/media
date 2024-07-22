import sqlite3

def create_connection(db_file):
    """Crea una connessione al database SQLite specificato dal db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connessione al database {db_file} riuscita.")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_tables(conn):
    """Crea le tabelle nel database."""
    try:
        sql_create_courses_table = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """
        sql_create_course_details_table = """
        CREATE TABLE IF NOT EXISTS course_details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            detail TEXT NOT NULL,
            FOREIGN KEY (course_id) REFERENCES courses (id)
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_courses_table)
        cursor.execute(sql_create_course_details_table)
        print("Tabelle create con successo.")
    except sqlite3.Error as e:
        print(e)

def add_course(conn, course_name):
    """Aggiunge un nuovo corso al database."""
    sql = '''INSERT INTO courses(name) VALUES(?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (course_name,))
    conn.commit()
    return cursor.lastrowid

def add_course_detail(conn, course_id, detail):
    """Aggiunge un dettaglio del corso al database."""
    sql = '''INSERT INTO course_details(course_id, detail) VALUES(?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (course_id, detail))
    conn.commit()

def get_courses(conn):
    """Recupera tutti i corsi dal database."""
    sql = '''SELECT * FROM courses'''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def get_course_details(conn, course_id):
    """Recupera i dettagli di un corso specifico dal database."""
    sql = '''SELECT * FROM course_details WHERE course_id = ?'''
    cursor = conn.cursor()
    cursor.execute(sql, (course_id,))
    rows = cursor.fetchall()
    return rows

if __name__ == '__main__':
    database = "school.db"
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)
        # Esempio di aggiunta di un corso e dettagli
        course_id = add_course(conn, "Matematica")
        add_course_detail(conn, course_id, "Algebra")
        add_course_detail(conn, course_id, "Geometria")
        courses = get_courses(conn)
        for course in courses:
            print(course)
            details = get_course_details(conn, course[0])
            for detail in details:
                print(f"  {detail}")
    else:
        print("Errore! Impossibile creare la connessione al database.")