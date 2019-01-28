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
from random import *
import jinja2
import sys
from datetime import *
from tkinter import *



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
    width_of_window=460
    height_of_window=115
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    x_coordinate=(screen_width/2)-(width_of_window/2)
    y_coordinate=(screen_height/2)-(height_of_window/2)
    window.geometry("%dx%d+%d+%d" % (width_of_window,height_of_window,x_coordinate,y_coordinate))
    window.title("Have you?")
    # window.wm_iconbitmap("../static/images/logo.png")
    window.configure(background="white")
    window.attributes('-topmost',True)
    pp=get_allinfos()
    Label(window , bg="white").grid(row=0,column=0)
    Label(window , text="Have you exercise",bg="#00868B",fg="white",font="none 40 bold").grid(row=1, column=0,sticky=N)
    Button(window,text="No",width=6, command=window.destroy ,fg="white",bg="#297373" ).grid(row=3,column=0,sticky=W)
    Button(window,text="Yes",width=6 ,command=buttonClick(),fg="white",bg="#297373").grid(row=3,column=0,sticky=E)
    Button(window,text="Yes",width=6 ,command=lambda aurl="http://127.0.0.1:5000/l":OpenUrl(aurl) ,fg="white",bg="#297373").grid(row=3,column=0,sticky=E)

    window.mainloop()
    return render_template("profile.html")

def buttonClick():
    webbrowser.open_new(r"http://127.0.0.1:5000/l")
def OpenUrl(url):
    webbrowser.open_new(url)

@app.route("/l")
def aboutitem():
        item = get_itemallinfos()
        return render_template('delivery.html', item=item)


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




@app.route("/showitemdetail/<id>")
def show_item(id):
    item = get_itemallinfo(id)
    num={}
    data =[]
    for i in range(1,int(IteminStore[id].quantity)+1):

        num["quantity"]=i
        data.append(dict(num))
    return render_template("itemdetail.html",item = item ,data=data)


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
    if request.method == 'POST':
        quantity = request.form['quantity']
        storeintocart(id,quantity)
        return redirect("/cart")

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
    listofitem=give_ACart()
    dictCart=give_ACartDict()
    total_calories=0
    total_price=0
    for i in dictCart:
        item=dictCart[i]

        total_price += float(item.price)
        total_calories+=float(item.calories)
    return render_template("payment.html",display_cart=listofitem,total=total_price,calories=total_calories)

@app.route("/creditcard" , methods=('GET', 'POST'))
def creditcard():
    if request.method == 'POST':

        # cardname = request.form['cardname']
        # cardnumber = request.form['cardnumber']
        expiry = request.form['expiry']
        # scode = request.form['scode']

        # if cardname.isalpha()==False:
        #     error = 'Must be letters'
        # else:
        #     if len(cardnumber) != 16:
        #         error = 'It must only contain 16 digits.'
        #     elif cardnumber.isdigit() == False:
        #         error = 'It must contain only digits.'
        #     else:
        #         if len(scode)<3 or len(scode)>4:
        #             error= 'Please enter a valid security code'
        #         else:
        today=datetime.today()
        month=int(today.month)
        year= str(today.year)
        year=int(year[-2:])
        inputMonth= int(expiry[:2])
        inputYear= int(expiry[-2:])
        if (inputYear<year):
            error="The card has expired."
            flash( error )
        elif (inputYear>=year):
            if(inputMonth>12 or inputMonth<0):
                error="Please enter a valid month."
                flash(error)
            else:
                if(inputMonth<month):
                    error="The card has expired."
                    flash( error )
                else:
                    return redirect(url_for('finish'))
        else:
            return redirect(url_for('finish'))
    return render_template("creditcard.html")

@app.route("/address" ,methods=('GET', 'POST'))
def afterpayment():
    if request.method == 'POST':
        contactnumber = request.form['contactnumber']
        add = request.form['add']
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


@app.route("/adminpage")
def adminpage():
    if 'id' in session:
        item = get_itemallinfos()
        return render_template('adminpage.html',item=item )

    else:
        return render_template('login.html')




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
            return redirect(request.url)

        file = request.files['picitem']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
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




# @app.route("/profile/<id>")
# def profile(id):
#     if 'id' in session:
#         post=editprofile
#         pp = get_allinfos()
#         return render_template('profile.html', post=post,pp=pp)
#
#     else:
#         return render_template('login.html')

# @app.route("/editprofile",methods=('GET', 'POST'))
# def editprofile():
#     if request.method == 'POST':
#         goal = request.form['goal']
#         achievement=request.form['achievement']
#         pic=request.form['picitem']
#
#         file = request.files['picitem']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             flash('file {} saved'.format(file.filename))
#             #filepic=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             file.save(os.path.join(os.path.abspath('static'), 'images', filename))
#             # return redirect('/l')
#             # return redirect(url_for('createitem',filename=filepic))
#         adduserinfo( goal,achievement,pic)
#         return redirect(url_for('profile',id=session["id"]))
#     return render_template("editprofile.html")




