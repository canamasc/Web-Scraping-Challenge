# Web-Scraping-Challenge

Uses Jupyter Notebook (Python), BeautifulSoup, Pandas, and Requests/Splinter to scrape Mars news websites, store information in MongoDB collection, then uses Flask to query the database and render a HTML page locally.

News site sources:
https://redplanetscience.com/
https://spaceimages-mars.com/
https://galaxyfacts-mars.com/
https://marshemispheres.com/

Scraping first done in jupyter notebook, then stored as a function in .py file. Flask app has two routes (/ and /scrape). /scrape is activated when "Scrape New Data" button is pressed on HTML page (index.html), and runs the scrape function to essentially refresh the data. "/" route just pulls up home page. 
Scrape functions stores found data from all sources as python dictionary in Mongo. 

