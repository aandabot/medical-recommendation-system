
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Sample medicine database
medicine_db = {
    "headache": "Ibuprofen",
    "fever": "Paracetamol",
    "cold": "Cetrizine",
    "cough": "Dextromethorphan",
    "diabetes": "Metformin"
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    symptom = request.form.get("symptom")
    medicine = medicine_db.get(symptom.lower(), "Not Found")
    return jsonify({"recommendation": medicine})

if __name__ == '__main__':
    app.run(debug=True)
