from flask import Flask, render_template, request
from flask.helpers import url_for
from flaskext.mysql import MySQL
import os
from os.path import join, dirname, realpath
from werkzeug.utils import redirect, secure_filename
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

@app.route("/add-category", methods=['GET','POST'])
def add_category():
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO categories (name, description) VALUES (%s,%s);",(name,desc))
        conn.commit()
        return redirect(url_for("add_category"))
    return render_template("add-category.html")

@app.route("/all-category")
def all_category():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from categories")
    categories = cursor.fetchall()
    return render_template("all-category.html",categories=categories)

@app.route("/delete-category/<string:id>")
def delete_category(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from categories where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_category"))

@app.route("/add-brand",methods=['GET','POST'])
def add_brand():
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO brands (name, description) VALUES (%s,%s);",(name,desc))
        conn.commit()
        return redirect(url_for("add_brand"))
    return render_template("add-brand.html")

@app.route("/all-brand")
def all_brand():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from brands")
    brands = cursor.fetchall()
    return render_template("all-brand.html",brands=brands)

@app.route("/delete-brand/<string:id>")
def delete_brand(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from brands where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_brand"))

@app.route("/add-new-lense-type",methods=['GET','POST'])
def add_new_lense_type():
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        category_id = request.form.get("category_id")
        brand_id = request.form.get("brand_id")
        left_right_pair = request.form.get("left_right_pair")
        if not left_right_pair:
            left_right_pair = False
        else:
            left_right_pair = True
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO lense_types (name, description,lense_category_id,lense_brand_id,left_right_pair) VALUES (%s,%s,%s,%s,%s);",(name,desc,category_id,brand_id,left_right_pair))
        conn.commit()
        return redirect(url_for("add_new_lense_type"))
    
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from brands")
    brands = cursor.fetchall()
    cursor.execute("SELECT * from categories")
    categories = cursor.fetchall()
    return render_template("add-new-lense-type.html",categories=categories,brands=brands)

@app.route("/all-lense-types")
def all_lense_types():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("select lense_types.id, lense_types.name, lense_types.description,categories.name AS category,brands.name AS brand,lense_types.left_right_pair from lense_types INNER JOIN categories ON lense_types.lense_category_id=categories.id INNER JOIN brands On lense_types.lense_brand_id=brands.id;")
    lense_types = cursor.fetchall()
    print(lense_types)
    return render_template("all-lense-types.html",lense_types=lense_types)

@app.route("/delete-lense-type/<string:id>")
def delete_lense_type(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from lense_types where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_lense_types"))

@app.route("/add-pricing-qty",methods=['GET','POST'])
def add_pricing_qty():
    if request.method=='POST':
        pass 
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from lense_types")
    lense = cursor.fetchall()
    return render_template("add-pricing-qty.html",lense=lense)

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