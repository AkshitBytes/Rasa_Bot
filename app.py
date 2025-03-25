from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    rasa_response = requests.post('http://localhost:5005/webhooks/rest/webhook', 
                                json={'message': user_message}).json()
    bot_message = rasa_response[0]['text'] if rasa_response else "Sorry, I didn’t get that."
    return {'response': bot_message}

if __name__ == '__main__':
    app.run(debug=True)