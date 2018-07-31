from flask import Flask, render_template_string
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return render_template_string("""
        <!doctype html>
            <html>
            <head>
                <title>Example Site</title>
                <meta charset="utf-8" />
                <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="stylesheet" type="text/css" href="static/css/client.css">
            </head>
            <body>
                <div>
                    <h1>Example Site</h1>
                    <p>Every instance of this site will execute some payload and return the results back.</p><br>
                </div>
                <script type="text/javascript" src="static/javascript/client.js"></script>
            </body>
            </html>
        """)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
