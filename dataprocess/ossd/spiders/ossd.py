import scrapy
import os
import json
from ossd.items import OssdItem


class ExampleSpider(scrapy.Spider):
    name = 'ossd'
    allowed_domains = ['npmjs.com']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'example'
        self.allowed_domains = ['npmjs.com', 'godaddy.com']
        jsonlist = os.listdir('./metadata')
        for item in jsonlist:
            with open('./metadata/' + item, 'r') as f:
                print(item)
                data = json.load(f)
                for pck in data['rows']:
                    key = pck['key'].replace('%', '%25').replace('/', '%2F').replace('@', '%40').replace('+', '%2B').replace('=', '%3D').replace(
                        ' ', '%20').replace('?', '%3F').replace('&', '%26').replace('#', '%23')
                    self.start_urls.append(
                        'https://replicate.npmjs.com/' + key)

    def parse(self, res):
        item = OssdItem()
        doc = res.text.replace('¥', '\\')
        item['doc'] = doc
        yield item
