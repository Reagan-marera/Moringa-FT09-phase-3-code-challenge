from database.connection import get_connection

class Author:
    def __init__(self, name):
        self.name = name
        self._create_in_db()
        
    def _create_in_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self.name,))
        conn.commit()
        
        self.id = cursor.lastrowid
        
        conn.close()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title FROM articles
            WHERE author_id = ?
        ''', (self.id,))
        
        articles = cursor.fetchall()
        conn.close()
        
        return articles

    @staticmethod
    def get_by_id(author_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            author = Author(row[1])
            author.id = row[0]
            return author
        return None
