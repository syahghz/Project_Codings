from flask import Flask, render_template, request, flash, url_for, redirect, session
from persistence4 import *
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'

UPLOAD_FOLDER = '\\static\\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/recipes")
def recipe():
    items = get_datas()
    return render_template('RecipeAll.html', posts=items)


@app.route("/", methods=("GET", "POST"))
def create():
    session['user_name'] = 'pop'
    username = session['user_name']
    if request.method == "POST":
        print('000')
        dishName = request.form['dishName']
        ingredients = request.form['ingredients']
        nutrition = request.form['nutrition']
        instructions = request.form['instructions']

        if 'file' not in request.files:
            flash('Invalid file')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))

            file.save(os.path.join(os.path.abspath('static'), 'images', filename))

            storeData(username, dishName, ingredients, nutrition, instructions, file.filename)
            return redirect(url_for('recipe', filename=file.filename))

        return render_template("CreateBlog.html", dn=dishName, ind=ingredients, nu=nutrition, ins=instructions,
                               file=file)

    return render_template('CreateBlog.html')


@app.route('/<string:id>/update', methods=('GET', 'POST'))
def update(id):
    post = get_data(id)
    print("test-231")
    username = session['user_name']
    if request.method == 'POST':
        print("123321")
        dishName = request.form['dishName']
        ingredients = request.form['ingredients']
        nutrition = request.form['nutrition']
        instructions = request.form['instructions']

        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            flash('file {} saved'.format(file.filename))

            file.save(os.path.join(os.path.abspath('static'), 'images', filename))

            updateData(id, username, dishName, ingredients, nutrition, instructions, file.filename)
            return redirect(url_for('recipe', filename=file.filename))

    return render_template('updateblog.html', post=post)


@app.route('/<string:id>/delete', methods=('GET', 'POST'))
def delete(id):
    delete_data(id)
    post = get_data(id)
    return redirect(url_for('recipe'))

@app.route('/<string:id>/view', methods=('GET', 'POST'))
def indiRecipe(id):
    post = get_data(id)
    return render_template('Recipe.html', post=post)


if __name__ == '__main__':
    app.run(debug = True)

