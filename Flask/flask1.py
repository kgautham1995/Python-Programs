from flask import Flask

app=Flask(__name__)

@app.route('/')
def wish():
    return "Hello World, Welcome to Flask Framework"
if __name__ == "__main__":
    app.run()