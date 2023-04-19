import os
import json

class JsonParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_json_file(self):
        with open(self.filepath, 'r') as read_file:
            self.data = json.load(read_file)

    def convert_to_float(self, string_number):
        self.integer_number = float(string_number)
        return self.integer_number
    
    def average_prices(self):
        total = 0
        num_items = 0
        for item in self.data:
            price_float = self.convert_to_float(item['price'])
            total += price_float
            num_items += 1
        average_price = round(total / num_items, 2)
        monetary_unit = self.data[0]["monetary_unit"]
        print('Average book price:', monetary_unit, average_price)

    def average_star_rating(self):
        total = 0
        num_items = 0
        for item in self.data:
            stars = item["star_rating"]
            total += stars
            num_items += 1
        average_stars = round(total / num_items, 2)
        print('Average star rating:', average_stars)

    def print_data(self):
        self.get_json_file()
        self.average_prices()
        self.average_star_rating()




parsed_data = JsonParser('./books.json')
parsed_data.print_data()