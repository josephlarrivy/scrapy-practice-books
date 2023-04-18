import scrapy

class BooksSpider(scrapy.Spider):
    name = 'booksspider'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        items = response.css('div.col-sm-8.col-md-9')

        header = items.css('div.page-header.action')
        header.css('h1::text').get()
        
        main_items_section = items.css('section')
        items = main_items_section.css('ol.row')
        
        for item in items.css('li.col-xs-6.col-sm-4.col-md-3.col-lg-3'):
            inner_container = item.css('article.product_pod')
            price_container = inner_container.css('div.product_price')
            price = price_container.css('p.price_color::text').get().replace('£', '')

            yield {
                'price': price
            }