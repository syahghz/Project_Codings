from flask import *
from persistence import  *
from tkinter import *
import webbrowser
import tkinter as tk
from tkinter import messagebox
import time
import shelve
import functools
from werkzeug import *
from werkzeug.utils import secure_filename
import os
import jinja2
import sys


app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'




app=Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)



# def answer():
#     showerror("Answer", "Sorry, no answer available")
#
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#         showwarning('Yes', 'Not yet implemented')
#     else:
#         showinfo('No', 'Quit has been cancelled')
#
# Button(text='Quit', command=callback).pack(fill=X)
# Button(text='Answer', command=answer).pack(fill=X)
# mainloop()



# root= tk.Tk() # create window
# canvas1 = tk.Canvas(root, width = 800, height = 350)
# canvas1.pack()
#
# @app.route("/")
# def remind():
#     def Exercise():
#         MsgBox = tk.messagebox.askquestion ('Yes or No?','Have you excerise today?')
#         if MsgBox == 'yes':
#             root.destroy()
#             return render_template("plain.html")
#         else:
#             tk.messagebox.showinfo('Return','We will check on you again in 10 minutes time')
#     button1 = tk.Button (root, text='Exit Application',command=Exercise)
#     canvas1.create_window(97, 270, window=button1)
#     Exercise()
#     root.mainloop()
#     return render_template("plain.html")
#
#
# def timer():
#
#     #run = raw_input("Start? > ")
#     mins = 0
#     # Only run if the user types in "start"
#     #if run == "start":
#     # Loop until we reach 20 minutes running
#     while mins != 10:
#         #print ">>>>>>>>>>>>>>>>>>>>>", mins
#         # Sleep for a minute
#         time.sleep(60)
#         # Increment the minute total
#         mins += 1
#         # Bring up the dialog box here
#     if mins==10:
#         remind()
#
#food=persistence.Store


from tkinter import *

def helloCallBack():
    return render_template("delivery.html")
#
# def page1():
#     page2text.pack_forget()
#     page1text.pack()
#
# def page2():
#     page1text.pack_forget()
#     page2text.pack()
#
# page1text=
# page2text=


# urlforprofile= redirect(url_for('profile'))
# def openweb():
#
@app.route("/delivery")

def remind():

    window= Tk()
    window.title("Have you?")
    window.configure(background="white")
    window.attributes('-topmost',True)
    pp=get_allinfos()
    Label(window , bg="white").grid(row=0,column=0)
    Label(window , text="Have you exercise",bg="white",fg="black",font="none 40 bold").grid(row=1, column=0,sticky=N)
    Button(window,text="No",width=6, command=window.destroy ).grid(row=3,column=0,sticky=W)
    Button(window,text="Yes",width=6 ,command=buttonClick()).grid(row=3,column=0,sticky=E)
    Button(window,text="Yes",width=6 ,command=lambda aurl="http://127.0.0.1:5000/l":OpenUrl(aurl)).grid(row=3,column=0,sticky=E)

    window.mainloop()
    return render_template("profile.html")

def buttonClick():
    webbrowser.open_new(r"http://127.0.0.1:5000/l")
def OpenUrl(url):
    webbrowser.open_new(url)




@app.route("/l")
def aboutitem():
    print('*****************111.....')
    if 'id' in session:
        print('*****************111-0.....')
        item = get_itemallinfos()

        return render_template('delivery.html', item=item)
    else:
        print('*****************111-1.....')
        return render_template('login.html')
    # item=Store.fooddetail
    # foodname=Store.foodname
    # #return render_template("aboutitem.html" , aboutitem=food)
    # return render_template("aboutitem.html",item=item,foodname=foodname)

@app.route('/<string:id>/deleteitemadmin', methods=('GET', 'POST'))
def deleteitem(id):
    delete_itemadmin(id)
    item = get_itemallinfos()
    return render_template('admindelivery.html', item=item)



# @app.route("/deletedata")
# def deletedata():
#     dict=IteminStore
#     dict.clear()
#     return render_template("plain.html")




@app.route("/plain")
def plain():
    return render_template("plain.html")

@app.route("/showitemdetail/<id>")
def show_item(id):
    item = get_itemallinfo(id)
    num={}
    data =[]
    for i in range(1,int(IteminStore[id].quantity)+1):

        num["quantity"]=i
        data.append(dict(num))
    return render_template("itemdetail.html",item = item ,data=data)

# @app.route("/cart")
# def shopping_cart():
#     if "cart" not in session:
#         flash("There is nothing in your cart.")
#         return render_template("cart.html", display_cart = {}, total = 0)
#     else:
#         items = session["cart"]
#         dict_of_melons = {}
#
#         total_price = 0
#         for item in items:
#             melon = get_itemallinfo(item)
#             total_price += float(melon.price)
#             if melon.id in dict_of_melons:
#                 dict_of_melons[melon.id]["qty"] += 1
#             else:
#                 dict_of_melons[melon.id] = {"qty":1, "name": melon.name, "price":melon.price}
#
#         return render_template("cart.html", display_cart = dict_of_melons, total = total_price )

