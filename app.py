from flask import Flask,jsonify,request,json,abort,make_response
import json
import uuid
from models import *
from Points import *



app = Flask(__name__)

receipts_Id = {}
pointsForReceipts = {}




@app.route('/receipts/process', methods=['POST'])
def process_receipts():
	schema = CreateReceiptSchema()
	data = request.get_json()
	errors = schema.validate(data)
	if errors :
		return {"Errors" : errors} , 422
	receipt_data = schema.dump(data)
	receipt_unique_id = str(uuid.uuid4())
	receipts_Id[receipt_unique_id] = receipt_data
	pointsForReceipts [receipt_unique_id] = Calculate_points(receipt_data)
	return jsonify({"id" : receipt_unique_id}) , 201

@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def get_points(receipt_id):
	emptyvalues = ["", "''", " ", "' '", None, '""', '" "']
	if receipt_id in emptyvalues:
		abort(400)
	if receipt_id not in receipts_Id:
		abort(404)
	return jsonify({"points": pointsForReceipts[receipt_id]})

@app.errorhandler(500)
def handle_500_error(error):
	return make_response(jsonify({'error' : 'Internal Server error occcured'}), 500)


@app.errorhandler(404)
def handle_404_found(error):
	return make_response(jsonify({'error': 'Receipt ID Invalid'}), 404)


@app.errorhandler(422)
def handle_422_found(error):
	return make_response(jsonify({'error' : 'Invalid receipt parameters'}), 422)

@app.errorhandler(400)
def non_empty_input(error):
    return make_response(jsonify({'error' : 'Receipt Id cannot be empty'}), 400)




    
if __name__=="__main__":
	app.run(debug=True, host="0.0.0.0", port=5000)

