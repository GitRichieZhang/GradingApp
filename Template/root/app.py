from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
