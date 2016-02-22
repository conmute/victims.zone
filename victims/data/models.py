from victims import db
from sqlalchemy.dialects.postgresql import JSON
import datetime


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
    author_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))
