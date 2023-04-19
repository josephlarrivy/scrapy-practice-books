

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
    def create_new_list(cls, item_id, title, price, monetary_unit, star_rating, link, website):
        return cls(item_id=random_string, title=title, price=price, monetary_unit=monetary_unit, star_rating=star_rating, link=link, website=website)

