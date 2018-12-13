from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=("GET", "POST"))
def testing():
    if request.method == "POST":
        dish_name = request.form['DishName']
        ingredient = request.form['Ingredients']
        nutrition = request.form['Nutrition']
        direction = request.form['Directions']
        return render_template('Recipe.html', dn=dish_name, ind=ingredient, nu=nutrition, dir=direction)

    return render_template('CreateBlog.html')


if __name__ == '__main__':
    app.run()
