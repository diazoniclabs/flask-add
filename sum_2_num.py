from flask import Flask
from flask import request
app = Flask(__name__)

'''
@app.route('/add?a=<int:n1>&b=<int:n2>')
def add(n1,n2):
    sum = n1+n2
    return "%d" % (sum)
'''

@app.route('/add',methods=['GET'])
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    return "Sum is %d" % (int(a)+int(b))

# run app
if __name__ == '__main__':
    app.run(debug=True)
