# build d9fcb26663
# (auto) 72a225
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
