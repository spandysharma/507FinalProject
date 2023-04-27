from flask import Flask, render_template, request
import searchTerms

def searchOutput(results):
    '''results is a list of search results and comprises of dictionaries
    where each dictionary is a single result'''
    display = []
    for d in results:
        print("d====================",d)
        display.append(d['name'])
    return display

gameName = ""
genre = ""

app = Flask(__name__)

@app.route('/')
def index():
    global gameName
    global genre
    genre = ""
    gameName = ""
    return render_template("inputForm.html")
    # return render_template("slider.html")

@app.route('/handle_form', methods=['POST'])
def handle_the_form():
    global gameName
    global genre
    # gameName = request.form["gameName"]
    genre = request.form["genre"]
    print(genre)
    results = searchTerms.performSearchMCQ(genre)
    # display = searchOutput(results)
    # return f"hello"
    return render_template("displayList.html",data=results)


'''
    global gameName
    gameName = request.form["genre"] #CHANGED THIS
    preferences = dict()
    preferences['genre'] = gameName
    results = searchTerms.performSearchMCQ(preferences) #CHANGED THIS
    display = searchOutput(results)
'''

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
