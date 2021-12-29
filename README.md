# Mission to Mars
## Web-Scrapping-Challenge

### Introduction
The goal of this project is full stack app devevlopment. I was able to build a web application that scrapes various websites to obtain data related to the Mission to Mars, and subsequently display acquired information in a single HTML page.  

### Data/Resources
Websites that are scraped include:
Mars News Site- https://redplanetscience.com
JPL Mars Space Images hrrps://spaceimages-mars.com
Mars Facts webpage https://galaxyfacts-mars.com
Mars Hemispheres https://marshemispheres.com/

### Methodology
A number of methods was used in order to scrape the data.  Python coding in a Jupyter notebook was utilized for main scrape coding.  BeautifulSoup, Pandas, and Splinter libraries were required to obtain data.  BeautifulSoup was utilized for data parsing.  Splinter was used to navigate site and click a 'button' to obtain an image.  Pandas was used to scrape a table, creation of a corresponding dataframe, and conversion to HTML table string. MongoDB and Flask appication were utilized to create a new HTML page to display scraped information, and Bootstrap for structuring.  

### Results/Conclusion

![mission to mars](https://user-images.githubusercontent.com/88807979/147621336-2b435d0c-9500-4a04-909f-ff57cce4c5cf.png)
