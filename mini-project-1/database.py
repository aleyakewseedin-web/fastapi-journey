
from contextlib import contextmanager
import sqlite3

class Database:

    def connect_to_db(self):
        self.conn = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.conn.cursor()

    def create_table(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY,
                name TEXT,
                department TEXT
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS enrollment (
                id INTEGER PRIMARY KEY,
                course_name TEXT,
                semester TEXT,
                grade REAL,
                instructor TEXT,
                student_id INTEGER,
                FOREIGN KEY (student_id) REFERENCES student(id)
            )
        """)

    def get_all(self) -> list:
        self.cur.execute("SELECT * FROM student")
        rows = self.cur.fetchall()
        return [self._row_to_dict(row) for row in rows]
    def get(self, id: int) -> dict | None:
        self.cur.execute("""
            SELECT * FROM student WHERE id = ?
        """, (id,))
        row = self.cur.fetchone()
        return self._row_to_dict(row) if row else None
    
    def create(self, item) -> int:
        self.cur.execute("SELECT MAX(id) FROM student")
        result = self.cur.fetchone()
        new_id = (result[0] or 0) + 1
        self.cur.execute("""
            INSERT INTO student
            VALUES (:id, :name, :department)
        """, {"id": new_id, **item.model_dump()})
        self.conn.commit()
        return new_id
    
    def update(self, id: int, item) -> dict | None:
        self.cur.execute("""
            UPDATE student
            SET name = :name, department = :department
            WHERE id = :id
        """, {"id": id, **item.model_dump()})
        self.conn.commit()
        return self.get(id)
    
    def delete(self, id: int):
        self.cur.execute("""
            DELETE FROM student WHERE id = ?
        """, (id,))
        self.conn.commit()
    
def get_all(self) -> list:
        self.cur.execute("SELECT * FROM enrollment")
        rows = self.cur.fetchall()
        return [self._row_to_dict(row) for row in rows]

def get(self, id: int) -> dict | None:
        self.cur.execute("""
            SELECT * FROM enrollment WHERE id = ?
        """, (id,))
        row = self.cur.fetchone()
        return self._row_to_dict(row) if row else None

def create(self, item) -> int:
        self.cur.execute("SELECT MAX(id) FROM enrollment")
        result = self.cur.fetchone()
        new_id = (result[0] or 0) + 1
        self.cur.execute("""
            INSERT INTO enrollment
            VALUES (:id, :course_name, :semester, :grade, :instructor, :student_id)
        """, {"id": new_id, **item.model_dump()})
        self.conn.commit()
        return new_id
def update(self, id: int, item) -> dict | None:
        self.cur.execute("""
            UPDATE enrollment
            SET course_name = :course_name, semester = :semester, grade = :grade, instructor = :instructor, student_id = :student_id
            WHERE id = :id
        """, {"id": id, **item.model_dump()})
        self.conn.commit()
        return self.get(id)

def delete(self, id: int):
        self.cur.execute("""
            DELETE FROM enrollment WHERE id = ?
        """, (id,))
        self.conn.commit()

def close(self):
        self.conn.close()
def _student_row_to_dict(self, row):
    return {
        "course_name": row[0],
        "semester": row[1],
        "grade": row[2],
        "instructor": row[3]
    }

def _enrollment_row_to_dict(self, row):
    return {
        "id": row[0],
        "name": row[1],
        "department": row[2]
    }

@contextmanager
def managed_db():
    db = Database()
    db.connect_to_db()
    db.create_table()
    try:
        yield db
    finally:
        db.close()