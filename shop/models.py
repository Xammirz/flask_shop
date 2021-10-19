
from flask_login import UserMixin
from datetime import datetime
from shop import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get((user_id))
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    category = db.Column(db.String(), nullable = False)
    availibility = db.Column(db.String(), nullable = False)
    description = db.Column(db.Text(), nullable = False)
    image = db.Column(db.String(), nullable = False)
    def __repr__(self):
        return self.name
        
class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(), nullable = False, unique=True)
    password = db.Column(db.String(), nullable = False)
    IsAdmin = db.Column(db.Boolean())
    posts = db.relationship('Post', backref='author', lazy=True)
    carts = db.relationship('Cart', backref='vladelec', lazy=True)
    def __repr__(self) -> str:
        return self.email


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False) #название поста//до 50 символов
    content = db.Column(db.String(), nullable=False)
    date_posted = db.Column(
        db.DateTime(), nullable=False, default=datetime.now)
    image = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
    

    def __repr__(self) -> str:
        return self.title        
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False) #Имя ///до 50 символов
    subject = db.Column(db.String(50), nullable=False) #Объект//до 50 символов
    email = db.Column(db.String(), nullable=False) #email 
    date_posted = db.Column(
        db.DateTime(), nullable=False, default=datetime.now) #дата комментария
    message = db.Column(db.String(), nullable=False) #само сообщение
    post_id = db.Column(db.Integer(), db.ForeignKey(
        'posts.id'), nullable=False) #создаем связь

    def __repr__(self) -> str:
        return self.subject    
class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable = False)
    price = db.Column(db.Integer(), nullable = False)   
    image = db.Column(db.String(), nullable = False)
    date_posted = db.Column(
        db.DateTime(), nullable=False, default=datetime.now)
    user_id = db.Column(db.Integer(), db.ForeignKey(
        'users.id'), nullable=False)
    def __repr__(self):
        return self.title