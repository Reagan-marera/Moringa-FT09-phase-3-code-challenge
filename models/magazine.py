
from database.connection import get_connection

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._create_in_db()
        
    def _create_in_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
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
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, title FROM articles
            WHERE magazine_id = ?
        ''', (self.id,))
        
        articles = cursor.fetchall()
        conn.close()
        
        return articles

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT DISTINCT authors.id, authors.name FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        
        contributors = cursor.fetchall()
        conn.close()
        
        return contributors

    @staticmethod
    def get_by_id(magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            magazine = Magazine(row[1], row[2])
            magazine.id = row[0]
            return magazine
        return None
