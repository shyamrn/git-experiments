# Sample application for texting docker

#* Import libraries
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

#* Flask app
app = Flask(__name__)

@app.route('/modify', methods=['POST'])
def modify_text():
    if request.method=='POST':
        input_text = request.get_json()['input_text']
        modified_text = input_text.split(".")[0]
        return jsonify({'modified_text':modified_text})

if __name__=='__main__':
    app.run(debug=True)
