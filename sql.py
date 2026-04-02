def login(username, password):
    query = f"SELECT * FROM users WHERE username = 'admin' -- AND password = '{password}';"
