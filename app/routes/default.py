from flask import render_template  # , Blueprint
from .. import app

# default_blueprint = Blueprint("default", __name__, url_prefix="/")


@app.get("/")
def main():
    return render_template("main.html")
