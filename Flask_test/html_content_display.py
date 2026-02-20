from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv('uri')
print(MONGO_URI)
#uri = "mongodb+srv://kamlesh4java_db_user:pass123@cluster0.e4p6a7v.mongodb.net/myappdb?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
client = pymongo.MongoClient(MONGO_URI)
db = client.get_default_database()   #Get database name

print("Connected to DB:", db.name)

collection = db['testdata']
app = Flask(__name__)     # initializing flask
@app.route('/')
def home():
    start_time = datetime.now()
    day_of_week = start_time.strftime('%A, %H:%M:%S')
    return render_template('index.html',day_of_week=day_of_week)  # need import render_template 

@app.route('/submit',methods=['POST'])
def submit():
       
       #Name = request.form.get("name")
       #Pwd = request.form.get("password")
      # return render_template('index.html',name=Name,password=Pwd)
      
       form_data = dict(request.form)
       collection.insert_one(form_data)
       return 'Data submitted successfully'
@app.route('/view')
def view():
       data = collection.find()
       data = list(data)
       for item in data:
              print(item)
              del item['_id']
              data = {
                     'data':data
              } 
       return data
if __name__ == '__main__':
       app.run(debug =True) 