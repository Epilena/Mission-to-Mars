from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

#Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#create a root route that will query the Mongo database and pass the mars data into HTML for rendering 
@app.route("/")
def index():
    composite_data= mongo.db.composite_data.find_one()
    return render_template("index.html", mars = composite_data)

#create route function that will import you scrape mars py script and call the scrape funcion
@app.route("/scrape")
def scrape():
    composite_data= mongo.db.composite_data
    composite = scrape_mars.scrape()
    composite_data.update_one({},{"$set":composite}, upsert=True)
    return redirect("/")

if __name__ =="__main__":
    app.run(debug=True)