
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True,auto_incrementing=False)
    title = db.Column(db.String)
    image = db.Column(db.String)
    
    def __init__(self,title,image):
        
    image = db.Col
    pass
    
    
class ProductUser(db.model):
    pass

@app.route("/")
def hello_world():
    return {"status":200}

if __name__ == "__main__":
    app.run(host = '0.0.0.0')