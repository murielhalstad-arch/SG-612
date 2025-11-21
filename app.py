from flask import Flask, render_template, request, redirect, url_for
from ai_client import classify

app = Flask(__name__, template_folder="templates", static_folder="static")

TASKS = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            result = classify(title)  # heuristikk nå
            TASKS.append({"title": title, "label": result["label"], "priority": result["priority"]})
        return redirect(url_for("home"))
    return render_template("index.html", tasks=TASKS)

@app.route("/clear", methods=["POST"])
def clear():
    TASKS.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


