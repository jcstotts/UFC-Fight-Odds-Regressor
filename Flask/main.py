from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Example fighter data
fighters = [
    "Conor McGregor", "Khabib Nurmagomedov", "Israel Adesanya", "Jon Jones", 
    "Stipe Miocic", "Francis Ngannou", "Jorge Masvidal", "Kamaru Usman", 
    "Dustin Poirier", "Tony Ferguson"
]

@app.route('/')
def home():
    return render_template('index.html')

# Route for predicting odds (placeholder)
@app.route('/predict', methods=['POST'])
def predict():
    fighter1 = request.form['fighter1']
    fighter2 = request.form['fighter2']
    
    # Placeholder odds prediction logic
    odds_fighter1 = 1.75
    odds_fighter2 = 2.25

    result = f"Odds for {fighter1}: {odds_fighter1}, Odds for {fighter2}: {odds_fighter2}"
    return render_template('result.html', fighter1=fighter1, fighter2=fighter2, result=result)

# Autocomplete route to return fighter suggestions based on input
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q')
    suggestions = [fighter for fighter in fighters if query.lower() in fighter.lower()]
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)
