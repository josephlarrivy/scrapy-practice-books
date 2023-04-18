
import scrapy
import re
import time

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

            title_container_h3 = inner_container.css('h3')
            # gets the title text
            title = title_container_h3.css('a::text').get()
            anchor = title_container_h3.css('a')
            # gets the link from the anchor tag
            href = anchor.css('a::attr(href)').get()

            price_container = inner_container.css('div.product_price')
            # gets the price and removes the monetary unit
            price = price_container.css('p.price_color::text').get().replace('£', '')

            # gets the monetary unit only from price
            string = price_container.css('p.price_color::text').get()

            # gets the star-rating from the className
            star_rating = inner_container.css('p.star-rating::attr(class)').get()

            # regex that removes the value from price and retunrs only the monetary unit
            pattern = r'^.*?(£)'
            match = re.search(pattern, string)
            if match:
                monetary_unit = match.group(1)

            # regex that looks at the star-rating and retunrs onlt the number
            def extract_rating(string):
                pattern = r'^star-rating\s+(\w+)$'
                match = re.match(pattern, string)
                if match:
                    return match.group(1)
                else:
                    return 'n/a'

            # function that takes the output above and converts the string number into an integer
            def convert_string_to_number(string):
                numbers = {
                    'One': 1,
                    'Two': 2,
                    'Three': 3,
                    'Four': 4,
                    'Five': 5
                }
                return numbers.get(string, None)

            star_rating_number = convert_string_to_number(extract_rating(star_rating))

            yield {
                'price': price,
                'monetary_unit' : monetary_unit,
                'star_rating' : star_rating_number,
                'title' : title,
                'link' : href
            }

        pager = response.css('ul.pager')
        next_page_button_li = pager.css('li.next')
        next_page_link = next_page_button_li.css('a::attr(href)').get()
        next_page = f'http://books.toscrape.com/{next_page_link}'

        time.sleep(10)

        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)