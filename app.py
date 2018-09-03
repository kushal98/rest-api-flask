from flask import Flask , jsonify

app = Flask(__name__)

stores=[
    {
        'name' : 'My store',
        'item':[
            {
                'name' : 'first item',
                'price': 10.09
            }
        ]
    }
]

#POST /store 
@app.route('/',methods=['POST'])
def create_store():
    pass
#GET /store
@app.route('/store',methods=['GET'])
def get_stores():
    return jsonify({'stores':stores})

#GET /store/<string:name>
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    pass
#POST /store/<string :name>/item {name:,price:}
@app.route('/store/<string:name>/item')
def add_item_in_store(name):
    pass
#GET /store/<string : name>/item
@app.route('/store/<string:name>/item')
def get_item_from_store(name):
    pass
app.run(port=5000)