@app.route("/cart")
def shopping_cart():
    cheat=True
    if cheat==True:
        listofitem=give_ACart()
        dictCart=give_ACartDict()
        total_calories=0
        total_price=0
        for i in dictCart:
            item=dictCart[i]

            total_price += float(item.price)
            total_calories+=float(item.calories)


        return render_template("cart.html",display_cart=listofitem,total=total_price,calories=total_calories)


    if "cart" not in session:
        flash("There is nothing in your cart.")
        return render_template("cart.html", display_cart = {}, total = 0)
    else:
        items = session["cart"]
        dict_of_melons = []
        total_calories=0
        total_price = 0
        print(items)
        for item in items:
            melon = get_itemallinfo(item)
            total_price += float(melon.price)
            total_calories+=float(melon.calories)
            dict_of_melons.append(melon)

            # if melon.id in dict_of_melons:
            #     dict_of_melons[melon.id]["qty"] += 1
            # else:
            #     dict_of_melons[melon.id] = {"qty":1, "name": melon.name, "price":melon.price}

        return render_template("cart.html", display_cart = dict_of_melons, total = total_price ,calories=total_calories)

@app.route("/add_to_cart/<id>", methods=('GET', 'POST'))
def add_to_cart(id):
    print("test0")
    if request.method == 'POST':
        quantity = request.form['quantity']
        storeintocart(id,quantity)
        print("test1")
        return redirect("/cart")

    print("test2")
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)


    flash("Successfully added to cart!")
    return redirect("/cart")

@app.route('/<string:id>/deletecartitem', methods=('GET', 'POST'))
def deletecart(id):
    delete_itemcart(id)
    posts = give_ACart()
    return render_template('cart.html', posts=posts)

@app.route('/cart/<string:id>/removecart', methods=('GET', 'POST'))
def delete_cart(id):
    if request.method == 'POST':
        session["cart"].remove(id)
    return redirect('/cart')



@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/creditcard" , methods=('GET', 'POST'))
def creditcard():
    if request.method == 'POST':
        cardname = request.form['cardname']
        cardnumber = request.form['cardnumber']
        expiry = request.form['expiry']
        scode = request.form['scode']
        error = None
        if cardname.isalpha()==False:
            error = 'Must be letters'
        else:
            if len(cardnumber)!=16:
                error = 'It must only contain 16 digits. '
            elif cardnumber.isdigit()==False:
                error = 'It must contain only digits.'
            else:
                if len(scode)<3 or len(scode)>4:
                    error= 'Please enter a valid security code'
                else:
                    if error is not None:

                        flash(error)
                    else:
                        return redirect(url_for('aboutitem'))
    return render_template("creditcard.html")

@app.route("/address" ,methods=('GET', 'POST'))
def afterpayment():
    if request.method == 'POST':
        contactnumber = request.form['contactnumber']
        add = request.form['add']
        error = None
        if not contactnumber:
            error = 'contactnumber is required.'

        elif not add:
            error = 'Address is required'

        else:
            if len(contactnumber)!= 8:
                error='Please enter a valid contact number'
                flash(error)
            else:
                return redirect(url_for('payment'))

    return render_template("afterpay.html")

@app.route("/allitem")
def allitem():
    # melon = get_itemallinfo(id)
    if 'id' in session:
        item = get_itemallinfos()
        return render_template('allitem.html', item=item )
    # ,display_melon = melon
    else:
        return render_template('login.html')



#UPLOAD_FOLDER = '/static/images'
UPLOAD_FOLDER = '\\static\\images'
# UPLOAD_FOLDER = os.path.basename('images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           # filename.rsplit('.', 1)[1].lower()





# admin for delivery

@app.route("/adminl")
def adminaboutitem():
    if 'id' in session:
        item = get_itemallinfos()

        return render_template('admindelivery.html', item=item)
    else:
        return render_template('login.html')

@app.route("/createitem",methods=('GET', 'POST'))
def createitem():
    if request.method == 'POST':
        type=request.form.get('comp_select')
        name = request.form['name']
        price = request.form['price']
        calories = request.form['calories']
        ingredient = request.form['ingredient']
        quantity = request.form['quantity']
        # file = request.files['picitem']

        if 'picitem' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['picitem']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))
            #filepic=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(os.path.abspath('static'), 'images', filename))
            # return redirect('/l')
            # return redirect(url_for('createitem',filename=filepic))
            Storing( file.filename , type, name, price, calories,ingredient,quantity)

            return redirect(url_for('aboutitem',filename=file.filename))
    return render_template("createitem.html",data=[{'type':'Main dish'}, {'type':'Soup'}, {'type':'Dessert'}, {'type':'Drink'}])




