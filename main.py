from flask import Flask, render_template
import requests
import os
import random

app = Flask(__name__)

'''Code to retrieve all pictures from img folder:'''
img_bank = (os.listdir('./static/img'))

@app.route('/')
def get_quote():
    img_rand_choice = random.choice(img_bank)
    print(img_rand_choice)

    response = requests.get('https://stoic-server.herokuapp.com/random')
    quote_data = response.json()
    
    author = quote_data[0]['author']
    body = quote_data[0]['body']
    source = quote_data[0]['quotesource']

    print(f'author:{author}\nbody:{body}\nsource:{source}')

    stoic_quote = {
        'author': author,
        'body_text': body,
        'source': source,
    }

    return render_template('index.html', quote=stoic_quote, img=f'static/img/{img_rand_choice}')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999)
    # app.run(debug=True)