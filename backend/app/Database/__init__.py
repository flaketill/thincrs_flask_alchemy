from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime
from settings import SQLALCHEMY_DATABASE_URI
#from flask_marshmallow import Marshmallow
from flask import current_app as app


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


metadata = MetaData(naming_convention=convention)


# create the extension
db = SQLAlchemy(metadata=metadata)

# Set up your SQLAlchemy engine and session
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine, autoflush=True)


class BaseModelMixin:
	created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
	deleted = db.Column(db.Boolean, nullable=False, default=False)


	def save(self):
		db.session.add(self)
		db.session.commit()


	def delete(self):
		db.session.delete(self)
		db.session.commit()


	def update(self):
		db.session.commit()


	@classmethod
	def get_by_id(cls, id):
		return cls.query.get(id)


	@classmethod
	def get_all(cls):
		return cls.query.filter_by(deleted=False).all()


	@classmethod
	def simple_filter(cls, **kwargs):
		return cls.query.filter_by(**kwargs).all()

