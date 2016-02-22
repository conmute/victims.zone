from victims import db
from sqlalchemy.dialects.postgresql import JSON
import enum

# Helper variables
class RecordType(enum.Enum):
    single = "single"
    summary = "summary"

# Helper tables
tags = db.Table('tags_to_record',
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')),
    db.Column('record_id', db.Integer, db.ForeignKey('record.id')),
)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String())
    registered_date = db.Column(db.DateTime)


class Record(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String())
    date_from = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_to = db.Column(db.DateTime, default=db.func.current_timestamp())
    description = db.Column(db.Text)
    map_data = db.Column(JSON)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))
    tags = db.relationship('Tag', secondary=tags,
        backref=db.backref('record', lazy='dynamic'))
    type = db.Column(db.Enum(RecordType));
    author_id = db.Column(db.BigInteger, db.ForeignKey('user.id'))

    def __init__(self, **args):
        self.name = args.name
        self.date_from = args.date_from
        self.date_to = args.date_to
        self.description = args.description
        self.map_data = args.map_data
        self.category = args.category
        self.tags = args.tags
        self.type = args.type
        self.author_id = args.author_id

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String())
    date = db.Column(db.DateTime, default=db.func.current_timestamp())


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
