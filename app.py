
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Lab</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>My CI/CD Pipeline Works!</h1>
            <p>Experiment 5 - Jenkins, Docker and AWS EC2</p>
            <p>Version 1</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
