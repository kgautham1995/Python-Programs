from flask import Flask, render_template

app=Flask(__name__)

@app.route('/<d>')
def name(d):
    return "Hello Mr/Miss :"+d

@app.route('/open/<d>')
def show(d):
    return render_template('demo1.html', d=d)

if __name__ == "__main__":
    app.run(debug=True)