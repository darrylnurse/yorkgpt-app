from flask import Flask, request, jsonify
from yorkgpt import get_model_response
from waitress import serve
from flask_cors import CORS, cross_origin

# initialize Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/yorkgpt", methods=['POST'])
@cross_origin()
def yorkgpt():

    # go fetch
    data = request.get_json() 

    # reject the request with error 400 if question header is not present or if the data is not fetched
    if not data or 'question' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    # parse question from request and input it to model
    question = data.get('question') 
    result = get_model_response(question) 

    # error handle the result and format it as json
    if result:
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Failed to get a valid response from the model"}), 500

# start the Flask server
if __name__ == "__main__":
    print('Server is running on port 3000.')
    serve(app, host="0.0.0.0", port=3000)
