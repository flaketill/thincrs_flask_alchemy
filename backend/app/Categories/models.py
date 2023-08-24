from ..Database import db


# Creating the Category for inserting data into the database
class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), index=True)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
        