from flask import Blueprint, render_template, request

VISIBLE = "visible"
HIDDEN = "hidden"

bp = Blueprint("blog", __name__)
visibility = HIDDEN
answer = ""


@bp.route("/", methods=["GET", "POST"])
def index():
    global visibility
    global answer
    if request.method == "POST":
        prompt = request.form.get("prompt")
        # TODO: Do API calls here
        answer = f"You have entered: {prompt}"
        visibility = VISIBLE

    return render_template("index.html", visibility=visibility, answer=answer)
