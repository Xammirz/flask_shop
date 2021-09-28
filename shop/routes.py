from flask import render_template, request
from werkzeug.utils import secure_filename
from shop.models import Product,db
from shop import app
import os

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