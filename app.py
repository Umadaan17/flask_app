from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

@app.route('/math')
def math_operation():
    if (request.method =='POST'):
        ops=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if (ops=='add'):
            r=num1+num2
            result='the sum of'+str(num1)+ 'and'+str(num2)+ 'is'+ str(r)
            return render_template('results.html',result=result)


app.run()