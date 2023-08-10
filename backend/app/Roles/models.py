from app.Database import db, BaseModelMixin


class Roles(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    users = db.relationship('Users', backref="roles", cascade='all, delete-orphan')


    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f'Rol({self.name})'


    def __str__(self):
        return f'{self.name}'


    @classmethod
    def return_all(cls):
        def to_json(rol):
            return {
                'name': rol.name
            }
        return {'roles': [to_json(rol) for rol in Roles.query.all()]}
                