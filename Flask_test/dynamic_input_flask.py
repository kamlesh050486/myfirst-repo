from flask import Flask, request

app = Flask(__name__) 
@app.route('/api')        
def name():
    name = request.values.get('name')   # import request
    age = request.values.get('age')
    result = {
             'name':name,
             'age':age
       }
    return result
if __name__ == '__main__':
     app.run(debug =True)