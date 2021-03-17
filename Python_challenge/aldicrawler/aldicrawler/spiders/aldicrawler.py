import scrapy

class AldiSpider(scrapy.Spider):    
    name = "aldicrawler"
    
    start_urls = [
        'https://www.aldi.com.au/en/groceries/super-savers/',
        'https://www.aldi.com.au/en/groceries/fresh-produce/',
        'https://www.aldi.com.au/en/groceries/baby/nappies-and-wipes/',
        'https://www.aldi.com.au/en/groceries/baby/baby-food/',
        'https://www.aldi.com.au/en/groceries/beauty/',
        'https://www.aldi.com.au/en/groceries/freezer/',
        'https://www.aldi.com.au/en/groceries/health/',
        'https://www.aldi.com.au/en/groceries/laundry-household/household/',
        'https://www.aldi.com.au/en/groceries/laundry-household/laundry/',
        'https://www.aldi.com.au/en/groceries/liquor/wine/',
        'https://www.aldi.com.au/en/groceries/liquor/beer-cider/',
        'https://www.aldi.com.au/en/groceries/liquor/champagne-sparkling/',
        'https://www.aldi.com.au/en/groceries/liquor/spirits/',
        'https://www.aldi.com.au/en/groceries/pantry/gluten-free/',
        'https://www.aldi.com.au/en/groceries/pantry/olive-oil/',
        'https://www.aldi.com.au/en/groceries/pantry/just-organic/',
        'https://www.aldi.com.au/en/groceries/pantry/chocolate/'
    ]
    
    def parse(self, response):
        for box in response.xpath('//a[@title="to product detail"]//div[@class="box m-text-image"]').getall():
            sel = scrapy.Selector(text=box)
            # Get Product image
            product_image = sel.xpath('//img/@src').get()
            # Get Product Title
            product_title = sel.xpath('//div[@class="box--description--header"]/text()').get().strip()
            # Get Package size
            package_size = sel.xpath('//span[@class="box--amount"]/text()').get()
            # Calculate price
            front = sel.xpath('//span[@class="box--value"]/text()').get()
            back = sel.xpath('//span[@class="box--decimal"]/text()').get()
            if front is None and back is None:
                price = ''
            else:
                price = front + 'c' if back is None else front + back
            # Get Price Per Unit
            price_per_unit = sel.xpath('//span[@class="box--baseprice"]/text()').get()
            yield {
                'Product_title': product_title,
                'Product_image': product_image,
                'Packsize': package_size,
                'Price': price,
                'Price per unit': price_per_unit
            }


