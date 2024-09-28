from flask import render_template, redirect, url_for, flash, request, session
from app import app, db
from models import Product, User, Order
from forms import RegistrationForm, LoginForm, ShippingForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product_details.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product.id)
    flash('Product added to cart!')
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    products = Product.query.filter(Product.id.in_(cart)).all()
    return render_template('cart.html', products=products)

@app.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    action = request.form.get('action')
    cart = session.get('cart', [])
    if action == 'remove':
        cart.remove(product_id)
    session['cart'] = cart
    return redirect(url_for('view_cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    form = ShippingForm()
    if form.validate_on_submit():
        cart = session.get('cart', [])
        products = Product.query.filter(Product.id.in_(cart)).all()
        total_price = sum([p.price for p in products])
        order = Order(user_id=current_user.id, total_price=total_price, shipping_address=form.address.data)
        db.session.add(order)
        db.session.commit()
        session.pop('cart', None)
        flash('Order placed successfully!')
        return redirect(url_for('my_orders'))
    return render_template('checkout.html', form=form)

@app.route('/my_orders')
@login_required
def my_orders():
    orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('my_orders.html', orders=orders)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful.')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
