from flask import Flask, request, render_template,redirect,sessions
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index():
    """show first page"""

    return render_template("index.html")

@app.route('/application-success')
def username():
    firstname = request.args.get("firstname")
    lastname = request.args.get('lastname')

    return render_template("/application-response.html")
	
@app.route('/application-success')
def position():
    position = request.args.get("position")
    return render_template("/application-response.html")




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
