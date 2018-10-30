from flask import Flask, render_template

class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update({
        "variable_start_string":"[[",
        "variable_end_string":"]]"
        })
app = VueFlask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)