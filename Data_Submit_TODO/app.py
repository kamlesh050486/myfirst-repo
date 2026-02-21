from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os

print("Script is running")

app = Flask(__name__)

@app.route("/todo")
def todo():
    print("Script is running in todo")
    return render_template("todo.html")

client = MongoClient("mongodb+srv://kamlesh4java_db_user:pass123@cluster0.e4p6a7v.mongodb.net/mydatabase")
#db = client["todo_db"]
#collection = db["items"]
db = client["mydatabase"]
collection = db["users"]


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)

    return "Item Stored Successfully!"

if __name__ == "__main__":
        app.run(debug=True)