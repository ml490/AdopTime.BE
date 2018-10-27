from flask import Flask
from animalManager import AnimalManager

app = Flask(__name__)

@app.route('/animals', methods=['GET', 'POST'])
def index():
    return 'INDEX'

if __name__ == '__main__':
    app.run()





