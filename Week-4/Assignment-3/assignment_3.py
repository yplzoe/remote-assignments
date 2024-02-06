from flask import Flask, request, render_template, url_for, redirect, make_response, flash

import connect_sql

app = Flask(__name__)
app.secret_key = "key"


@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        # get info of user
        email = request.form.get('email')
        pwd = request.form.get('password')
        print(email, pwd)
        btn = request.form.get('action')
        print(btn)

        if request.form.get('action') == 'sign-up':
            print('sign up')
            all_correct, exist_email, result = connect_sql.check_db(email, pwd)
            if exist_email == False:
                print('not in db')
                connect_sql.add_to_db(email, pwd)
                resp = make_response(redirect('/member_page'))
                resp.set_cookie('email', email)
                resp.set_cookie('pwd', pwd)
                return resp

            else:
                print('already in db')
                flash('The email has been registered before.')

        elif request.form.get('action') == 'sign-in':
            print('sign in')
            all_correct, exist_email, result = connect_sql.check_db(email, pwd)
            if all_correct:
                print('found in db')
                resp = make_response(redirect('/member_page'))
                resp.set_cookie('email', email)
                resp.set_cookie('pwd', pwd)
                return resp
            elif exist_email:
                print('wrong pwd')
                flash('Wrong password.')
            else:
                print('cannot get info')
                flash('The email has not been registered before.')

        else:
            print('error in button')

    return render_template("home.html")


@app.route("/member_page", methods=['GET', 'POST'])
def member_page():
    user_email = request.cookies.get('email')
    return render_template("member.html", email=user_email)


@app.route("/del")
def del_cookie():
    res = make_response('delete cookies')
    res.delete_cookie('email')
    res.delete_cookie('pwd')
    return res


@app.route("/clear_db")
def clear_db():
    connect_sql.delete_all()
    res = make_response('clear all data in user')
    return res


if __name__ == '__main__':
    # for HTTP server
    app.run(debug=True, port=3000)
