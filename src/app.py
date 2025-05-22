from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Lootbox App!"

@app.route('/api/data')
def get_data():
    return {"message": "This is your data!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)