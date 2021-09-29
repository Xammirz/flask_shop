from flask import render_template, request,redirect,url_for
from werkzeug.utils import secure_filename
from shop.models import Product, User,db,User
from shop import app
import os
from flask_login import login_user,logout_user,current_user
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/category')
def category():
    return render_template('category.html')

@app.route('/single-product')
def singleproduct():
    return render_template('single-product.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        u = User(email=request.form.get('email'), password=request.form.get('password'))
        db.session.add(u)
        db.session.commit()
        login_user(u)
        return redirect(url_for('index'))
    return render_template('registration.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and user.password == request.form.get('password'):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', product=product)








@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')







@app.route('/single-blog')
def singleblog():
    return render_template('single-blog.html')
@app.route('/add_product', methods=['GET','POST'])
def add_product():
 if request.method == 'POST':
    f = request.form 
    file_name = request.files.get('image')   
    filename = secure_filename(file_name.filename)
    file_name.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    p = Product(title=f.get('title'),price=f.get('price'),category=f.get('category'),availibility=f.get('availibility'),description=f.get('description'),image=file_name.filename)  
    db.session.add(p)
    db.session.commit()
 return render_template('add_product.html')  