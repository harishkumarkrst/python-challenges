import sqlite3


def create_database(db_path):
    """
    Create a SQLite database at db_path with a 'students' table.
    """
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT    NOT NULL,
                grade TEXT    NOT NULL,
                score REAL    NOT NULL
            )
        """)


def add_student(db_path, name, grade, score):
    """
    Insert a new student record and return its ID.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "INSERT INTO students (name, grade, score) VALUES (?, ?, ?)",
            (name, grade, score)
        )
        return cursor.lastrowid


def get_student(db_path, student_id):
    """
    Retrieve a student by ID.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT id, name, grade, score FROM students WHERE id = ?",
            (student_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "name": row[1],
            "grade": row[2],
            "score": row[3]
        }


def get_all_students(db_path):
    """
    Retrieve all students.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT id, name, grade, score FROM students"
        )

        rows = cursor.fetchall()

        return [
            {
                "id": r[0],
                "name": r[1],
                "grade": r[2],
                "score": r[3]
            }
            for r in rows
        ]


def update_score(db_path, student_id, new_score):
    """
    Update student's score.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "UPDATE students SET score = ? WHERE id = ?",
            (new_score, student_id)
        )

        return cursor.rowcount > 0


def delete_student(db_path, student_id):
    """
    Delete a student.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        return cursor.rowcount > 0


def get_students_by_grade(db_path, grade):
    """
    Return all students with a specific grade.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT id, name, grade, score FROM students WHERE grade = ?",
            (grade,)
        )

        rows = cursor.fetchall()

        return [
            {
                "id": r[0],
                "name": r[1],
                "grade": r[2],
                "score": r[3]
            }
            for r in rows
        ]


def get_average_score(db_path):
    """
    Return average student score rounded to 2 decimals.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            "SELECT AVG(score) FROM students"
        )

        avg = cursor.fetchone()[0]

        if avg is None:
            return None

        return round(avg, 2)