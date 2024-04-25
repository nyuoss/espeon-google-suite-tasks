from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    # This will render the 'index.html' when the root URL is accessed
    return render_template('index.html', title='Google Suite Manager Tool')

# Additional routes and functionalities can be defined here

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='127.0.0.1', port=5000)