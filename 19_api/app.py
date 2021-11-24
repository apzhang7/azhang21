import urllib
from flask import Flask
from flask import render_template
import json

app = Flask(__name__) 
@app.route('/')
def display():
    req = urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=pJkgjfYApMvTrcMw0O7hdO7Chooqu9b4jcuDu2zC')
    text = json.load(req)
    #for i in text:
        #print(json.load(r)[i])
    picture = (text['url'])
    description = (text['explanation'])
    return render_template('main.html', pic = picture, desc = description)
        


if __name__ == '__main__':
    app.debug = True
    app.run()