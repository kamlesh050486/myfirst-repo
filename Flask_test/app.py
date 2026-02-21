from flask import Flask
app= Flask(__name__)
@app.route('/')
def home():
    return 'Hello Flask Programmer !!'

@app.route('/aboutMe')
def second():
    return 'Here Kamlesh is Flask Programmer !!'

@app.route('/api/<name>')
def third(name):
    print(name)
    return 'we can see o/p in terminal dynamic API name given in URL'

@app.route('/api')
       def emp():
        return 'Empjson data added'
if __name__== '__main__':
    app.run(debug=True)

