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
