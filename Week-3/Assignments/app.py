from flask import Flask, request, render_template, url_for, redirect, make_response

app = Flask(__name__)

@app.route("/data", methods=['GET'])
def for_data():
    num = request.args.get('number')
    print(num)
    if num==None:
        return "Lack of Parameter"
    elif num.isdigit():
        num=int(num)
        total_sum=int((1+num)*num/2)
        print(total_sum)
        return "{}".format(total_sum)
    else:
        return "Wrong Parameter"

@app.route("/sum.html")
def sum_of_data():
    return render_template("sum.html")

@app.route("/myName")
def get_name():
    user=request.cookies.get('userID')
    if user!=None:
        return "{}".format(user)
    else:
        return redirect('/trackName')
    
@app.route("/trackName", methods = ['POST', 'GET'])
def track_name():
    print(request.path)
    user=request.args.get('name')
    print(user)
    # resp=make_response('hi')
    resp = make_response(render_template("trackname.html"))
    if user!=None:
        resp.set_cookie('userID', user)
        return "{}".format(user)
    
    # if request.method == 'GET':
    #     resp.set_cookie('userID', user)
    #     return "{}".format(user)
    
    return resp

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"



if __name__ == '__main__':
	app.run(debug=True, port=3000)