from flask_sqlalchemy import SQLAlchemy
import os
import random
import string
import psycopg2


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))


class Book_Title(db.Model): 
    __tablename__ = 'book_titles'

    title = db.Column(db.Text, primary_key=True, nullable=False, unique=True)

    @classmethod
    def insert_title_into_database(title):
        return cls(title=title)
    

class Prices(db.Model):
    __tablename__ = 'prices'
    
    item_id = db.Column(db.Text, unique=True, primary_key=True, nullable=False)
    title = db.Column(db.Text, db.ForeignKey('book_titles.title'), nullable=False)
    price = db.Column(db.Text, nullable=False)
    monetary_unit = db.Column(db.Text, nullable=False)
    star_rating = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    website = db.Column(db.Text, nullable=False)

    @classmethod
    def create_new_list(cls, item_id, title, price, monetary_unit, start_rating, link, website):
        return cls(item_id=random_string, title=title, price=price, monetary_unit=monetary_unit, start_rating=start_rating, link=link, website=website)



conn = psycopg2.connect(
   database="scrapy_data"
)

cur = conn.cursor()
cur.execute("INSERT INTO book_titles VALUES ('test_book');")
cur.execute("INSERT INTO prices VALUES ('xxx', 'test_book', '1.00', '$', '5', 'www.xxx.com', 'www.yyy.com');")



conn.commit()
conn.close()