from flask import Flask , jsonify, request

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
    request_data = request.get_json()
    new_store={
        'name':request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store
@app.route('/store',methods=['GET'])
def get_stores():
    return jsonify({'stores':stores})

#GET /store/<string:name>
@app.route('/store/<string:name>',methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' :'store not found'})


#POST /store/<string :name>/item {name:,price:}
@app.route('/store/<string:name>/item')
def add_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name':request_data['name'],
            'price':request_data['price']
            }
            stores['item'].append(new_item)
            return jsonify(new_item )
    return jsonify({'message':'store not found'})


#GET /store/<string : name>/item
@app.route('/store/<string:name>/item')
def get_item_from_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return({'message':'item not found'})
app.run(port=5000)