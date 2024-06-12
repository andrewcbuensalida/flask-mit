from flask import Flask, render_template

app = Flask(__name__)



@app.route("/", methods=["GET"])
def first_route():
    return "My first GET request"
    
    
 

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
