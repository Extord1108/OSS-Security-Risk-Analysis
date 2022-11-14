import json
import re

from flask import Flask
import requests
from flask import request
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)


@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/search')
def search_content():
    count = 0
    file_object2 = open("templates/content.txt", 'r')
    # {"id": "--hoodmane-test-pyodide", "key": "--hoodmane-test-pyodide","value": {"rev": "2-ca1f76c11cfe8727f8768fe43e76b341"}},
    obj1 = re.compile('{"id":"(?P<id>.*?)","key":"(?P<key>.*?)","value":(?P<value>.*?)}', re.S)
    page_content = file_object2.read()
    answer = obj1.finditer(page_content)
    for i in answer:
        count = count + 1

    print(count)
    return str(count)


@app.route('/find', methods=['GET', 'POST'])
def Find_com():
    # find_content = request.args.get('find_content')
    find_content = "gmail.com"
    urls = f"https://www.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={find_content}&redirected=true&tmskey=1dom_03_intlgtld"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    }
    resp = requests.get(urls, headers=headers)

    return str(resp.text)


@app.route('/crawl')
def crawl():
    resp = requests.get('https://replicate.npmjs.com/_all_docs')
    page_content = resp.text
    resp.close()
    file_object1 = open("content.txt", mode="a", encoding="utf-8")
    file_object1.write(page_content)
    file_object1.close()


if __name__ == '__main__':
    app.run()
