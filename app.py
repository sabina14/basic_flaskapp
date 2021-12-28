from flask import Flask,request,jsonify, render_template



app=Flask(__name__)


@app.route('/',methods=['GET']) #called by web browser, so empty field
def index():
    return render_template('index.html') #to showcase page in a webpage




@app.route('/math',methods=['POST'])

def math_operation():
    if (request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if (operation == 'subtract'):
            r = num1 - num2
            result = 'the differnce of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if (operation == 'multiply'):
            r = num1 * num2
            result = 'the product of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if (operation == 'division'):
            r = num1 / num2
            result = 'the division  of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        return render_template('results.html',result=result)


@app.route('/via_postman',methods=['POST'])

def math_operation_via_postman():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        if(operation=='add'):
            r=num1+num2
            result='the sum of '+str(num1) + 'and' + str(num2)+'is' + str(r)
        if(operation=='subtract'):
            r=num1-num2
            result='the differnce of '+str(num1) + 'and' + str(num2)+'is' + str(r)
        if(operation=='multiply'):
            r=num1*num2
            result='the product of '+str(num1) + 'and' + str(num2)+'is' + str(r)
        if(operation=='division'):
            r=num1/num2
            result='the division  of '+str(num1) + 'and' + str(num2)+'is' + str(r)
        return jsonify(result)






if __name__=="__main__":
    print("the app is working")
    app.run()