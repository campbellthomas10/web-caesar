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
                background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(9,9,121,1) 35%, rgba(0,212,255,1) 100%);
            }}

            h1 {{
                text-align: center;
                color: white;
            }}

            footer {{
                color: white;
                font-size: 8pt;
                width: 540px;
                margin: 0 auto;
                margin-top: 5px;
            }}

            form {{
                background-color: #eee;
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
            }}
        </style>
    </head>
    <body>
      <h1>Caesar Encrypter</h1>
      <form method="POST">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0">
        <br />
        <textarea name="text">{0}</textarea>
        <br />
        <input type="submit" value="Send">
      </form>
      <footer>By: Tommy Campbell<br />Last Updated: 6/11/19</footer>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    try:
        rot = request.form['rot']
        text = request.form['text']
        encrypted = rotate_string(text,int(rot))
        return form.format(encrypted)
    except ValueError:
        return form.format('Enter a number in "Rotate by:"')
    
app.run()