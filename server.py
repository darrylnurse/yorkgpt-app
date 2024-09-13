from flask import Flask, request, jsonify
from yorkgpt import get_model_response

app = Flask(__name__)

@app.route("/yorkgpt", methods=['POST'])
def yorkgpt():
    data = request.get_json() 

    if not data or 'question' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    question = data.get('question') 
    result = get_model_response(question) 

    if result:
        return jsonify({"result": result})
    else:
        return jsonify({"error": "Failed to get a valid response from the model"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)