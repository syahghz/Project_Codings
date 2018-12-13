from flask import *
from persistence import  *
import tkinter as tk
from tkinter import messagebox
import time
import shelve
import functools





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
@app.route("/delivery")
def remind():
    window= Tk()
    window.title("Have you?")
    window.configure(background="white")
    Label (window , bg="white").grid(row=0,column=0)
    Label (window , text="Have you exercise today?",bg="white",fg="black",font="none 40 bold").grid(row=1, column=0,sticky=N)
    Button (window,text="No",width=6, command=window.destroy ).grid(row=3,column=0,sticky=W)
    Button (window,text="Yes",width=6 , command=window.destroy ).grid(row=3,column=0,sticky=E)
    window.mainloop()





@app.route("/l")
def aboutitem():
    item=Store.fooddetail
    foodname=Store.foodname
    #return render_template("aboutitem.html" , aboutitem=food)
    return render_template("aboutitem.html",item=item,foodname=foodname)

@app.route("/plain")
def plain():
    return render_template("plain.html")

@app.route("/allitem")
def allitem():
    item=Store.fooddetail
    foodname=Store.foodname
    store=Store.Cart()
    return render_template("allitem.html",item=item ,foodname=foodname,store=store)


# def clicka():
#     print("hihhihihihhhhhhhhhhhhhhhhh")
#     return 1
# item=Store.fooddetail

# for food in item:
#
#
#     @app.route("/"+item[food]["name"])
#     def individualitem():
#
#         return render_template("forone.html")

# @app.route("/profile")
# def profile():
#     return render_template("profile.html")

if __name__=="__main__":
    app.run(debug=True)
