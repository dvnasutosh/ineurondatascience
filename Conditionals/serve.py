
from urllib import request
from flask  import Flask, request,jsonify;

app = Flask(__name__)

@app.route('/test',methods=['GET','POST'])
def test1():
    if (request.method=='POST'):
        a= request.json['num1']
        b= request.json['num2']
        result= a/b;
        return jsonify((str(result)))



# Write a program to insert a record in sql table via api 



if __name__== '__main__':
    app.run()