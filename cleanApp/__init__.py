from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '53dd5a9f27bb8b853b9789e7688ebdf5'


from cleanApp import routes