from database.connection import get_connection

class Article:
    def __init__(self, author, magazine, title):
        self.author_id = author.id
        self.magazine_id = magazine.id
        self.title = title
        self._create_in_db()
        self.id = None 

    def _create_in_db(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)', (self.author_id, self.magazine_id, self.title))
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
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    def author(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM authors WHERE id = ?', (self.author_id,))
        
        author = cursor.fetchone()
        conn.close()
        
        return author

    def magazine(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (self.magazine_id,))
        
        magazine = cursor.fetchone()
        conn.close()
        
        return magazine
