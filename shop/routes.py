from flask import render_template

from shop import app

@app.route('/')
def index():
    return render_template('index.html')

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
    