#with the help of Ace
@app.route("/profile/<id>")
def profile(id):
    id=session['user_name']
    if 'id' in session:
        post=editprofile
        pp = get_allinfo(id)
        cc=userinfocall(id)
        aa=userinfocalle(id)
        bb=userinfocallp(id)
        return render_template('profile.html', post=post,pp=pp,cc=cc,aa=aa,bb=bb)

    else:
        return render_template('login.html')
    #
    # username = request.form['username']
    # password = request.form['password']
    # user = get_user(username, password)
    # session['id'] = user.get_id()
    # session['user_name'] = user.get_username()
    # post=editprofile
    # pp=get_allinfos()
    #
    # return render_template("profile.html",post=post,pp=pp)

@app.route("/editprofile",methods=('GET', 'POST'))
def editprofile():

    id=session['user_name']
    aa=userinfocall(id)
    bb=userinfocallp(id)
    cc=userinfocalle(id)

    if request.method == 'POST':

        goal = request.form['goal']
        achievement=request.form['achievement']
        try:
            file = request.files['picitem']
            if 'picitem' not in request.files:
                return redirect(request.url)
            file = request.files['picitem']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
            #filepic=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                file.save(os.path.join(os.path.abspath('static'), 'images', filename))
            # return redirect('/l')
            # return redirect(url_for('createitem',filename=filepic))
                adduserinfo(id, goal,achievement,file.filename)
                return redirect(url_for('profile',id=session["id"],filename=file.filename))
            print(file)
            print(type(file))
        except:
            # file="FileStorage: 'default.png' ('image/png')"
            file="default.png"
            adduserinfo(id, goal,achievement,file)

            return redirect(url_for('profile',id=session["id"],filename=file))
        # if user does not select file, browser also
        # submit a empty part without filename
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     #filepic=file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     file.save(os.path.join(os.path.abspath('static'), 'images', filename))
        #     # return redirect('/l')
        #     # return redirect(url_for('createitem',filename=filepic))
        #     adduserinfo(id, goal,achievement,file.filename)
        #     return redirect(url_for('profile',id=session["id"],filename=file.filename))
    return render_template("editprofile.html",aa=aa,bb=bb,cc=cc)


@app.route('/<string:id>/updateprofile', methods=('GET', 'POST'))
def updatep(id):
    pp=get_allinfos()
    id=session["user_name"]
    post =get_allinfo(id)
    if request.method == 'POST':
        goal = request.form['goal']
        achievement=request.form['achievement']
        post.goal = goal
        post.achievement = achievement
        update_userinfo(post)
        return redirect(url_for('profile'))
    return render_template("updateprofile.html",post=post,pp=pp)

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


# @app.route('/login',  methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#         error = None
#         if not username:
#             error = 'Username is required.'
#         elif not password:
#             error = 'Password is required.'
#
#         elif not email:
#             error = 'Email is required'
#         else:
#             user = get_user(username, password, email)
#             if user is None:
#                 error = 'Wrong username and password and email'
#             else:
#                 session['id'] = user.get_id()
#                 session['user_name'] = user.get_username()
#                 session['password'] = user.get_password()
#                 session['email'] = user.get_email()
#                 return redirect(url_for('profile',id=session["id"]))
#         flash(error)
#     return render_template('login.html')


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         print('username: '+username+"!")
#         password = request.form['password']
#         print('password: ' + password + "!")
#
#         #email = request.form['email']
#         email = request.form.get('email', 'az@a.com')
#
#         print('email: ' + email + "!")
#         error = None
#         if not username:
#             error = 'Username is required.'
#         elif not password:
#             error = 'Password is required.'
#
#         elif not email:
#             error ='Email is required'
#         else:
#             create_user(username, password, email)
#             return redirect(url_for('login'))
#         flash(error)
#     return render_template('register.html')

@app.route('/registeradmin', methods=('GET', 'POST'))
def adminregister():
    if request.method == 'POST':
        username = request.form['ausername']
        password = request.form['apassword']
        email= request.form['aemail']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
        else:
            create_admin(username, password, email)
            return redirect(url_for('login'))
        flash(error)
    return render_template('adminregister.html')

@app.route('/login',  methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        type=request.form.get('type')
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            if type=="User":
                user = get_user(username,password,email)
                if user is None:
                    error = 'Wrong username,password and email.'
                else:
                    session['id'] = user.get_id()
                    session['user_name'] = user.get_username()
                    session['email']=user.get_email()
                    return redirect(url_for('profile',id=session["id"]))
            elif type=="Admin":

                admin=get_admin(username,password,email)
                if admin is None:
                    error='Wrong username,password and email.'
                else:
                    session['id'] = admin.get_id()
                    session['user_name'] = admin.get_username()
                    session['email']=admin.get_email()
                    return redirect(url_for('adminaboutitem'))
        flash(error)
    return render_template('login.html', data=[{'type':'User'}, {'type':'Admin'}] )

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email= request.form['email']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
        else:
            create_user(username, password, email)
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
