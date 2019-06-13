from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            body {{
                font-family: Verdana, sans-seriff;
                background: linear-gradient(90deg, rgba(254,254,254,1) 0%, rgba(55,55,55,1) 50%, rgba(255,255,255,1) 100%);
            }}
            h1 {{
                text-align: center;
                color: black;
                background-color: rgba(255, 255, 255, 0.75);
                width: 540px;
                margin-top: 5%;
                margin-left: auto;
                margin-right: auto;
                border-radius: 25px;
            }}

            footer {{
                color: white;
                font-size: 8pt;
                color: black;
                width: 540px;
                margin: 0 auto;
            }}

            form {{
                background-color: rgba(255, 255, 255, 0.75);
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
                resize: vertical;
            }}
        </style>
    </head>
    <body>
      <h1>Caesar Encrypter</h1>
      <form method="POST">
        <label for="rot">Rotate by:</label>
        <input type="number" step=1 name="rot" value="0">
        <br />
        <textarea name="text">{0}</textarea>
        <br />
        <input type="submit" value="Send">
      </form>
      <footer>By: Tommy Campbell<br />Last Updated: 6/13/19</footer>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypted = rotate_string(text,int(rot))
    return form.format(encrypted)

    
app.run()