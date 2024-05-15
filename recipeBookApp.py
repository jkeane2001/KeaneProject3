'''
Jack Keane
Professor Jenq
CSIT 537 Web Development
Project 3: Recipe Book App
'''
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

recipeDB = mysql.connector.connect(
    host="localhost",
    user="ChefAri",
    password="Lethercook12",
    database="recipeBook"
)

#cursor = recipeDB.cursor()

@app.route('/addRecipe', methods=['GET','POST'])
def addRecipe():
    if request.method == 'POST':
        recipeName = request.form['recipeName']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        cursor = recipeDB.cursor()
        recipe = "INSERT INTO recipes (recipeName, ingredients, instructions) VALUES (%s, %s, %s)"
        val = (recipeName, ingredients, instructions)
        cursor.execute(recipe, val)
        recipeDB.commit()

        return redirect(url_for('index'))
    return render_template('addRecipe.html')

@app.route('/deleteRecipe/<int:recipeID>', methods=['POST'])
def deleteRecipe(recipeID):
    cursor = recipeDB.cursor()
    delete_query = "DELETE FROM recipes WHERE id = %s"
    cursor.execute(delete_query, (recipeID,))
    recipeDB.commit()
    return redirect(url_for('index'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        cursor = recipeDB.cursor()
        cursor.execute("SELECT * FROM recipes")
        recipes = cursor.fetchall()
        return render_template('index.html', recipes=recipes)


#app.run(debug=True)
app.run(debug=True, port=7000)

