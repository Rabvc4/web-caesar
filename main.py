from flask import Flask, request, redirect, render_template
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])

def encrypt():

    rot = request.form['rot']
    text = request.form['text']

    rot_error = ''

    if not is_integer(rot):
        rot_error = 'Please try again with a valid integer.'
        rot = ''
    else:
        rot = int(rot)

    if not rot_error:
        rotated_text = rotate_string(text, rot)
        return render_template('form.html',
            rotated_text=rotated_text)
    else:
        return render_template('form.html',
            rot_error=rot_error)


app.run()
