@app.route("/todo")
def todo():
    return render_template("todo.html")