from app import db
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    email_address = db.Column(db.Text, nullable=False)
    post = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def password_matches(self, to_check):
        return check_password_hash(self.password, to_check)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    body_content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False,
        default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=False,
        default=func.now(), onupdate=func.now())
    
    # author_name = db.Column(db.String(128))

    def __repr__(self):
        return f"<Post ('{self.title}', '{self.created_at}')>"
