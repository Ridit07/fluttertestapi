from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def returnascii():
    d = {}
    inputchr1 = str(request.args['query1'])
    inputchr2 = str(request.args['query2'])
    answer1 = str(ord(inputchr1))
    answer2 = str(ord(inputchr2))
    d['output1'] = answer1
    d['output2'] = answer2
    return d

if __name__ =="__main__":
    app.run()
