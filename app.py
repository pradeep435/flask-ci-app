from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Welcome Pradeep, to the page! the have been made in CI/CD Project with Terraform, Jenkins, and Docker is DONE !"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
