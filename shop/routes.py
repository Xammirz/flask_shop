import os

from flask import render_template, request, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user
from shop.forms import RegistrationForm
from shop import app
from shop.models import Product, User, db



@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/shop_category')
def shop_category():
    return render_template('category.html')

@app.route('/registration', methods=['GET','POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Успешно!!', 'seccess')
        return redirect(url_for('login'))       
    return render_template('registration.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and user.email == request.form.get('email'):
            login_user(user)
            return redirect(url_for('index'))
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
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], image.filename))
        p = Product(title=title, price=price, category=category,
                    availibility=availibility, description=description, image=image.filename)
        db.session.add(p)
        db.session.commit()
        
    return render_template('add_product.html')


@app.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get(product_id)
    return render_template('product_detail.html', product=product)
