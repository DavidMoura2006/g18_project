from flask import Flask, render_template, request, session
from classes.factory import Factory
from datafile import filename
from classes.inventory import Inventory
from classes.machine import Machine
from classes.maintenancelog import MaintenanceLog
from classes.userlogin import Userlogin
from datetime import datetime


app = Flask(__name__)
Userlogin.read(filename + 'users.db')
app.secret_key = 'BAD_SECRET_KEY'

Machine.read(filename + 'factorys.db')
Factory.read(filename + 'factorys.db')
Inventory.read(filename + 'factorys.db')
MaintenanceLog.read(filename + 'factorys.db')

prev_option_factory = ""
prev_option_machine = ""
prev_option_maintenancelog = ""
prev_option_inventory = ""
prev_option = ""

@app.route("/factory", methods=["POST", "GET"])
def factory():
    global prev_option_factory
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Factory.current()
        Factory.remove(obj.id)
        if not Factory.previous():
            Factory.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_factory == 'insert' and option == 'save':
        strobj = str(Factory.get_id(0)) + ";" + request.form["_factory_name"] + ';' + \
                 request.form["_location"]
        obj = Factory.from_string(strobj)
        Factory.insert(obj.id)
        Factory.last()
    elif prev_option_factory == 'edit' and option == 'save':
        obj = Factory.current()
        obj._factory_name = request.form["_factory_name"]
        obj._location = request.form["_location"]
        Factory.update(obj.id)
    elif option == "first":
        Factory.first()
    elif option == "previous":
        Factory.previous()
    elif option == "next":
        Factory.nextrec()
    elif option == "last":
        Factory.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_factory = option
    obj = Factory.current()

    if option == 'insert' or len(Factory.lst) == 0:
        id = Factory.get_id(0)
        _factory_name = _location = ""
    else:
        id = obj.id
        _factory_name = obj._factory_name
        _location = obj._location

    return render_template("index.html", tipo="factory", butshow=butshow, butedit=butedit,
                           id=id, _factory_name=_factory_name, _location = _location,
                           ulogin=session.get("user"))



@app.route("/maintenancelog", methods=["POST", "GET"])
def maintenancelog():
    global prev_option_maintenancelog
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = MaintenanceLog.current()
        MaintenanceLog.remove(obj.id)
        if not MaintenanceLog.previous():
            MaintenanceLog.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_maintenancelog == 'insert' and option == 'save':
        strobj = str(MaintenanceLog.get_id(0)) + ';' + \
                  request.form["_details_maintenancelogs"] + ';' + request.form["_log_date"] + ';' + \
                request.form["_technician"] + ';' + request.form["_maintenance_date"]
        obj = MaintenanceLog.from_string(strobj)
        MaintenanceLog.insert(obj.id)
        MaintenanceLog.last()
    elif prev_option_maintenancelog == 'edit' and option == 'save':
        obj = MaintenanceLog.current()
        obj._details_maintenancelogs = request.form["_details_maintenancelogs"]
        obj._log_date = request.form["_log_date"]
        obj._technician = request.form["_technician"]
        obj._maintenance_date = request.form["_maintenance_date"]
        MaintenanceLog.update(obj.id)
    elif option == "first":
        MaintenanceLog.first()
    elif option == "previous":
        MaintenanceLog.previous()
    elif option == "next":
        MaintenanceLog.nextrec()
    elif option == "last":
        MaintenanceLog.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_maintenancelog = option
    obj = MaintenanceLog.current()

    if option == 'insert' or len(MaintenanceLog.lst) == 0:
        id = MaintenanceLog.get_id(0)
        _details_maintenancelogs = _log_date = _technician = _maintenance_date = ""
    else:
        id = obj.id
        _details_maintenancelogs = obj._details_maintenancelogs
        _log_date = obj._log_date
        _technician = obj._technician
        _maintenance_date = obj._maintenance_date

    return render_template("index.html", tipo="maintenancelog", butshow=butshow, butedit=butedit,
                            id=id, _details_maintenancelogs=_details_maintenancelogs, _log_date=_log_date, _technician=_technician,
                            _maintenance_date=_maintenance_date, ulogin=session.get("user"))

