from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
def scrape():
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Avoid repeating code and launching broswer multiple times 
    def scrape1(url_str):
        browser.visit(url_str)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        return soup

    # Get latest news headline and blurb
    listings = {}

    url = "https://redplanetscience.com"

    soup = scrape1(url)
    listings["headline"] = soup.find("div", class_="content_title").get_text().strip()
    listings["text"] = soup.find("div", class_="article_teaser_body").get_text().strip()

    # Get featured Mars image
    url = "https://spaceimages-mars.com/"
    soup = scrape1(url)
    relative_image_path = soup.find_all('img')[1]["src"]
    featured_image_url = url + relative_image_path

    # Galaxy facts tables
    url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url)

    df = tables[0]
    htmltable = df.to_html()
    # Hemisphere high res images
    url = "https://marshemispheres.com/"
    hemispheres = []

    soup = scrape1(url)
    sidebar = soup.find_all('div', class_='item')

    for item in sidebar:
        hemi = {}
        img_url = item.find('a')['href']
        hemi['title'] = (item.find('h3').get_text().strip())[:-9]
    
        newurl = url + img_url
        soup = scrape1(newurl)
        
        # is this correct image?
        n = soup.find_all('dd')[1]
        hemi['img_url'] = n.find('a')['href']
        
        hemispheres.append(hemi)

    # quit browser
    browser.quit()

    # Return dict
    ans = {"headline": listings,
        "featured image": featured_image_url,
        "facts table": htmltable,
        "hemisphere images": hemispheres}
    
    return ans