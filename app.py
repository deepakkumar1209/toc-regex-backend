from flask import Flask, request, jsonify, send_file
from nfa_converter import regex_to_nfa
from dfa_converter import nfa_to_dfa
import os

app = Flask(__name__)
OUTPUT_FOLDER = "static"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    regex = data.get("regex", "")
    try:
        nfa_path = os.path.join(OUTPUT_FOLDER, "nfa.png")
        dfa_path = os.path.join(OUTPUT_FOLDER, "dfa.png")

        nfa = regex_to_nfa(regex)
        nfa.draw(nfa_path)

        dfa = nfa_to_dfa(nfa)
        dfa.draw(dfa_path)

        return jsonify({
            "nfa_image_url": f"{request.url_root}static/nfa.png",
            "dfa_image_url": f"{request.url_root}static/dfa.png"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
