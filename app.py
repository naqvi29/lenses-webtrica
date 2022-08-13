
from re import T
from flask import Flask, render_template, request, session, jsonify
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
app.config['MYSQL_DATABASE_PORT'] = 3307
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
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM customers;")
            customers = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM users;")
            users = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM branch;")
            branch = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM suppliers;")
            suppliers = cursor.fetchone()[0]
            return render_template("index2.html",customers=customers,users=users,branches=branch,suppliers=suppliers)
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

@app.route("/edit-category/<string:id>", methods=['GET','POST'])
def edit_category(id):
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE categories SET name=%s,description=%s WHERE id=%s; ",(name,desc,id))
        conn.commit()
        return redirect(url_for("all_category"))
        
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from categories where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-category.html",data=data)


@app.route("/add-treatment", methods=['GET','POST'])
def add_treatment():
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO treatments (name, description) VALUES (%s,%s);",(name,desc))
        conn.commit()
        return redirect(url_for("view_treatments"))
    return render_template("add-treatment.html")

@app.route("/edit-treatment/<string:id>", methods=['GET','POST'])
def edit_treatment(id):
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()        
        cursor.execute("UPDATE treatments SET name=%s,description=%s WHERE id=%s; ",(name,desc,id))
        conn.commit()
        return redirect(url_for("view_treatments"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from treatments where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-treatment.html",data=data)


@app.route("/add-tints-of-service", methods=['GET','POST'])
def add_tints_of_service():
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO tints_of_services (name, description) VALUES (%s,%s);",(name,desc))
        conn.commit()
        return redirect(url_for("view_tints_of_services"))
    return render_template("add-tints-of-service.html")

@app.route("/edit-tints-of-service/<string:id>", methods=['GET','POST'])
def edit_tints_of_service(id):
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE tints_of_services SET name=%s,description=%s WHERE id=%s; ",(name,desc,id))
        conn.commit()   
    
        return redirect(url_for("view_tints_of_services"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from tints_of_services where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-tints-of-service.html",data=data)

@app.route("/all-category")
def all_category():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from categories")
    categories = cursor.fetchall()
    return render_template("all-category.html",categories=categories)

@app.route("/view-treatments")
def view_treatments():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from treatments")
    treatments = cursor.fetchall()
    return render_template("view-treatments.html",treatments=treatments)

@app.route("/view-tints-of-services")
def view_tints_of_services():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from tints_of_services")
    tints_of_services = cursor.fetchall()
    return render_template("view-tints-of-services.html",tints_of_services=tints_of_services)

@app.route("/delete-category/<string:id>")
def delete_category(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from categories where id=%s",(id))
    conn.commit()
    return redirect(url_for("all_category"))

@app.route("/delete-tints-of-service/<string:id>")
def delete_tints_of_service(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from tints_of_services where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_tints_of_services"))

@app.route("/delete-treatment/<string:id>")
def delete_treatment(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from treatments where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_treatments"))

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

@app.route("/edit-brand/<string:id>",methods=['GET','POST'])
def edit_brand(id):
    if request.method=='POST':
        name = request.form.get("name")
        desc = request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE brands SET name=%s,description=%s WHERE id=%s; ",(name,desc,id))
        conn.commit()
        return redirect(url_for("all_brand"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from brands where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-brand.html",data=data)


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
        # customer_description= request.form.get("customer_description")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO customers (name, email,phone,address) VALUES (%s,%s,%s,%s);",(customer_name,customer_email,customer_phone,customer_address))
        conn.commit()
        return redirect(url_for("add_customer"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    return render_template("add-customer.html",customers=customers)

@app.route("/edit-customer/<string:id>", methods=['GET','POST'])
def edit_customer(id):
    if request.method=='POST':
        customer_name= request.form.get("customer_name")
        customer_email= request.form.get("customer_email")
        customer_phone= request.form.get("customer_phone")
        customer_address= request.form.get("customer_address")
        # customer_description= request.form.get("customer_description")
        conn = mysql.connect()
        cursor =conn.cursor()        
        cursor.execute("UPDATE customers SET name=%s,email=%s,phone=%s,address=%s WHERE id=%s; ",(customer_name,customer_email,customer_phone,customer_address,id))
        conn.commit()
        return redirect(url_for("all_customers"))
    conn = mysql.connect()
    cursor =conn.cursor()
    
    cursor.execute("SELECT * from customers where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-customer.html",data=data)

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
        # order_number = request.form.get("order_number")
        
        customer_id = request.form.get("customer")
        item_id = request.form.get("item_id")
        billing_address = request.form.get("billing_address")
        # cost_price = request.form.get("cost_price")
        # sales_price = request.form.get("sales_price")
        # qty = request.form.get("qty")
        # description = request.form.get("dsc")
        description = None
        
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        # od_prism_no = request.form.get("od_prism_no")
        od_prism_no = None
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        # od1 = request.form.get("od1")
        # os1 = request.form.get("os1")
        od1 = None
        os1 = None
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")
        status = "pending"
        total_amount = request.form.get("total_amount")

        cursor.execute("SELECT name from customers where id=%s",(customer_id))
        customer_name = cursor.fetchone()
        customer_name = customer_name[0]
        cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        item_name = cursor.fetchone()
        print("item name is: ",item_name)
        item_name = item_name[0]
        print("item name is: ",item_name)
        order_number = None
        cursor.execute("INSERT INTO rx_orders (date,reference,order_number,customer_id,customer_name,item_id,item_name,billing_address,description,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming,status,od_size,os_size,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,total_amount,frame_size_v,frame_size_d) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(date,reference,order_number,customer_id,customer_name,item_id,item_name,billing_address,description,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming,status,od_size,os_size,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,total_amount,frame_size_v,frame_size_d))
        

        conn.commit()
        # todo 
        # cursor.execute("SELECT LAST_INSERT_ID(id) From rx_orders;")
        cursor.execute("SELECT MAX( id ) FROM rx_orders;")
        last_row_id = cursor.fetchone()
        last_row_id = last_row_id[0]
        print("last row id is:........ ",last_row_id)
        order_number = "gos-"+str(last_row_id)
        cursor.execute("UPDATE rx_orders SET order_number=%s WHERE id=%s; ",(order_number,last_row_id))
        conn.commit()
        # ..
        return redirect(url_for("view_rx_orders"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    # customers2=[]    
    # for i in customers:
    #     dict = {}
    #     dict.update({"customerid":i[0],"customer_name":i[1],"billing_address":i[4]})
    #     customers2.append(dict)
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from treatments;")
    treatments = cursor.fetchall()
    cursor.execute("SELECT * from tints_of_services;")
    tints_of_services = cursor.fetchall()
    # todo write query which fetch the id of last inserted row in rx_orders
    
    # cursor.execute("select id from rx_orders ORDER BY id DESC LIMIT 1;;")
    # last_row_id = cursor.fetchone()
    # reference = last_row_id[0]+1
    return render_template("make-rx-order.html",customers=customers,rx_items=rx_items,treatments=treatments,tints_of_services=tints_of_services)

@app.route("/edit-rxorder/<string:id>", methods=['GET','POST'])
def edit_rxorder(id):
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        date = request.form.get("date")
        reference = request.form.get("reference")
        order_number = request.form.get("order_number")
        customer_name = request.form.get("customer")
        item_name = request.form.get("item_name")
        billing_address = request.form.get("billing_address")
        # description = request.form.get("dsc")
        description = None
        
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        # od_prism_no = request.form.get("od_prism_no")
        od_prism_no = None
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        # od1 = request.form.get("od1")
        # os1 = request.form.get("os1")
        od1 = None
        os1 = None
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")
        status = "pending"
        total_amount = request.form.get("total_amount")

        # cursor.execute("SELECT name from customers where id=%s",(customer_id))
        # customer_name = cursor.fetchone()
        # customer_name = customer_name[0]
        # cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        # item_name = cursor.fetchone()
        # print("item name is: ",item_name)
        # item_name = item_name[0]
        # print("item name is: ",item_name)
        # temp    

        
        cursor.execute("UPDATE rx_orders SET date=%s, reference=%s, order_number=%s,customer_name=%s, item_name=%s,billing_address=%s, description=%s,treatment=%s, tint_service=%s,od_sph=%s, od_cyl=%s,od_axis=%s, od_add=%s,od_base=%s, od_fh=%s,od_prism_no=%s, od_prism_detail=%s,os_sph=%s, os_cyl=%s,os_axis=%s, os_add=%s,os_base=%s, os_fh=%s,os_prism_no=%s, os_prism_detail=%s,bvd_mm=%s, face_angle=%s,pantoscopic_Angle=%s, nrd=%s, decentration=%s,center_edge=%s, frame_size_h=%s,oc_height=%s, od1=%s,os1=%s, occupation=%s,driving=%s, computer=%s,reading=%s, mobile=%s,gaming=%s,status=%s,od_size=%s,os_size=%s,od_cost_price=%s,od_sales_price=%s,od_qty=%s,os_cost_price=%s,os_sales_price=%s,os_qty=%s,od_pd=%s,os_pd=%s,total_amount=%s,frame_size_v=%s,frame_size_d=%s WHERE id=%s; ",(date,reference,order_number,customer_name,item_name,billing_address,description,treatment,tint_service,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_no,od_prism_detail,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_no,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,od1,os1,occupation,driving,computer,reading,mobile,gaming,status,od_size,os_size,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,total_amount,frame_size_v,frame_size_d,id))
        

        conn.commit()
        return redirect(url_for("view_rx_orders"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from treatments;")
    treatments = cursor.fetchall()
    cursor.execute("SELECT * from tints_of_services;")
    tints_of_services = cursor.fetchall()
    cursor.execute("SELECT * from rx_orders where id=%s;",(id))
    data = cursor.fetchone()
    # todo write query which fetch the id of last inserted row in rx_orders
    
    # cursor.execute("select id from rx_orders ORDER BY id DESC LIMIT 1;;")
    # last_row_id = cursor.fetchone()
    # reference = last_row_id[0]+1
    return render_template("edit-rx-order.html",customers=customers,rx_items=rx_items,treatments=treatments,tints_of_services=tints_of_services,data=data)


@app.route("/make-rx-purchase", methods=['GET','POST'])
def make_rx_purchase():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        supplier_id = request.form.get("supplier")
        # description = request.form.get("dsc")
        description = None
        item_id = request.form.get("item_idd")
        item_name = request.form.get("item_name")
        exp_account = request.form.get("exp_account")
        # item_qty = request.form.get("qty")
        item_qty = None
        # cost_price = request.form.get("cost_price")
        cost_price = None
        total_amount = request.form.get("total_amount")
        # status = request.form.get("status")
        status = None
        cursor.execute("SELECT name from suppliers where id=%s",(supplier_id))
        supplier_name = cursor.fetchone()
        supplier_name = supplier_name[0]
        # cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        # item_name = cursor.fetchone()
        # item_name = item_name[0]     
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")  
        cursor.execute("INSERT INTO rx_purchases (issue_date, due_date, reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, cost_price, total_amount,status,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,occupation,driving,computer,reading,mobile,gaming,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,frame_size_v,frame_size_d,treatment,tint_service) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(issue_date,due_date ,reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, cost_price, total_amount,status,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,occupation,driving,computer,reading,mobile,gaming,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,frame_size_v,frame_size_d,treatment,tint_service))
        conn.commit()

        # now fetch supplier bal 
        cursor.execute("SELECT actual_bal from suppliers where id=%s",(supplier_id))
        supplier_bal = cursor.fetchone()
        supplier_bal=supplier_bal[0]
        new_bal = float(supplier_bal)+float(total_amount)
        # update supplier bal 
        cursor.execute("UPDATE suppliers SET actual_bal=%s WHERE id=%s; ",(new_bal,supplier_id))
        conn.commit()

        # now increase item qty in inventory 
        # cursor.execute("SELECT qty from rx_items where id=%s",(item_id))
        # actual_qty = cursor.fetchone()
        # actual_qty=actual_qty[0]
        # print("item_id :",item_id)
        # print("actual_qty :",actual_qty)
        # print("item_qty :",item_qty)
        # updated_qty = int(actual_qty) + int(item_qty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,item_id))
        # conn.commit()

        # now change order status from pending to in process
        # cursor.execute("SELECT id from rx_orders where order_number=%s",(reference))
        # order_id = cursor.fetchone()
        # if order_id:
        #     cursor.execute("UPDATE rx_orders SET status='inprocess' WHERE id=%s; ",(order_id))
        #     conn.commit()

        
        return redirect(url_for("view_rx_purchase"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers;")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from rx_orders;")
    rx_orders = cursor.fetchall()
    return render_template("make-rx-purchase.html",suppliers=suppliers,rx_items=rx_items,rx_orders=rx_orders)

@app.route("/edit-rx-purchase/<string:id>", methods=['GET','POST'])
def edit_rx_purchase(id):
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        supplier_id = request.form.get("supplier_id")
        supplier_name = request.form.get("supplier_name")
        # description = request.form.get("dsc")
        description = None
        item_id = request.form.get("item_idd")
        item_name = request.form.get("item_name")
        exp_account = request.form.get("exp_account")
        # item_qty = request.form.get("qty")
        item_qty = None
        # cost_price = request.form.get("cost_price")
        cost_price = None
        total_amount = request.form.get("total_amount")
        # status = request.form.get("status")
        status = None
        # cursor.execute("SELECT name from suppliers where id=%s",(supplier_id))
        # supplier_name = cursor.fetchone()
        # supplier_name = supplier_name[0]
        # cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        # item_name = cursor.fetchone()
        # item_name = item_name[0]     
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")
        # cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        # item_name = cursor.fetchone()
        # item_name = item_name[0]    
        # fetch old item id and quantity      
        # cursor.execute("SELECT item_id,item_qty from rx_purchases where id=%s",(id))
        # prevData = cursor.fetchone()
        # prevItemID=prevData[0]
        # prevItemQty=prevData[1]

        # cursor.execute("INSERT INTO rx_purchases (issue_date, due_date, reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, item_price, total,status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s);",(issue_date,due_date ,reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, item_price, total,status))

        # fetch old total amount      
        cursor.execute("SELECT total_amount from rx_purchases where id=%s",(id))
        prevData = cursor.fetchone()
        prev_total_amount=prevData[0]

        cursor.execute("UPDATE rx_purchases SET issue_date=%s,due_date=%s,reference=%s,supplier_id=%s,supplier_name=%s,description=%s,item_id=%s,item_name=%s,exp_account=%s,item_qty=%s,cost_price=%s,total_amount=%s,status=%s,od_size=%s,od_sph=%s,od_cyl=%s,od_axis=%s,od_add=%s,od_base=%s,od_fh=%s,od_prism_detail=%s,os_size=%s,os_sph=%s,os_cyl=%s,os_axis=%s,os_add=%s,os_base=%s,os_fh=%s,os_prism_detail=%s,bvd_mm=%s,face_angle=%s,pantoscopic_Angle=%s,nrd=%s,decentration=%s,center_edge=%s,oc_height=%s,occupation=%s,driving=%s,computer=%s,reading=%s,mobile=%s,gaming=%s,od_cost_price=%s,od_sales_price=%s,od_qty=%s,os_cost_price=%s,os_sales_price=%s,os_qty=%s,od_pd=%s,os_pd=%s,frame_size_h=%s,frame_size_v=%s,frame_size_d=%s,treatment=%s,tint_service=%s WHERE id=%s; ",(issue_date,due_date ,reference, supplier_id, supplier_name, description, item_id, item_name, exp_account, item_qty, cost_price, total_amount,status,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,oc_height,occupation,driving,computer,reading,mobile,gaming,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,frame_size_h,frame_size_v,frame_size_d,treatment,tint_service,id))
        conn.commit()

        # now fetch supplier bal 
        cursor.execute("SELECT actual_bal from suppliers where id=%s",(supplier_id))
        supplier_bal = cursor.fetchone()
        supplier_bal=supplier_bal[0]
        new_bal = float(supplier_bal)-float(prev_total_amount)
        new_bal = float(new_bal)+float(total_amount)
        # update supplier bal 
        cursor.execute("UPDATE suppliers SET actual_bal=%s WHERE id=%s; ",(new_bal,supplier_id))
        conn.commit()

        

        # undo old record 
        # cursor.execute("SELECT qty from rx_items where id=%s",(prevItemID))
        # prev_qty = cursor.fetchone()
        # prev_qty=prev_qty[0]
        # updated_qty = int(prev_qty) - int(prevItemQty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,prevItemID))
        # conn.commit()

        # now increase item qty in inventory 
        # cursor.execute("SELECT qty from rx_items where id=%s",(item_id))
        # actual_qty = cursor.fetchone()
        # actual_qty=actual_qty[0]
        # updated_qty = int(actual_qty) + int(item_qty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,item_id))
        # conn.commit()
        
        return redirect(url_for("view_rx_purchase"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers;")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from rx_purchases where id=%s;",(id))
    data = cursor.fetchone()
    return render_template("edit-rx-purchase.html",suppliers=suppliers,rx_items=rx_items,data=data)


@app.route("/make-rx-invoice", methods=['GET','POST'])
def make_rx_invoice():
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        print("reference is: ",reference)
        customer_id = request.form.get("customer_id")
        customer_name = request.form.get("customer_name")
        billing_address = request.form.get("billing_address")
        # description = request.form.get("dsc")
        description = None 
        item_id = request.form.get("item_idd")
        item_name = request.form.get("item_name")
        exp_account = request.form.get("exp_account")
        # item_qty = request.form.get("qty")
        # sales_price = request.form.get("sales_price")
        item_qty = None
        sales_price = None
        total_amount = request.form.get("total_amount")
            
            
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")  
        cursor.execute("INSERT INTO rx_invoices (issue_date, due_date, reference, customer_id, customer_name,billing_address, description, item_id, item_name, exp_account, item_qty, sales_price, total_amount,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,occupation,driving,computer,reading,mobile,gaming,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,frame_size_v,frame_size_d,treatment,tint_service) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(issue_date,due_date ,reference, customer_id, customer_name,billing_address, description, item_id, item_name, exp_account, item_qty, sales_price, total_amount,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,frame_size_h,oc_height,occupation,driving,computer,reading,mobile,gaming,od_cost_price,od_sales_price,od_qty,os_cost_price,os_sales_price,os_qty,od_pd,os_pd,frame_size_v,frame_size_d,treatment,tint_service))
        conn.commit()

        # now change order status to ready 
        # cursor.execute("SELECT id from rx_orders where order_number=%s;",(reference))
        # order_id = cursor.fetchone()
        # order_id=order_id[0]
        # print("Gorder_id is: ",order_id)
        cursor.execute("UPDATE rx_orders SET status='ready' WHERE id=%s;",(reference))
        conn.commit()


        # cursor.execute("INSERT INTO rx_invoices (issue_date, due_date, reference, customer_id, customer_name, billing_address, description, item_id, item_name, exp_account, item_qty, sales_price, total,od_size,od_sph ,od_cyl ,od_axis ,od_add , od_base,od_fh , os_size,os_sph ,os_cyl, os_axis,os_add , os_base,os_fh,os_prism_detail, od_prism_detail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",(issue_date,due_date ,reference, customer_id, customer_name, billing_address, description, item_id, item_name, exp_account, item_qty, sales_price, total,od_size,od_sph ,od_cyl ,od_axis ,od_add , od_base,od_fh , os_size,os_sph ,os_cyl, os_axis,os_add , os_base,os_fh,os_prism_detail, od_prism_detail))
        # conn.commit()
        # now decrease item qty in inventory 
        # cursor.execute("SELECT qty from rx_items where id=%s",(item_id))
        # actual_qty = cursor.fetchone()
        # actual_qty=actual_qty[0]
        # updated_qty = int(actual_qty) - int(item_qty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,item_id))
        # conn.commit()

        # now change order status from in process to ready 
        # cursor.execute("SELECT id from rx_orders where order_number=%s",(reference))
        # order_id = cursor.fetchone()
        # cursor.execute("UPDATE rx_orders SET status='ready' WHERE id=%s; ",(order_id))
        # conn.commit()

        return redirect(url_for("view_rx_invoice"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from rx_orders;")
    rx_orders = cursor.fetchall()
    return render_template("make-rx-invoice.html",customers=customers,rx_items=rx_items,rx_orders=rx_orders)

@app.route("/edit-rx-invoice/<string:id>", methods=['GET','POST'])
def edit_rx_invoice(id):
    if request.method == "POST": 
        conn = mysql.connect()
        cursor =conn.cursor()
        issue_date = request.form.get("issue_date")
        due_date = request.form.get("due_date")
        reference = request.form.get("reference")
        customer_name= request.form.get("customer_name")
        billing_address = request.form.get("billing_address")
        # description = request.form.get("dsc")
        description = None
        item_name = request.form.get("item_name")
        exp_account = request.form.get("exp_account")
        # item_qty = request.form.get("qty")
        item_qty = None
        # sales_price = request.form.get("sales_price")
        sales_price = None
        total_amount = request.form.get("total_amount")
            
            
        treatment = request.form.get("treatment")
        tint_service = request.form.get("tint_service")

        od_size = request.form.get("od_size")
        od_sph = request.form.get("od_sph")
        od_cyl = request.form.get("od_cyl")
        od_axis = request.form.get("od_axis")
        od_add = request.form.get("od_add")
        od_base = request.form.get("od_base")
        od_fh = request.form.get("od_fh")
        od_prism_detail = request.form.get("od_prism_detail")
        od_pd = request.form.get("od_pd")
        od_cost_price = request.form.get("od_cost_price")
        od_sales_price = request.form.get("od_sales_price")
        od_qty = request.form.get("od_qty")
        
        os_size = request.form.get("os_size")
        os_sph = request.form.get("os_sph")
        os_cyl = request.form.get("os_cyl")
        os_axis = request.form.get("os_axis")
        os_add = request.form.get("os_add")
        os_base = request.form.get("os_base")
        os_fh = request.form.get("os_fh")
        # os_prism_no = request.form.get("os_prism_no")
        
        os_prism_no = None
        os_prism_detail = request.form.get("os_prism_detail")
        os_pd = request.form.get("os_pd")
        os_cost_price = request.form.get("os_cost_price")
        os_sales_price = request.form.get("os_sales_price")
        os_qty = request.form.get("os_qty")
        
        bvd_mm = request.form.get("bvd_mm")
        face_angle = request.form.get("face_angle")
        pantoscopic_Angle = request.form.get("pantoscopic_Angle")
        nrd = request.form.get("nrd")
        decentration = request.form.get("decentration")
        center_edge = request.form.get("center_edge")
        frame_size_h = request.form.get("frame_size_h")
        frame_size_v = request.form.get("frame_size_v")
        frame_size_d = request.form.get("frame_size_d")
        oc_height = request.form.get("oc_height")
        occupation = request.form.get("occupation")
        driving = request.form.get("driving")
        computer = request.form.get("computer")
        reading = request.form.get("reading")
        mobile = request.form.get("mobile")
        gaming = request.form.get("gaming")
        # cursor.execute("SELECT name from customers where id=%s",(customer_id))
        # customer_name = cursor.fetchone()
        # customer_name = customer_name[0]
        # cursor.execute("SELECT lense_type from rx_items where id=%s",(item_id))
        # item_name = cursor.fetchone()
        # item_name = item_name[0]   

        # fetch old item id and quantity      
        # cursor.execute("SELECT item_id,item_qty from rx_invoices where id=%s",(id))
        # prevData = cursor.fetchone()
        # prevItemID=prevData[0]
        # prevItemQty=prevData[1]

        # cursor.execute("UPDATE rx_invoices SET issue_date=%s,due_date=%s,reference=%s,customer_name=%s,billing_address=%s,description=%s,item_name=%s,exp_account=%s,item_qty=%s,sales_price=%s,total=%s,od_size=%s,od_sph=%s,od_cyl=%s,od_axis=%s,od_add=%s,od_base=%s,od_fh=%s,os_size=%s,os_sph=%s,os_cyl=%s,os_axis=%s,os_add=%s,os_base=%s,os_fh=%s,os_prism_detail=%s,od_prism_detail=%s WHERE id=%s; ",(issue_date,due_date ,reference,  customer_name, billing_address, description, item_name, exp_account, item_qty, sales_price, total,od_size,od_sph ,od_cyl ,od_axis ,od_add , od_base,od_fh , os_size,os_sph ,os_cyl, os_axis,os_add , os_base,os_fh,os_prism_detail, od_prism_detail,id))
        # conn.commit()

        cursor.execute("UPDATE rx_invoices SET issue_date=%s,due_date=%s,reference=%s,customer_name=%s,billing_address=%s,description=%s,item_name=%s,exp_account=%s,item_qty=%s,sales_price=%s,total_amount=%s,od_size=%s,od_sph=%s,od_cyl=%s,od_axis=%s,od_add=%s,od_base=%s,od_fh=%s,od_prism_detail=%s,os_size=%s,os_sph=%s,os_cyl=%s,os_axis=%s,os_add=%s,os_base=%s,os_fh=%s,os_prism_detail=%s,bvd_mm=%s,face_angle=%s,pantoscopic_Angle=%s,nrd=%s,decentration=%s,center_edge=%s,oc_height=%s,occupation=%s,driving=%s,computer=%s,reading=%s,mobile=%s,gaming=%s,od_sales_price=%s,od_qty=%s,os_sales_price=%s,os_qty=%s,od_pd=%s,os_pd=%s,frame_size_h=%s,frame_size_v=%s,frame_size_d=%s,treatment=%s,tint_service=%s WHERE id=%s; ",(issue_date,due_date ,reference, customer_name,billing_address, description, item_name, exp_account, item_qty, sales_price, total_amount,od_size,od_sph,od_cyl,od_axis,od_add,od_base,od_fh,od_prism_detail,os_size,os_sph,os_cyl,os_axis,os_add,os_base,os_fh,os_prism_detail,bvd_mm,face_angle,pantoscopic_Angle,nrd,decentration,center_edge,oc_height,occupation,driving,computer,reading,mobile,gaming,od_sales_price,od_qty,os_sales_price,os_qty,od_pd,os_pd,frame_size_h,frame_size_v,frame_size_d,treatment,tint_service,id))
        
        conn.commit()

        # undo old record 
        # cursor.execute("SELECT qty from rx_items where id=%s",(prevItemID))
        # prev_qty = cursor.fetchone()
        # prev_qty=prev_qty[0]
        # updated_qty = int(prev_qty) + int(prevItemQty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,prevItemID))
        # conn.commit()

        # now decrease item qty in inventory 
        # cursor.execute("SELECT qty from rx_items where id=%s",(item_id))
        # actual_qty = cursor.fetchone()
        # actual_qty=actual_qty[0]
        # updated_qty = int(actual_qty) - int(item_qty)
        # cursor.execute("UPDATE rx_items SET qty=%s WHERE id=%s; ",(updated_qty,item_id))
        # conn.commit()
        return redirect(url_for("view_rx_invoice"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers;")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from rx_items;")
    rx_items = cursor.fetchall()
    cursor.execute("SELECT * from rx_invoices where id=%s;",(id))
    data = cursor.fetchone()
    return render_template("edit-rx-invoice.html",customers=customers,rx_items=rx_items,data=data)


@app.route("/add-supplier",methods=['GET','POST'])
def add_supplier():
    if request.method=='POST':
        name= request.form.get("name")
        email= request.form.get("email")
        phone= request.form.get("phone")
        address= request.form.get("address")
        desc= request.form.get("desc")
        starting_bal= request.form.get("starting_bal")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO suppliers (name, email, phone,address,description,actual_bal) VALUES (%s,%s,%s,%s,%s,%s);",(name,email,phone,address,desc,starting_bal))
        conn.commit()
        return redirect(url_for("add_supplier"))
    return render_template("add-supplier.html")

@app.route("/edit-supplier/<string:id>",methods=['GET','POST'])
def edit_supplier(id):
    if request.method=='POST':
        name= request.form.get("name")
        email= request.form.get("email")
        phone= request.form.get("phone")
        address= request.form.get("address")
        desc= request.form.get("desc")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE suppliers SET name=%s,email=%s,phone=%s,address=%s,description=%s WHERE id=%s; ",(name,email,phone,address,desc,id))
        conn.commit()
        return redirect(url_for("all_suppliers"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-supplier.html",data=data)

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

@app.route("/delete-rx-purchase/<string:id>")
def delete_rx_purchase(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("Delete from rx_purchases where id=%s",(id))
    conn.commit()
    return redirect(url_for("view_rx_purchase"))

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

@app.route("/edit-branch/<string:id>",methods=['GET','POST'])
def edit_branch(id):
    if request.method=='POST':
        name= request.form.get("name")
        phone= request.form.get("phone")
        address= request.form.get("address")
        security_code= request.form.get("security_code")
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE branch SET name=%s,phone=%s,address=%s,security_code=%s WHERE id=%s; ",(name,phone,address,security_code,id))
        conn.commit()
        return redirect(url_for("all_branch"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from branch where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-branch.html",data=data)

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
@app.route("/edit-user/<string:id>",methods=['GET','POST'])
def edit_user(id):
    if request.method=='POST':
        name= request.form.get("name")
        email= request.form.get("email")
        branch= request.form.get("branch")
        password= request.form.get("password")
        confirm_password= request.form.get("confirm_password")
        security_code= request.form.get("security_code")
        type = "user"
        
        if password != confirm_password:            
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT * from branch")
            branch = cursor.fetchall()
            cursor.execute("SELECT * from users where id=%s",(id))
            data = cursor.fetchone()
            return render_template("edit-user.html",error="Passwords doesn't match",branch=branch,data=data)
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE users set name=%s, email=%s,branch=%s,password=%s,security_code=%s where id=%s;",(name,email,branch,password,security_code,id))
        conn.commit()
        return redirect(url_for("all_users"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from branch")
    branch = cursor.fetchall()
    cursor.execute("SELECT * from users where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-user.html",branch=branch,data=data)


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

@app.route("/view-receipts")
def view_receipts():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from inoutreceipts;")
    data = cursor.fetchall()
    return render_template("view-receipts.html",data=data)

@app.route("/view-bank-accounts")
def view_bank_accounts():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from bank_accounts;")
    data = cursor.fetchall()
    return render_template("view-bank-accounts.html",data=data)
@app.route("/view-cash-accounts")
def view_cash_accounts():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from cash_accounts;")
    data = cursor.fetchall()
    return render_template("view-cash-accounts.html",data=data)

@app.route("/view-payments")
def view_payments():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from payments;")
    data = cursor.fetchall()
    return render_template("view-payments.html",data=data)

@app.route("/add-receipts", methods=['GET','POST'])
def add_receipts():
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
        return redirect(url_for("add_receipts"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    return render_template("add-receipts.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts)

@app.route("/edit-receipts/<string:id>", methods=['GET','POST'])
def edit_receipts(id):
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        date= request.form.get("date")
        # reference= request.form.get("reference")
        paid_by_account_type= request.form.get("paid_by_type")
        print(paid_by_account_type)
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
            print(paid_by_account_id)             
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
        
        # fetch previous amount from receippt
        cursor.execute("SELECT total_amount,received_in_account_id from inoutreceipts where id=%s",(id))
        data = cursor.fetchone()
        prev_bal=data[0]
        prev_received_in_account_id=data[1]

        # update receipt 
        cursor.execute("UPDATE inoutreceipts SET date=%s, paid_by_account_type=%s,paid_by_account_id=%s,paid_by_account_name=%s,received_in_account_id=%s,received_in_account_name=%s,description=%s,exp_account=%s,total_amount=%s WHERE id=%s;",(date,paid_by_account_type,paid_by_account_id,paid_by_account_name,received_in_account_id,received_in_account_name,description,exp_account,total_amount,id))
        conn.commit()

        
        

        # undo prev record 
        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(prev_received_in_account_id))
        actual_balance0 = cursor.fetchone()
        actual_balance0=actual_balance0[0]
        u = actual_balance0 - prev_bal
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(u,prev_received_in_account_id))
        conn.commit()

        # now update new record

        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(received_in_account_id))
        actual_balance = cursor.fetchone()
        actual_balance=actual_balance[0]
        update_balance = actual_balance + total_amount
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(update_balance,received_in_account_id))
        conn.commit()
        return redirect(url_for("view_receipts"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    cursor.execute("SELECT * from inoutreceipts where id=%s",id)
    data = cursor.fetchone()
    return render_template("edit-receipts.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts,data=data)

@app.route("/edit-payments/<string:id>", methods=['GET','POST'])
def edit_payments(id):
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
        
        payee_name = request.form.get("payee_name")
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
        
        # fetch prev record  
        cursor.execute("SELECT paid_from_account_id,total_amount from payments where id=%s",(id))
        prev_rec = cursor.fetchone()
        prev_paid_from_account_id=prev_rec[0]
        prev_total_amount=prev_rec[1]

        cursor.execute("UPDATE payments SET date=%s,reference=%s,paid_from_account_name=%s,payee_type=%s,payee_name=%s,description=%s,exp_account=%s,total_amount=%s where id=%s;",(date,reference,paid_from_account_id,payee_type,payee_name,description,exp_account,total_amount,id))
        conn.commit()

        # undo prev record 
        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(prev_paid_from_account_id))
        prev_account_bal = cursor.fetchone()
        prev_account_bal=prev_account_bal[0]
        u_account_bal = float(prev_account_bal) + float(prev_total_amount)
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(u_account_bal,prev_paid_from_account_id))
        conn.commit()
        
        cursor.execute("SELECT actual_balance from bankandcashaccounts where id=%s",(paid_from_account_id))
        actual_balance = cursor.fetchone()
        actual_balance=actual_balance[0]
        update_balance = actual_balance - total_amount
        cursor.execute("UPDATE bankandcashaccounts SET actual_balance=%s WHERE id=%s; ",(update_balance,paid_from_account_id))
        conn.commit()
        
        return redirect(url_for("view_payments"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    cursor.execute("SELECT * from payments where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-payments.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts,data=data)

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
        return redirect(url_for("view_payments"))
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers")
    customers = cursor.fetchall()
    cursor.execute("SELECT * from suppliers")
    suppliers = cursor.fetchall()
    cursor.execute("SELECT * from bankandcashaccounts")
    bank_accounts = cursor.fetchall()
    return render_template("add-payments.html",customers=customers,suppliers=suppliers, bank_accounts=bank_accounts)

@app.route("/add-bank-accounts", methods=['GET','POST'])
def add_bank_accounts():
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        name= request.form.get("name")
        code= request.form.get("code")
        starting_bal= float(request.form.get("starting_bal"))
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO bank_accounts (name, code, actual_balance) VALUES (%s,%s,%s);",(name,code,starting_bal))
        conn.commit()
        return redirect(url_for("view_bank_accounts"))
    return render_template("add-bank-accounts.html")
@app.route("/add-cash-accounts", methods=['GET','POST'])
def add_cash_accounts():
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        name= request.form.get("name")
        code= request.form.get("code")
        starting_bal= float(request.form.get("starting_bal"))
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("INSERT INTO cash_accounts (name, code, actual_balance) VALUES (%s,%s,%s);",(name,code,starting_bal))
        conn.commit()
        return redirect(url_for("view_cash_accounts"))
    return render_template("add-cash-accounts.html")

@app.route("/edit-bank-and-cash-accounts/<string:type>/<string:id>", methods=['GET','POST'])
def edit_bank_and_cash_accounts(type,id):
    if request.method=='POST':
        conn = mysql.connect()
        cursor =conn.cursor()
        name= request.form.get("name")
        code= request.form.get("code")
        conn = mysql.connect()
        cursor =conn.cursor()
        if type=="bank":
            cursor.execute("UPDATE bank_accounts SET name=%s, code=%s WHERE id=%s;",(name,code,id))
            conn.commit()
            return redirect(url_for("view_bank_accounts"))
        elif type=="cash":
            cursor.execute("UPDATE cash_accounts SET name=%s, code=%s WHERE id=%s;",(name,code,id))
            conn.commit()
            return redirect(url_for("view_cash_accounts"))
    conn = mysql.connect()
    cursor = conn.cursor()      
    if type=="bank":  
        cursor.execute("Select * from bank_accounts where id=%s",(id))   
    elif type=="cash":  
        cursor.execute("Select * from cash_accounts where id=%s",(id))   
    data = cursor.fetchone()
    return render_template("edit-bank-and-cash-accounts.html",data=data,type=type)

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
        cursor.execute("Delete from bank_accounts where id=%s",(id))    
        conn.commit()
        return redirect(url_for("view_bank_accounts"))
    elif type =="cash_accounts":
        cursor.execute("Delete from cash_accounts where id=%s",(id))    
        conn.commit()
        return redirect(url_for("view_cash_accounts"))

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

@app.route("/generate-supplier/<int:id>")
def generate_supplier(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from suppliers where id=%s;",(id))
    supplier = cursor.fetchone()
    return render_template("generate-supplier.html", supplier= supplier)

@app.route("/generate-receipt/<int:id>")
def generate_receipt(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from inoutreceipts where id=%s;",(id))
    receipt = cursor.fetchone()
    return render_template("generate-receipt.html", receipt= receipt)

@app.route("/generate-payment/<int:id>")
def generate_payment(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from payments where id=%s;",(id))
    payment = cursor.fetchone()
    return render_template("generate-payment.html", payment=payment)

@app.route("/generate-rx-invoice/<int:id>")
def generate_rx_invoice(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_invoices where id=%s;",(id))
    rx_invoices = cursor.fetchone()
    return render_template("generate-rx-invoice.html", rx_invoices= rx_invoices)

@app.route("/generate-customer/<int:id>")
def generate_customer(id):
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from customers where id=%s;",(id))
    customer = cursor.fetchone()
    return render_template("generate-customer.html", customer= customer)

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
        # if request.form.get("desc"):
        #     description = request.form.get("desc")
        # else:
        #     description = None
        description = None
        lense_type = request.form.get("lense_type")
        unit_name = request.form.get("unit_name")
        purchase_price = request.form.get("purchase_price")
        sales_price = request.form.get("sales_price")
        # qty = request.form.get("qty")
        qty = None
        # service_cost = request.form.get("service_cost")
        service_cost = None
        # total_cost = request.form.get("total_cost") 
        total_cost = None
        if not lense_type and not unit_name and not purchase_price and not sales_price and not qty and not service_cost and not total_cost:
            return "Oops! Something is missing"      
        cursor.execute("INSERT INTO rx_items (item_code, lense_type, unit_name, purchase_price, sales_price, qty, service_cost, description, total_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",(item_code,lense_type ,unit_name, purchase_price, sales_price, qty, service_cost, description, total_cost))
        conn.commit()
        return redirect(url_for("add_rx_item"))
    return render_template("add-rx-item.html")

@app.route("/edit-rx-inventory/<string:id>", methods=['GET','POST'])
def edit_rx_inventory(id):
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
        lense_type = request.form.get("lense_type")
        unit_name = request.form.get("unit_name")
        purchase_price = request.form.get("purchase_price")
        sales_price = request.form.get("sales_price")
        qty = request.form.get("qty")
        service_cost = request.form.get("service_cost")
        total_cost = request.form.get("total_cost") 
        if not lense_type and not unit_name and not purchase_price and not sales_price and not qty and not service_cost and not total_cost:
            return "Oops! Something is missing"   
        cursor.execute("UPDATE rx_items SET item_code=%s,lense_type=%s,unit_name=%s,purchase_price=%s,sales_price=%s,qty=%s,service_cost=%s,description=%s,total_cost=%s WHERE id=%s; ",(item_code,lense_type ,unit_name, purchase_price, sales_price, qty, service_cost, description, total_cost,id))
        conn.commit()
        return redirect(url_for("view_rx_inventory"))
    conn = mysql.connect()
    cursor =conn.cursor()
    
    cursor.execute("SELECT * from rx_items where id=%s",(id))
    data = cursor.fetchone()
    return render_template("edit-rx-item.html",data=data)


@app.route("/fetch-billing-address",methods=["POST"])
def fetch_billing_address():
    customer_id = request.form.get("customer_id")
    print("customerid is: ",customer_id)
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT address from customers where id=%s",(customer_id))
    billing_address = cursor.fetchone()
    return str(billing_address)

@app.route("/fetch-order",methods=["POST"])
def fetch_order():
    order_id = request.form.get("order_id")
    print("order_id is: ",order_id)
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT * from rx_orders where id=%s",(order_id))
    data = cursor.fetchone()
    print(data)
    return str(data)


@app.route("/fetch-item-price",methods=["POST"])
def fetch_item_price():
    item_id = request.form.get("item_id")
    print("item_id is: ",item_id)
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute("SELECT purchase_price,sales_price from rx_items where id=%s",(item_id))
    data = cursor.fetchone()
    resp = [data[0],data[1]]
    print(resp)
    # print("data is: ",data[0])
    return str(resp)

@app.route("/update-rxorder-status/<string:id>/<string:status>")
def update_rxorder_status(id,status):
    try:
        conn = mysql.connect()
        cursor =conn.cursor()
        cursor.execute("UPDATE rx_orders SET status=%s WHERE id=%s; ",(status,id))
        conn.commit()
        return redirect(url_for("view_rx_orders"))
    except Exception as e:
        return str(e)

@app.route("/copy-rxorder-to/<string:type>/<string:order_id>")
def copy_rxorder_to_sales_purchase_invoice(type,order_id):
    try:
        if type == "purchaseinvoice":
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT * from suppliers;")
            suppliers = cursor.fetchall()
            cursor.execute("SELECT * from rx_items;")
            rx_items = cursor.fetchall()
            cursor.execute("SELECT * from rx_orders where id=%s;",(order_id))
            rx_orders = cursor.fetchone()
            return render_template("make-rx-purchase.html",suppliers=suppliers,rx_items=rx_items,rx_orders=rx_orders,copy=True)
        elif type == "salesinvoice":
            conn = mysql.connect()
            cursor =conn.cursor()
            cursor.execute("SELECT * from customers;")
            customers = cursor.fetchall()
            cursor.execute("SELECT * from rx_items;")
            rx_items = cursor.fetchall()
            cursor.execute("SELECT * from rx_orders where id=%s;",(order_id))
            rx_orders = cursor.fetchone()
            return render_template("make-rx-invoice.html",customers=customers,rx_items=rx_items,rx_orders=rx_orders,copy=True)
    except Exception as e:
        return str(e)





if __name__ == '__main__':
    app.run(debug=True)