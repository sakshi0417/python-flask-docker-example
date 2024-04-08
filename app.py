from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_world():
        # Return a simple message when the root URL is accessed
    return "Hello, World!"
    

# This block of code ensures that the Flask app is run only when this script is executed directly
if __name__ == '__main__':
    # Run the app in debug mode for development
       app.run(debug=True)  
