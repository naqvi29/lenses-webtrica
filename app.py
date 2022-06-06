from flask import Flask, render_template
from flaskext.mysql import MySQL
import os
from os.path import join, dirname, realpath
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'lenses'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
mysql.init_app(app)

# configure secret key for session protection)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-category")
def add_category():
    return render_template("add-category.html")

@app.route("/all-category")
def all_category():
    return render_template("all-category.html")

@app.route("/add-brand")
def add_brand():
    return render_template("add-brand.html")

@app.route("/all-brand")
def all_brand():
    return render_template("all-brand.html")

@app.route("/add-new-lense-type")
def add_new_lense_type():
    return render_template("add-new-lense-type.html")

@app.route("/add-pricing-qty")
def add_pricing_qty():
    return render_template("add-pricing-qty.html")

@app.route("/add-customer")
def add_customer():
    return render_template("add-customer.html")

@app.route("/order-to-make")
def order_to_make():
    return render_template("order-to-make.html")

@app.route("/add-supplier")
def add_supplier():
    return render_template("add-supplier.html")

@app.route("/add-sale-receipt")
def add_sale_receipt():
    return render_template("add-sale-receipt.html")

@app.route("/add-sale-order")
def add_sale_order():
    return render_template("add-sale-order.html")

@app.route("/add-purchase-order")
def add_purchase_order():
    return render_template("add-purchase-order.html")

@app.route("/add-branch")
def add_branch():
    return render_template("add-branch.html")

@app.route("/add-user")
def add_user():
    return render_template("add-user.html")

if __name__ == '__main__':
    app.run(debug=True)