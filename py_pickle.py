@app.route('/load')
def load_data():
    data = request.get_data()
    obj = pickle.loads(data)  # B3 vulnerability