@app.route("/machine", methods=["POST", "GET"])
def machine():
    global prev_option_machine
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Machine.current()
        Machine.remove(obj.id)
        if not Machine.previous():
            Machine.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_machine == 'insert' and option == 'save':
        strobj = str(Machine.get_id(0)) + ';' + request.form["_machines_type"] + ';' + \
                 request.form["_capacity"] + ';' + request.form["_purchase_date"] 
        obj = Machine.from_string(strobj)
        Machine.insert(obj.id)
        Machine.last()
    elif prev_option_machine == 'edit' and option == 'save':
        obj = Machine.current()
        obj._machines_type = request.form["_machines_type"]
        obj._capacity = request.form["_capacity"]
        obj._purchse_date = request.form["_purchase_date"]
        Machine.update(obj.id)
    elif option == "first":
        Machine.first()
    elif option == "previous":
        Machine.previous()
    elif option == "next":
        Machine.nextrec()
    elif option == "last":
        Machine.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_machine = option
    obj = Machine.current()

    if option == 'insert' or len(Machine.lst) == 0:
        id = Machine.get_id(0)
        _machines_type = _capacity = _purchase_date = ""
    else:
        id = obj.id
        _machines_type = obj._machines_type
        _capacity= obj._capacity
        _purchase_date = obj._purchase_date

    return render_template("index.html", tipo="machine", butshow=butshow, butedit=butedit,
                           id=id, _machines_type=_machines_type, _capacity=_capacity,
                           _purchase_date=_purchase_date,
                           ulogin=session.get("user"))



@app.route("/inventory", methods=["POST", "GET"])
def inventory():
    global prev_option_inventory
    butshow, butedit = "enabled", "disabled"
    option = request.args.get("option")

    if option == "edit":
        butshow, butedit = "disabled", "enabled"
    elif option == "delete":
        obj = Inventory.current()
        Inventory.remove(obj.id)
        if not Inventory.previous():
            Inventory.first()
    elif option == "insert":
        butshow, butedit = "disabled", "enabled"
    elif option == 'cancel':
        pass
    elif prev_option_inventory == 'insert' and option == 'save':
        strobj = str(Inventory.get_id(0)) + ';' + request.form["_factories_id"] + ';' + \
                  request.form["_machines_id"]
        obj = Inventory.from_string(strobj)
        Inventory.insert(obj.id)
        Inventory.last()
    elif prev_option_inventory == 'edit' and option == 'save':
        obj = Inventory.current()
        obj._factories_id = int(request.form["_factories_id"])
        obj._machines_id = int(request.form["_machines_id"])
        Inventory.update(obj.id)
    elif option == "first":
        Inventory.first()
    elif option == "previous":
        Inventory.previous()
    elif option == "next":
        Inventory.nextrec()
    elif option == "last":
        Inventory.last()
    elif option == 'exit':
        return "<h1>Thank you for using this app</h1>"

    prev_option_inventory = option
    obj = Inventory.current()

    if option == 'insert' or len(Inventory.lst) == 0:
        id = Inventory.get_id(0)
        _factories_id = _machines_id = ""
    else:
        id = obj.id
        _factories_id = obj._factories_id
        _machines_id = obj._machines_id

    return render_template("index.html", tipo="inventory", butshow=butshow, butedit=butedit,
                            id=id, _factories_id=_factories_id, _machines_id=_machines_id,
                            ulogin=session.get("user"))







@app.route("/")
def index():
    return render_template("index.html", ulogin=session.get("user"))
    
@app.route("/login")
def login():
    return render_template("login.html", id= 0, user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("Index1.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("Index1.html", ulogin=session.get("user"))
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
            return render_template("index1.html", ulogin=session.get("user"))
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
        return render_template("index1.html", ulogin=ulogin)


if __name__ == '__main__':
    app.run()
    
