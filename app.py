from click import confirm, password_option
from flask import Flask, render_template, request, session
from flask.helpers import url_for
from flaskext.mysql import MySQL
import os
from os.path import join, dirname, realpath
from importlib_metadata import method_cache
from werkzeug.utils import redirect, secure_filename
from PIL import Image

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_PASSWORD'] = 'LAwrence1234**'
app.config['MYSQL_DATABASE_DB'] = 'lenses'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# app.config['MYSQL_DATABASE_PORT'] = 3307
mysql.init_app(app)

# configure secret key for session protection)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            return render_template("login.html",error="Missing username or password!")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("SELECT * from users where email=%s and type='admin'",(email))
        data = cursor.fetchone()
        if data:
            if data[4] == password:                
                session['loggedin'] = True
                session['userid'] = data[0]
                session['name'] = data[1]
                session['type'] = data[6]
                return redirect(url_for("index"))
            else:
                return render_template("login.html",error="Invalid Password!")
        else:
                return render_template("login.html",error="Invalid Email!")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('name', None)
    session.pop('type', None)
    # Redirect to index page
    return redirect(url_for('login'))

@app.route("/")
def index():        
    if 'loggedin' in session:
        if session['type'] == 'admin':
             return render_template("index.html")
        else:
             return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

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
        lense_name= request.form.get("lense_name")
        cylinder= request.form.get("cylinder")
        spherical= request.form.get("spherical")
        quantity_left= request.form.get("quantity_left")
        quantity_right= request.form.get("quantity_right")
        price= request.form.get("price")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO pricing (lense_name, cylinder,spherical,quantity_left,quantity_right,price) VALUES (%s,%s,%s,%s,%s,%s);",(lense_name,cylinder,spherical,quantity_left,quantity_right,price))
        conn.commit()
        return redirect(url_for("add_pricing_qty"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from lense_types")
    lense = cursor.fetchall()
    return render_template("add-pricing-qty.html",lense=lense)

@app.route("/view-all-pricing")
def all_pricing():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from pricing;")
    pricing = cursor.fetchall()
    return render_template("all-pricing.html", pricing= pricing)

@app.route("/delete-pricing/<string:id>")
def delete_pricing(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from pricing where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_pricing"))

@app.route("/add-customer", methods=['GET','POST'])
def add_customer():
    if request.method=='POST':
        customer_name= request.form.get("customer_name")
        customer_email= request.form.get("customer_email")
        customer_phone= request.form.get("customer_phone")
        customer_address= request.form.get("customer_address")
        customer_description= request.form.get("customer_description")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO customers (name, email,phone,address,description) VALUES (%s,%s,%s,%s,%s);",(customer_name,customer_email,customer_phone,customer_address,customer_description))
        conn.commit()
        return redirect(url_for("add_customer"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    return render_template("add-customer.html",customers=customers)

@app.route("/view-all-customers")
def all_customers():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    return render_template("all-customers.html", customers= customers)


@app.route("/delete-customer/<string:id>")
def delete_customers(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from customers where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_customers"))

@app.route("/order-to-make", methods=['GET','POST'])
def order_to_make():
    if request.method == "POST":
        customer = request.form.get("customer")
        lense_type = request.form.get("lense_type")
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")
        
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        od_prism_no = request.form.get("od_prism_no")
        od_prism_detail = request.form.get("od_prism_detail")
        
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        os_prism_no = request.form.get("os_prism_no")
        os_prism_detail = request.form.get("os_prism_detail")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        oc_height = request.form.get("oc_height")
        od1 = request.form.get("od1")
        os1 = request.form.get("os1")
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")

        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO orders (customer,lense_type,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(customer,lense_type,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming))
        conn.commit()
        return redirect(url_for("order_to_make"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from lense_types;")
    lense_types = cursor.fetchall()
    return render_template("order-to-make.html",customers=customers,lense_types=lense_types)

@app.route("/add-supplier",methods=['GET','POST'])
def add_supplier():
    if request.method=='POST':
        name= request.form.get("name")
        email= request.form.get("email")
        phone= request.form.get("phone")
        address= request.form.get("address")
        desc= request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO suppliers (name, email, phone,address,description) VALUES (%s,%s,%s,%s,%s);",(name,email,phone,address,desc))
        conn.commit()
        return redirect(url_for("add_supplier"))
    return render_template("add-supplier.html")

@app.route("/all-suppliers")
def all_suppliers():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers;")
    suppliers = cursor.fetchall()
    return render_template("all-suppliers.html", suppliers= suppliers)

@app.route("/delete-suppliers/<string:id>")
def delete_suppliers(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from suppliers where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_suppliers"))

@app.route("/add-sale-receipt")
def add_sale_receipt():
    return render_template("add-sale-receipt.html")

@app.route("/add-sale-order")
def add_sale_order():
    return render_template("add-sale-order.html")

@app.route("/add-purchase-order")
def add_purchase_order():
    return render_template("add-purchase-order.html")

@app.route("/add-branch",methods=['GET','POST'])
def add_branch():
    if request.method=='POST':
        name= request.form.get("name")
        phone= request.form.get("phone")
        address= request.form.get("address")
        security_code= request.form.get("security_code")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO branch (name, phone,address,security_code) VALUES (%s,%s,%s,%s);",(name,phone,address,security_code))
        conn.commit()
        return redirect(url_for("add_branch"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from branch")
    branch = cursor.fetchall()
    return render_template("add-branch.html",branch=branch)

@app.route("/all-branch")
def all_branch():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from branch;")
    branch = cursor.fetchall()
    return render_template("all-branch.html", branch= branch)

@app.route("/delete-branch/<string:id>")
def delete_branch(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from branch where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_branch"))

@app.route("/add-user",methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        name= request.form.get("name")
        email= request.form.get("email")
        branch= request.form.get("branch")
        password= request.form.get("password")
        confirm_password= request.form.get("confirm_password")
        security_code= request.form.get("security_code")
        type = "user"
        
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("SELECT * from users where email=%s",(email))
        exist = cursor.fetchone()
        if exist:            
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT * from branch")
            branch = cursor.fetchall()
            return render_template("add-user.html",error="Email Address Already Exists",branch=branch)
        if password != confirm_password:            
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT * from branch")
            branch = cursor.fetchall()
            return render_template("add-user.html",error="Passwords doesn't match",branch=branch)
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO users (name, email,branch,password,security_code,type) VALUES (%s,%s,%s,%s,%s,%s);",(name,email,branch,password,security_code,type))
        conn.commit()
        return redirect(url_for("add_user"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from branch")
    branch = cursor.fetchall()
    return render_template("add-user.html",branch=branch)


@app.route("/all-users")
def all_users():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from users;")
    users = cursor.fetchall()
    return render_template("all-users.html", users= users)

@app.route("/delete-user/<string:id>")
def delete_user(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from users where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_users"))


@app.route("/all-orders")
def all_orders():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from orders;")
    orders = cursor.fetchall()
    return render_template("all-orders.html", orders= orders)

@app.route("/delete-order/<string:id>")
def delete_order(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from orders where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_orders"))

if __name__ == '__main__':
    app.run(debug=True)