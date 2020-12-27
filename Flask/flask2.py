from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    html_text="""<html>
    <head>
    <title>Programming with Gautam</title>
    </head>
    <body>
    <h1 style="text-align:center"> Welcome to Flask Tutuorial by Programming With Gautam</h1>
    </body>
    </html>"""
    return html_text

if __name__ =="__main__":
    app.run()