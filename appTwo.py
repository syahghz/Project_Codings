from flask import*
import tkinter as tk
from tkinter import ttk


appTwo = Flask(__name__)


@appTwo.route('/')
def index():

    return render_template('Beginner.html')

# @appTwo.route('/popupmsg')
# def popupmsg(msg):
#
#   popup = tk.Tk()
#   popup.wm_title('!')
#   label = ttk.Label(popup, text=msg, font = NORM_FONT)
#   label.pack(side='top', fill='x',pady='10')
#   B1 = tkk.Button(popup, text='Okay', command = popup.destroy)
#   B1.pack()
#   popup.mainloop()
#
#   return render_template('Beginner.html', popupmsg=popupmsg)


# @appTwo.route('/')
# def window(enter):
#
#     if enter >=25:
#         print('You are overweight')
#     elif enter <=18.5:
#         print()


@appTwo.route('/nextPlease')
def nextplease():
    print('Next yesss')
    return render_template('InputH.html')

if __name__ == '__main__':
    appTwo.run()
