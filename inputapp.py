from flask import Flask, render_template, request
import searchTerms

def searchOutput(results):
    '''results is a list of search results and comprises of dictionaries
    where each dictionary is a single result'''
    display = []
    for d in results:
        display.append(d['name'])
    return display

gameName = ""
genre = ""
category = ""

app = Flask(__name__)

@app.route('/')
def index():
    global gameName
    global genre
    global category
    genre = ""
    gameName = ""
    category = ""
    return render_template("index.html")

@app.route('/genreMenu')
def genreMenu():
    global category
    category = "genre"
    return render_template('genre.html')

@app.route('/franchiseMenu')
def franchiseMenu():
    global category
    category = "franchise"
    return render_template('franchise.html')

@app.route('/platformMenu')
def platformMenu():
    global category
    category = "platform"
    return render_template('platform.html')

@app.route('/ratingMenu')
def ratingMenu():
    global category
    category = "rating"
    return render_template('rating.html')

@app.route('/handle_form', methods=['POST'])
def handle_the_form():
    global gameName
    global genre

    global category
    category = request.form[category]
    print(category)
    results = searchTerms.searchByCategory(category)
    return render_template("displayList.html",data=results)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
