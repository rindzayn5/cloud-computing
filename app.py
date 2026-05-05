from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Bhai-Mart Backend is Live!</h1><p>Azure Deployment Successful.</p>"

if __name__ == '__main__':
    app.run()