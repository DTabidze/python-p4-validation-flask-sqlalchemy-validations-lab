from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("name must be string")
        return value

    @validates("phone_number")
    def validate_phonenumber(self, key, value):
        if not isinstance(value, str) or len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        return value

    def __repr__(self):
        return f"Author(id={self.id}, name={self.name})"


class Post(db.Model):
    __tablename__ = "posts"
    # Add validations and constraints

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validate_content(self, key, value):
        if not isinstance(value, str) or len(value) < 250:
            raise ValueError("content must be at least 250 chars")
        return value

    @validates("summary")
    def validate_summary(self, key, value):
        if not isinstance(value, str) or len(value) >= 250:
            raise ValueError("summary should not be more then 250 chars")
        return value

    @validates("category")
    def validate_category(self, key, value):
        if value != "Fiction" and value != "Non-Fiction":
            raise ValueError("category must be str")
        return value

    @validates("title")
    def validate_title(self, key, title):
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("No clickbait found")
        return title

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})"
