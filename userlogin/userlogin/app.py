from flask import Flask, render_template, request, session
from datafile import filename
from classes.userlogin import Userlogin

app = Flask(__name__)

Userlogin.read(filename + 'business.db')
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'

@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return render_template("login.html", id= 0, user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    msg = ""
    ulogin=session.get("user")
    if (ulogin != None):
        user_id = Userlogin.get_user_id(ulogin)
        group = Userlogin.obj[user_id].usergroup
        if group != "admin":
            Userlogin.current(user_id)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            if obj.id != user_id:
                Userlogin.remove(obj.id)
                if not Userlogin.previous():
                    Userlogin.first()
            else:
                msg = 'You cannot delete the same user'
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            user = request.form["user"]
            if len(Userlogin.find(user, 'user')) == 0:
                usergroup = request.form["usergroup"]
                password =  request.form["password"]
                obj = Userlogin(0, user, usergroup, Userlogin.set_password(password))
                Userlogin.insert(obj.id)
                Userlogin.last()
            else:
                msg = 'duplicate username'
                Userlogin.current()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
            Userlogin.update(obj.id)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            id = 0
            user = ""
            usergroup = ""
            password = ""
        else:
            id = obj.id
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, msg=msg,id=id, user=user,
                               usergroup = usergroup,password=password,ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)

if __name__ == '__main__':
    app.run()