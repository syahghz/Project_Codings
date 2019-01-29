from persistenceOne import *
from persistenceS import *
from persistence import *
from persistence4 import *
from flask import *
from tkinter import *
import webbrowser
from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
import math
from datetime import *
import datetime

app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


app=Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)

def helloCallBack():
    return render_template("delivery.html")

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

@app.route('/<string:id>/deleteitemadmin', methods=('GET', 'POST'))
def deleteitem(id):
    delete_itemadmin(id)
    item = get_itemallinfos()
    return render_template('admindelivery.html', item=item)

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




UPLOAD_FOLDER = '\\static\\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

        if 'picitem' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['picitem']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))
            file.save(os.path.join(os.path.abspath('static'), 'images', filename))
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

@app.route("/profile")
def profile():
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


@app.route("/buy")
def finish():
    reduce()
    item = get_itemallinfos()
    return redirect(url_for('aboutitem' ,item=item) )


# NICOLE

@app.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        elif not email:
            error = 'Email is required'
        else:
            user = get_user(username, password, email)
            if user is None:
                error = 'Wrong username and password and email'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                session['password'] = user.get_password()
                session['email'] = user.get_email()
                # session['type']=user.get_type()
                return'Success! Welcome! :)'
            return redirect(url_for('profile'))
        flash(error)
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        print('username: '+username+"!")
        password = request.form['password']
        print('password: ' + password + "!")

        #email = request.form['email']
        email = request.form.get('email', 'az@a.com')

        print('email: ' + email + "!")
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        elif not email:
            error ='Email is required'
        else:
            create_user(username, password, email)
            return redirect(url_for('login'))
        flash(error)
    return render_template('register.html')


# nicole 3

@app.route('/BMI', methods=('GET', 'POST'))
def firstInput():

    if request.method == 'POST':
        w = request.form['weight']
        h = request.form['height']

        session["bmi"] = str(float(w)/(float(h)*float(h)))

        return redirect(url_for('nextplease'))

    return render_template('Input.html',)


@app.route('/nextPlease', methods=('GET', 'POST'))
def nextplease():
    print('Next yesss')

    bmiFloat = float(session["bmi"])
    resulttext = ''
    textFileToRead = ''




    if bmiFloat <= 18.5:

        textFileToRead = "advice_underweight"

    elif 18.5 <= bmiFloat <= 24.9:

        textFileToRead = "advice_normalweight"

    elif 25<= bmiFloat <= 29.9:

        textFileToRead = 'advice_overweight.txt'

    elif bmiFloat >= 30:

        textFileToRead = 'advice_obese'

    else:
        print('Try again')


    advice_file = open(textFileToRead, 'r')

    advice = []
    advice_file = open(textFileToRead, 'r')
    for line in advice_file:
        # in python 2
        # print line
        # in python 3

        advice.append(line)
    advice_file.close()

    return render_template('InputH.html', resulttext=advice , bmiFloat=bmiFloat )

@app.route("/123123123")
def beginner():
    return render_template("Beginner.html")

@app.route('/BlackPanther')
def video():
    return render_template('Video.html')

@app.route('/heyo', methods=['GET','POST'])
def percentage():

    if request.method['POST']:
       weight = request.form['weight']
       height = request.form['height']
       wa = request.form['waist']
       neck = request.form['neck']
       hip = request.form ['hip']

       session['bp'] =float(495/(1.29579-(0.35004*math.log10(wa+hip-neck))+(0.22100*math.log10(height))) - 450)

       return redirect(url_for('letmego'))

    return render_template('Body Percentage.html')

@app.route('/EXO')
def letmego():
    print('fighting')
    body = session['bp']

    return render_template('Bodyresult.html', body=body)

# Li qi

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/recipes")
def recipe():
    print('recipe-0')
    items = get_datas()
    print('recipe-1::size('+str(len(items))+')!!!')

    return render_template('RecipeAll.html', posts=items)

@app.route("/CreateBlog", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        print('000')
        dishName = request.form['dishName']
        ingredients = request.form['ingredients']
        nutrition = request.form['nutrition']
        instructions = request.form['instructions']

        print('111AA')
        if 'file' not in request.files:
            print('222')
            flash('Invalid file')
            return redirect(request.url)

        print('111BB')
        file = request.files['file']

        if file.filename == '':
            print('333')
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            print('444')
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))

            file.save(os.path.join(os.path.abspath('static'), 'images', filename))

            storeData(dishName, ingredients, nutrition, instructions, file.filename)
            return redirect(url_for('recipe', filename=file.filename))

        print('555')
        return render_template("CreateBlog.html", dn=dishName, ind=ingredients, nu=nutrition, ins=instructions,
                               file=file)

    print('666')
    return render_template('CreateBlog.html')


