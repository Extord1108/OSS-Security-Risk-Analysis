import re

from flask import Flask
import requests

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

@app.route('/crawl')
def crawl():
    resp = requests.get('https://replicate.npmjs.com/_all_docs')
    page_content = resp.text
    resp.close()
    file_object1=open("content.txt", mode="a", encoding="utf-8")
    file_object1.write(page_content)
    file_object1.close()

if __name__ == '__main__':
    app.run()
