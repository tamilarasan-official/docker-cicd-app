from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Docker CI/CD Pipeline! This application is running with GitHub Actions automation, Docker containerization, and automated deployment from DockerHub. Build once, deploy everywhere!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
