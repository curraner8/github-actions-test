import pickle

# VULNERABLE: Pickle.load on user file
@app.route('/upload')
def upload():
    file = request.files['data']
    obj = pickle.load(file)  # B3 vulnerability
