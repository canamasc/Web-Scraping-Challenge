from flask import Flask, render_template, redirect
import pymongo
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home(vacation=None):

    # Find one record of data from the mongo database
    redplanet_data = mongo.db.collection.find_one()
    # print(list(redplanet_data))
    # print(type(redplanet_data))
    # print(redplanet_data['hemisphere_images'])
    # Return template and data
    return render_template('index.html', vacation=redplanet_data)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)