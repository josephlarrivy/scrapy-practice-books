1. Create project and install/start scrapy:
    1. Create and cd into project folder
    2. Python3 -m venv venv
    3. source venv/bin/activate
    4. pip3 install scrapy
    5. scrapy startproject projectname
    6. cd projectname
    7. scrapy shell

2. Once in scrapy shell:
    1. fetch(‘site_url’)
        1. Used to test if scrapy can access the page
    2. response
        1. Command should return ‘200 url’
    3. response.css(‘type.name’)
        1. type.name can look like the following where type is the type of css element (div, p, h1, article, etc) and name is what the developer called their element (item, product-info, price, article-title, etc)
        2. response.css(‘div.product-info’)
        3. response.css(‘article.title’)
    4. response.css(‘type+name’).get()
        1. .get() return the html code for the first item in the list
    5. name = response.css(‘type+name’)
        1. The response can be saved to a variable and then methods can be used on that variable to get nested elements within the original selection
    6. name.css(‘type.another.name’).get()
        1. This returns the entire elements
    7. name.css(‘type.another.name::text’).get()
        1. This returns only the text within the element
    8. name.css(‘type.another.name::text’).getall()
        1. This will return the text from every element that matches in a list
    9. Examples:
        1. products = response.css(‘div.product-item-info’)
        2. products.css(‘a.product-item-link::text’).get()
        3. products.css(‘a.product-item-link::text’).getall()
        4. products.css(‘a.product-item-link’).attrib[‘href’]
            1. Attributes of an elements can also be selected (this one will return the link)

3. To create a python script:
    1. Inside of spiders folder in project: create a folder
    2. See project files for rest of example

4. To run
    1. scrapy crawl spidername