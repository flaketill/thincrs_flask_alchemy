from app.Database import db, BaseModelMixin
from app.Roles.models import Roles


# Creating the Users for inserting data into the database
class Users(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable= False)


    def __init__(self, first_name, last_name, email, rol_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.rol_id = rol_id
        
    
    def __repr__(self):
        return f'User({self.email})'
    

    def __str__(self):
        return f'{self.name}'


    def to_json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "rol_id": self.rol_id,
        }   
    

    @classmethod
    def find_first_by_email(cls, email):
        return cls.query.filter_by(email = email).first()
    

    @classmethod
    def find_all_by_rol_id(cls, rol_id):
        return cls.query.filter_by(rol_id = rol_id).all()


    @classmethod
    def return_all(cls):
        def to_json(user):
            return {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "rol_id": user.rol_id,
            }
        return {'users': [to_json(user) for user in Users.query.all()]}

        
