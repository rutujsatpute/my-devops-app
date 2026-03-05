from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is the message users will see in their browser
    return "<h1>DevOps Project v1.0</h1><p>The application is running successfully!</p>"

if __name__ == '__main__':
    # We run the app on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)