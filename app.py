from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    posts = [
        {"title": "First Blog Post", "content": "Welcome to GoodiesReaders!"},
        {"title": "Second Post", "content": "This is your second post!"},
    ]
    return render_template("index.html", posts=posts)

if __name__ == '__main__':
    app.run(debug=True)