@app.route('/<string:id>/updateitem', methods=('GET', 'POST'))
def updateitem(id):
    post = get_itemallinfo(id)

    if request.method == 'POST':

        name = request.form['name']
        price = request.form['price']
        calories = request.form['calories']
        ingredient = request.form['ingredient']
        quantity = request.form["quantity"]
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            post.name = name

            post.price = price
            post.calories = calories
            post.ingredient = ingredient
            post.quantity= quantity
            update_iteminfo(post)
            return redirect(url_for('aboutitem'))

    return render_template('updateitem.html', post=post)
    # pic = request.files["picitem"]
    # fpic = 'images/'+str(secure_filename(pic.filename))
    # kkk = os.path.join(app.config['UPLOAD_FOLDER'], pic.filename)
    # pic.save(kkk)
    # pic.save(secure_filename(pic.filename))

    # file = request.files['file']
    # extension = os.path.splitext(file.filename)[1]
    # f_name = str(uuid.uuid4()) + extension
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))






@app.route("/profile")
def profile():
    # username = request.form['username']
    # password = request.form['password']
    # user = get_user(username, password)
    # session['id'] = user.get_id()
    # session['user_name'] = user.get_username()
    post=editprofile
    pp=get_allinfos()
    return render_template("profile.html",post=post,pp=pp)

@app.route("/editprofile",methods=('GET', 'POST'))
def editprofile():
    if request.method == 'POST':
        gender = request.form.get('comp_select')
        goal = request.form['goal']
        achievement=request.form['achievement']
        address = request.form['address']
        # if 'picitem' not in request.files:
        #     flash('No file part')
        #     return redirect(request.url)
        #
        # file = request.files['picitem']
        # # if user does not select file, browser also
        # # submit a empty part without filename
        # if file.filename == '':
        #     flash('No selected file')
        #     return redirect(request.url)
        #
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     flash('file {} saved'.format(file.filename))
        #     #filepic=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     file.save(os.path.join(os.path.abspath('static'), 'images', filename))
        #     # return redirect('/l')
        #     # return redirect(url_for('createitem',filename=filepic))
        adduserinfo( gender,goal,achievement,address )
        return redirect(url_for('profile'))
    return render_template("editprofile.html",data=[{'gender':'Unknown'}, {'gender':'Male'}, {'gender':'Female'}])


@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post =get_allinfo(id)
    if request.method == 'POST':
        gender = request.form.get('comp_select')
        goal = request.form['goal']
        achievement=request.form['achievement']
        address = request.form['address']
        error = None

        # if not :
        #     error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            adduserinfo(gender,goal,achievement,address)
            return redirect(url_for('profile'))

    return render_template("editprofile.html",data=[{'gender':'Unknown'}, {'gender':'Male'}, {'gender':'Female'}],post=post)

# @app.route('/goal', methods=('GET', 'POST'))
# def register():
#     if request.method == 'POST':
#         usergoal = request.form['usergoal']
#
#         create_user(username, password)
#         return redirect(url_for('profile'))
#
#     return render_template('goaladd.html')


# def contact():
#     if request.method == 'POST':
#         if request.form['submit_button'] == 'Do Something':
#             pass # do something
#         elif request.form['submit_button'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('allitem.html.html')

# @app.route("/cart")
# def cart():
#     cart=get_cartallinfo(id)
#     return render_template("cart.html",cart=cart)
#
# @app.route("/addtocart")
# def addtocart():
#     Cart(IteminStore(id))
#     return redirect(url_for('cart'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))



















#Nicole's code
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

@app.route('/init')
def init():
    init_db()
    return 'db initialised'

@app.route('/')
def index():
    if 'id' in session:
        posts = get_blogs()
        return render_template('profile.html', posts = posts)
    else:
        return render_template('login.html')


@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                return redirect(url_for('profile'))
        flash(error)
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')

# @app.route('/<string:id>/update', methods=('GET', 'POST'))
# def update(id):
#     post = get_blog(id)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         body = request.form['body']
#         error = None
#
#         if not title:
#             error = 'Title is required.'
#
#         if error is not None:
#             flash(error)
#         else:
#             post.title = title
#             post.body = body
#             update_blog(post)
#             return redirect(url_for('index'))
#
#     return render_template('update.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            create_blog(session['user_name'], title, body)
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route("/buy")
def finish():
    reduce()
    item = get_itemallinfos()
    return redirect(url_for('aboutitem' ,item=item) )


if __name__=="__main__":
    app.run(debug=True )
