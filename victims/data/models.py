from flask import current_app
from sqlalchemy.dialects.postgresql import JSON
import datetime

db = current_app.db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50))
    registered = db.Column(db.DateTime(), default=datetime.datetime.utcnow)


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50))
    created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

tags = db.Table('tags_to_record',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('record_id', db.Integer, db.ForeignKey('record.id'))
)


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created = db.Column(db.DateTime(), default=datetime.datetime.utcnow)


class Record(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(256))
    description = db.Column(db.Text())
    date_from = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    date_to = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    map_data = db.Column(JSON)
    type = db.Column(db.Enum('single', 'summary', name='record_types'))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('record', lazy='dynamic'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    author = db.Column(db.BigInteger, db.ForeignKey('user.id'))

    def __init__(self, name, description, date_from, date_to, map_data, category, tags, type, author):
        self.name = name
        self.description = description
        self.date_from = date_from
        self.date_to = date_to
        self.map_data = map_data
        self.category = category
        self.tags = tags
        self.type = type
        self.author = author

    def __repr__(self):
        return '<id {}>'.format(self.id)
