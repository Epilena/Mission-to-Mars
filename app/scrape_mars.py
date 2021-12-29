# %%
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    executable_path = {'executable_path' : ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # %%
    ###visit Nasa Mars News Site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # %%
    ###convert to BeautifulSoup object
    html = browser.html
    news_obj= soup(html, 'html.parser')
    stories = news_obj.select_one('div.list_text')

    # %%
    stories.find('div', class_= 'content_title')

    # %%
    title = stories.find('div', class_='content_title').get_text()
    title

    # %%
    para = stories.find('div', class_='article_teaser_body').get_text()
    para

    # %%
    ###visit JPL Mars Space Images
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # %%
    #find the image url for the current Featured Mars Image
    image_button= browser.find_by_tag('button')[1]
    image_button.click()

    # %%
    #convert HTML to BeautifulSoup object
    html = browser.html
    image_obj = soup(html, 'html.parser')

    # %%
    #find image url
    image_url = image_obj.find('img', class_='fancybox-image').get('src')
    image_url

    # %%
    #assign URL string to a variable
    featured_image_url = f'https://spaceimages-mars.com/{image_url}'
    featured_image_url

    # %%
    ##visit Mars Facts webpage use pandas to scrape the table
    Mars_df=pd.read_html('https://galaxyfacts-mars.com')[0]
    Mars_df.head()

    # %%
    #Rename columns remove index
    Mars_df.columns=['Parameter', 'Mars', 'Earth']
    Mars_df.set_index('Parameter', inplace = True)
    Mars_df

    # %%
    #use pandas to convert to HTML table string
    Mars_df=Mars_df.to_html()

    # %%
    ##Mars Hemispheres visit astrogeology site
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # %%
    #create loop to click 4 links to find image url to full resolution image
    hemi_images = []

    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css('a.product-item img')[i].click()
        pic = browser.links.find_by_text('Sample').first
        
        #Save both the image url and hemisphere title
        hemisphere['img_url'] = pic['href']
        hemisphere['title'] = browser.find_by_css('h2.title').text
        
        #Append the dictionary with the image url string and hemisphere title to the a list
        hemi_images.append(hemisphere)
        
        browser.back()

    hemi_images


    #creation of one python dictionary containing all scraped data
    composite_data = {
        "title": title,
        "paragraph": para,
        "featured_image_url": featured_image_url,
        "facts": Mars_df,
        "hemisphere_images": hemi_images
    }

    browser.quit()

    return composite_data

    # %%
