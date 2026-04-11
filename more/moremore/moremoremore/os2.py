import os

# VULNERABLE: Command injection
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    os.system(f'ping -c 4 {ip}')
