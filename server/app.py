from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

@validates('phone_number')
def validate_phone_number(self, key, value):
    if value is not None and len(value) != 10:
        raise ValueError('Phone number must be exactly ten digits.')
    return value

@validates('content')
def validate_content_length(self, key, value):
    if len(value) < 250:
        raise ValueError('Post content must be at least 250 characters long.')
    return value

@validates('summary')
def validate_summary_length(self, key, value):
    if len(value) > 250:
        raise ValueError('Post summary cannot be longer than 250 characters.')
    return value

if __name__ == '__main__':
    app.run(port=5555, debug=True)