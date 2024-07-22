from db_manager import create_connection, create_tables, add_course, add_course_detail, get_courses, get_course_details

def main():
    database = "school.db"
    conn = create_connection(database)
    if conn is not None:
        create_tables(conn)
        # Aggiungi corsi e dettagli qui
        course_id = add_course(conn, "Fisica")
        add_course_detail(conn, course_id, "Meccanica")
        add_course_detail(conn, course_id, "Termodinamica")
        
        # Recupera e stampa i corsi e i dettagli
        courses = get_courses(conn)
        for course in courses:
            print(course)
            details = get_course_details(conn, course[0])
            for detail in details:
                print(f"  {detail}")
    else:
        print("Errore! Impossibile creare la connessione al database.")

if __name__ == '__main__':
    main()