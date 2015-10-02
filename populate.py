import sqlite3
from datetime import datetime

with sqlite3.connect("bloggy.db") as connection:
    c = connection.cursor()
    posts = [
        (4, datetime.now(),'Just a test', 'Does it work'),
        (5, datetime.now(), 'Another test', 'So it works')
    ]
    c.executemany("INSERT INTO blog_post values(?,?,?,?)",posts)