import os
import re

from flask import render_template, request, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user, login_required
from shop.forms import LoginForm, RegistrationForm,PostForm
from shop import app
from shop.models import Cart, Comment, Product, User, db, Post
from cloudipsp import Api, Checkout



@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('blog.html', posts=posts)


@app.route('/shop_category')
def shop_category():
    return render_template('category.html')
@app.route('/buy/<int:buy_id>')
def buy(buy_id):
    item = Product.query.get(buy_id)
    api = Api(merchant_id=1396424,
          secret_key='test')
    checkout = Checkout(api=api)
    data = {
    "currency": "RUB",
    "amount": str (item.price) + "00"
}
    url = checkout.url(data).get('checkout_url')
    return redirect(url)

@app.route('/registration', methods=['GET','POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Успешно!!', 'success')
        login_user(user)
        return redirect(url_for('index'))       
    return render_template('registration.html', form=form)



@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and user.email == request.form.get('email'):   
            if user and user.password == request.form.get('password'):
                login_user(user)
            else:
                flash('Не правильный пароль!',category='error')    
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/category')
def category():
    return render_template('category.html')




@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        f = request.form
        title = f.get('title')
        price = f.get('price')
        category = f.get('category')
        availibility = f.get('availibility')
        description = f.get('description')
        image = request.files.get('image')
        image.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'product/', image.filename))
        p = Product(title=title, price=price, category=category,
                    availibility=availibility, description=description, image=image.filename)
        
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))
        
    return render_template('add_product.html')



@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', product=product)
    
@app.route('/post_detail/<int:post_id>', methods=['GET','POST'])
def post_detail(post_id):
    post = Post.query.get(post_id)
    comments = Comment.query.order_by(Comment.date_posted.desc()).all()
    if request.method == 'POST':
        comment = Comment(name=request.form.get('name'), subject=request.form.get('subject'), email=request.form.get('email'), message=request.form.get('message'), post=post)
        db.session.add(comment)
        db.session.commit()
        flash('Добавлено', 'success')
    return render_template('post_detail.html', post=post, comments=post.comments)   

@app.route('/cart/<int:id>')
def cart(id):
    product = Product.query.get(id) 
        
        
    return render_template("cart.html",product=product)
  
    
    

    



@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        image = request.files.get('image')
        if image:
            file_name = image.filename
            
            image.save(os.path.join(app.config['UPLOAD_FOLDER'] + 'blog/', file_name))
            post = Post(title=form.title.data, content=form.content.data, author=current_user, image=file_name)
            db.session.add(post)
            db.session.commit()
            flash('Пост был создан!', 'success')
            return redirect(url_for('blog'))
    return render_template('new_post.html', form=form, title='Создать пост', legend='Создать пост')
