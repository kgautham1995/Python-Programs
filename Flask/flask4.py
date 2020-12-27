from flask import Flask
app=Flask(__name__)

@app.route('/validate/<int:age>')
def age_check(age):
    if age >= 18:
        html = """<html>
                    <head>
                        <title>
                        PWG
                        </title>
                    </head>
                    <body align='center'>
                        <h1>Valid user</h1>
                    </body
                </html>"""
    else:
        html = "<html><head><title>PWG</title></head><body align='center'><h1>Invalid user</h1></body</html>"
    return html


if __name__ == "__main__":
    app.run()