# Syahiirah

@app.route('/TrackProg', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
            exer = request.form['exer']
            hours = request.form['hours']
            mins = request.form['mins']
            id = str(uuid.uuid4())
            dt = datetime.datetime.now()
            date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")
            error = None
            currentUsername = 'xuxi' #'vera'
            storeBook(id, currentUsername, date, exer, hours, mins)

            tester = displaybook(currentUsername)
            user_reward = calc_reward(exer, hours, mins, currentUsername)
            if path.exists('point_File' + currentUsername + '.txt'):
                print('bacefile')
                point_File = open('point_File' + currentUsername + '.txt', 'r')
                prevpoints = point_File.read()
                num = float(prevpoints)
                point_File.close()
                points = int(num)
                # if points >= 50:
                #     ncode = gen_num(date, currentUsername)
                #     print(ncode, "passed through PS")
                #
                #     if ncode[0] == currentUsername:
                #             print(ncode[0], 'usernow')
                #             Rcode = ncode[-2]
                #             print(Rcode, 'the code')
                # #
                #     point_File = open('point_File' + currentUsername + '.txt', 'w')
                #     aftpoints = points - 50
                #     leftpoints = point_File.write("{}".format(aftpoints))
                #     print(leftpoints)
                #     point_File.close()
                return render_template('TrackProg.html', tester=tester, points=points)
                # else:
                #     print('tkde')
                #     return render_template('TrackProg.html', tester=tester, points= 0)
            else:
                return render_template('TrackProg.html', tester=tester, points=0)


    else:
        currentUsername = 'xuxi'
        tester = displaybook(currentUsername)
        if path.exists('point_File' + currentUsername + '.txt'):
            point_File = open('point_File' + currentUsername + '.txt', 'r')
            prevpoints = point_File.read()
            num = float(prevpoints)
            point_File.close()
            points = int(num)
            print(points, 'in else')
            return render_template('TrackProg.html', tester=tester, points=points)
        else:
            points = 0
            print('tkde file utk bace')
            return render_template('TrackProg.html', tester=tester, points=points)

    return render_template('TrackProg.html', tester=tester)

@app.route('/voucher')
def voucher():
    vlist = []
    currentUsername = 'xuxi'
    id = str(uuid.uuid4())
    dt = datetime.datetime.now()
    date = dt.strftime("%d") + " " + dt.strftime("%B") + " " + dt.strftime("%Y")
    # voucher_code = gen_num(id, date, currentUsername)
    # show_voucher(currentUsername, voucher_list)
    # print('moving on')
    # print(voucher_code)
    # k = list(voucher_code.keys())
    # print(k)

    if path.exists('point_File' + currentUsername + '.txt'):
        print('bacefile')
        point_File = open('point_File' + currentUsername + '.txt', 'r')
        prevpoints = point_File.read()
        num = float(prevpoints)
        point_File.close()
        points = float(num)
        if points >= 50:
                voucher_code = gen_num(id, date, currentUsername)
                print('moving on')
                print(voucher_code)
                k = list(voucher_code.keys())
                print(k)
                point_File = open('point_File' + currentUsername + '.txt', 'w')
                aftpoints = points - 50
                leftpoints = point_File.write("{}".format(aftpoints))
                print(leftpoints)
                point_File.close()
                print(aftpoints)

                return render_template('voucher.html', vlist=voucher_code, k=k)

        return render_template('voucher.html')


    return render_template('voucher.html')

@app.route('/del')
def del_list():
    val = '1'
    k = list(voucher_code.keys())
    for i in k:
        print(i)
        voucher_code.pop(i)
        print('wee')
        return render_template('payment.html')
    # print(a)
    # del voucher_code[i]

    redirect(url_for('payment'))


# nicole
@app.route('/logout')
def logout():
    voucher_code = gen_num(id, date, currentUsername)
    session.clear()
    redirect(url_for('login'))


if __name__=="__main__":
    app.run(debug=True )
