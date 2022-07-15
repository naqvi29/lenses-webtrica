from tempfile import tempdir
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
             return render_template("index2.html")
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

@app.route("/delete-inventory/<string:id>")
def delete_inventory(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from rx_items where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_rx_inventory"))

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

@app.route("/make-rx-order", methods=['GET','POST'])
def make_rx_order():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        date = request.form.get("date")
        reference = request.form.get("reference")
        customer_id = request.form.get("customer")
        billing_address = request.form.get("billing_address")
        description = request.form.get("dsc")
        
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

        cursor.execute("SELECT name from customers where id=%s",(customer_id))
        customer_name = cursor.fetchone()
        customer_name = customer_name[0]
        # temp    
        # cursor.execute("INSERT INTO rx_orders (date, reference, customer_id, customer_name, billing_address, description, item_id, item_name, item_desc, item_qty, item_price, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(date, reference, customer_id, customer_name, billing_address, description, item_id, item_name, item_desc, item_qty, item_price, total))
        cursor.execute("INSERT INTO rx_orders (date,reference,customer_id,customer_name,billing_address,description,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(date,reference,customer_id,customer_name,billing_address,description,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming))

        conn.commit()
        return redirect(url_for("make_rx_order"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    return render_template("make-rx-order.html",customers=customers)

@app.route("/make-rx-purchase", methods=['GET','POST'])
def make_rx_purchase():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        supplier_id = request.form.get("supplier")
        description = request.form.get("dsc")
        item_id = request.form.get("item")
        exp_account = request.form.get("exp_account")
        item_qty = request.form.get("item_qty")
        item_price = request.form.get("item_price")
        total = request.form.get("total")
        cursor.execute("SELECT name from suppliers where id=%s",(supplier_id))
        supplier_name = cursor.fetchone()
        supplier_name = supplier_name[0]
        cursor.execute("SELECT item_name from rx_items where id=%s",(item_id))
        item_name = cursor.fetchone()
        item_name = item_name[0]        
        cursor.execute("INSERT INTO rx_purchases (issue_date, due_date, reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, item_price, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(issue_date,due_date ,reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, item_price, total))
        conn.commit()
        return redirect(url_for("make_rx_purchase"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers;")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    return render_template("make-rx-purchase.html",suppliers=suppliers,rx_items=rx_items)

@app.route("/make-rx-invoice", methods=['GET','POST'])
def make_rx_invoice():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        customer_id = request.form.get("customer")
        billing_address = request.form.get("billing_address")
        description = request.form.get("dsc")
        item_id = request.form.get("item")
        exp_account = request.form.get("exp_account")
        item_qty = request.form.get("item_qty")
        item_price = request.form.get("item_price")
        total = request.form.get("total")
        cursor.execute("SELECT name from customers where id=%s",(customer_id))
        customer_name = cursor.fetchone()
        customer_name = customer_name[0]
        cursor.execute("SELECT item_name from rx_items where id=%s",(item_id))
        item_name = cursor.fetchone()
        item_name = item_name[0]       
        cursor.execute("INSERT INTO rx_invoices (issue_date, due_date, reference, customer_id, customer_name, billing_address, description, item_id, item_name, exp_account, item_qty, item_price, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(issue_date,due_date ,reference, customer_id, customer_name, billing_address, description, item_id, item_name, exp_account, item_qty, item_price, total))
        conn.commit()
        return redirect(url_for("make_rx_invoice"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    return render_template("make-rx-invoice.html",customers=customers,rx_items=rx_items)

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

@app.route("/delete-rx-invoice/<string:id>")
def delete_rx_invoice(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from rx_invoices where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_rx_invoice"))

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


@app.route("/view-rx-orders")
def view_rx_orders():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_orders;")
    rx_orders = cursor.fetchall()
    return render_template("view-rx-orders.html", rx_orders= rx_orders)

@app.route("/view-rx-purchase")
def view_rx_purchase():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_purchases;")
    rx_purchases = cursor.fetchall()
    return render_template("view-rx-purchase.html", rx_purchases= rx_purchases)

@app.route("/view-rx-invoice")
def view_rx_invoice():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_invoices;")
    rx_invoices = cursor.fetchall()
    return render_template("view-rx-invoice.html", rx_invoices= rx_invoices)

@app.route("/delete-rxorder/<string:id>")
def delete_rxorder(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from rx_orders where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_rx_orders"))

@app.route("/view-ingoing-or-outgoing")
def view_ingoing_or_outgoing():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from inoutreceipts;")
    data = cursor.fetchall()
    return render_template("view-ingoing-or-outgoing.html",data=data)

@app.route("/view-bank-and-cash-accounts")
def view_bank_and_cash_accounts():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from bankandcashaccounts;")
    data = cursor.fetchall()
    return render_template("view-bank-and-cash-accounts.html",data=data)

@app.route("/view-payments")
def view_payments():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from payments;")
    data = cursor.fetchall()
    return render_template("view-payments.html",data=data)

@app.route("/add-ingoing-or-outgoing", methods=['GET','POST'])
def add_ingoing_or_outgoing():
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        date= request.form.get("date")
        reference= request.form.get("reference")
        paid_by_account_type= request.form.get("paid_by_type")
        if paid_by_account_type=="other":
            paid_by_account_name = request.form.get("other_name")
            paid_by_account_id= None
        elif paid_by_account_type=="customer":
            paid_by_account_id = request.form.get("customer")             
            cursor.execute("SELECT name from customers where id=%s",(paid_by_account_id))
            customer = cursor.fetchone()
            paid_by_account_name = customer[0]
        elif paid_by_account_type=="supplier":
            paid_by_account_id = request.form.get("supplier")             
            cursor.execute("SELECT name from suppliers where id=%s",(paid_by_account_id))
            supplier = cursor.fetchone()
            paid_by_account_name = supplier[0]
        received_in_account_id= request.form.get("received_in_account")                     
        cursor.execute("SELECT name from bankandcashaccounts where id=%s",(received_in_account_id))
        received_in_account_name = cursor.fetchone()
        received_in_account_name=received_in_account_name[0]
        description= request.form.get("desc")
        exp_account= request.form.get("exp_account")
        print(exp_account)
        print(description)
        total_amount= float(request.form.get("amount"))
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO inoutreceipts (date,reference,paid_by_account_type, paid_by_account_id, paid_by_account_name, received_in_account_id, 	received_in_account_name, description, exp_account, total_amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(date,reference,paid_by_account_type,paid_by_account_id,paid_by_account_name,received_in_account_id,received_in_account_name,description,exp_account,total_amount))
        conn.commit()
        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(received_in_account_id))
        actual_balance = cursor.fetchone()
        actual_balance=actual_balance[0]
        update_balance = actual_balance + total_amount
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(update_balance,received_in_account_id))
        conn.commit()
        return redirect(url_for("add_ingoing_or_outgoing"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    return render_template("add-ingoing-or-outgoing.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts)

@app.route("/add-payments", methods=['GET','POST'])
def add_payments():
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        date= request.form.get("date")
        reference= request.form.get("reference")
        paid_from_account_id= request.form.get("paid_from")             
        cursor.execute("SELECT name from bankandcashaccounts where id=%s",(paid_from_account_id))
        bank = cursor.fetchone()
        paid_from_account_name = bank[0]
        payee_type= request.form.get("payee_type")
        if payee_type=="other":
            payee__name = request.form.get("other_name")
            payee_account_id= None
        elif payee_type=="customer":
            payee_account_id = request.form.get("customer")             
            cursor.execute("SELECT name from customers where id=%s",(payee_account_id))
            customer = cursor.fetchone()
            payee__name = customer[0]
        elif payee_type=="supplier":
            payee_account_id = request.form.get("supplier")             
            cursor.execute("SELECT name from suppliers where id=%s",(payee_account_id))
            supplier = cursor.fetchone()
            payee__name = supplier[0]
        description= request.form.get("desc")
        exp_account= request.form.get("exp_account")
        total_amount= float(request.form.get("amount"))
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO payments (date,reference,paid_from_account_id, paid_from_account_name, payee_type, payee_id, 	payee_name, description, exp_account, total_amount) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(date,reference,paid_from_account_id,paid_from_account_name,payee_type,payee_account_id,payee__name,description,exp_account,total_amount))
        conn.commit()
        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(paid_from_account_id))
        actual_balance = cursor.fetchone()
        actual_balance=actual_balance[0]
        update_balance = actual_balance - total_amount
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(update_balance,paid_from_account_id))
        conn.commit()
        return redirect(url_for("add_payments"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    return render_template("add-payments.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts)

@app.route("/add-bank-and-cash-accounts", methods=['GET','POST'])
def add_bank_and_cash_accounts():
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        name= request.form.get("name")
        code= request.form.get("code")
        starting_bal= float(request.form.get("starting_bal"))
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO bankandcashaccounts (name, code, actual_balance) VALUES (%s,%s,%s);",(name,code,starting_bal))
        conn.commit()
        return redirect(url_for("add_bank_and_cash_accounts"))
    return render_template("add-bank-and-cash-accounts.html")

@app.route("/deletepay/<string:type>/<int:id>")
def deletepay(type,id):
    conn = mysql.connect()
    cursor =conn.cursor()
    if type =="inout":
        cursor.execute("Delete from inoutreceipts where id=%s",(id))    
        conn.commit()
        return redirect(url_for("view_ingoing_or_outgoing"))
    elif type =="payments":
        cursor.execute("Delete from payments where id=%s",(id))       
        conn.commit()
        return redirect(url_for("view_payments")) 
    elif type =="bank_accounts":
        cursor.execute("Delete from bankandcashaccounts where id=%s",(id))    
        conn.commit()
        return redirect(url_for("view_bank_and_cash_accounts"))

@app.route("/view-rx-inventory")
def view_rx_inventory():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_items;")
    data = cursor.fetchall()
    return render_template("view-rx-inventory.html",data=data)

@app.route("/generate-rx-purchase/<int:id>")
def generate_rx_purchase(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_purchases where id=%s;",(id))
    rx_purchases = cursor.fetchone()
    return render_template("generate-rx-purchase.html", rx_purchases= rx_purchases)

@app.route("/generate-rx-invoice/<int:id>")
def generate_rx_invoice(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_invoices where id=%s;",(id))
    rx_invoices = cursor.fetchone()
    return render_template("generate-rx-invoice.html", rx_invoices= rx_invoices)

@app.route("/generate-rx-order/<int:id>")
def generate_rx_order(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_orders where id=%s;",(id))
    rx_orders = cursor.fetchone()
    return render_template("generate-rx-order.html", rx_orders= rx_orders)

@app.route("/generate-rx-item/<int:id>")
def generate_rx_item(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_items where id=%s;",(id))
    rx_items = cursor.fetchone()
    return render_template("generate-rx-item.html", rx_items= rx_items)


@app.route("/add-rx-item", methods=['GET','POST'])
def add_rx_item():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        if request.form.get("item_code"):
            item_code = request.form.get("item_code")
        else:
            item_code = None
        if request.form.get("desc"):
            description = request.form.get("desc")
        else:
            description = None
        item_name = request.form.get("item_name")
        unit_name = request.form.get("unit_name")
        purchase_price = request.form.get("purchase_price")
        sales_price = request.form.get("sales_price")
        qty = request.form.get("qty")
        average_cost = request.form.get("average_cost")
        total_cost = request.form.get("total_cost") 
        if not item_name and not unit_name and not purchase_price and not sales_price and not qty and not average_cost and not total_cost:
            return "Oops! Something is missing"      
        cursor.execute("INSERT INTO rx_items (item_code, item_name, unit_name, purchase_price, sales_price, qty, average_cost, description, total_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",(item_code,item_name ,unit_name, purchase_price, sales_price, qty, average_cost, description, total_cost))
        conn.commit()
        return redirect(url_for("add_rx_item"))
    return render_template("add-rx-item.html")




if __name__ == '__main__':
    app.run(debug=True)