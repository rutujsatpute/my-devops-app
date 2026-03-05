from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is the message users will see in their browser
    return "This app is working successfully on My laptop"

if __name__ == '__main__':
    # We run the app on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)