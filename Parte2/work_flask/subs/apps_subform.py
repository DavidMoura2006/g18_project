from flask import Flask, render_template, request, session
from datafile import filename
from classes.courses import Courses
from classes.course_instructors import Courses_Instructors
from classes.instructor import Instructors
from classes.platform import Platforms
from classes.userlogin import Userlogin

prev_option = ""

def apps_subform(cname=""):
    global prev_option
    tlist = cname.split('.')
    cnames = tlist[0]
    scname = tlist[1]
    ulogin=session.get("user")
    if (ulogin != None):
        cl = eval(cnames)
        sbl = eval(scname)
        cl_header = cl.header
        sbl_header = sbl.header
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if prev_option == 'insert' and option == 'save':
            strobj = request.form[cl.att[0]]
            for i in range(1,len(cl.att)):
                strobj += ";" + request.form[cl.att[i]]
            obj = cl.from_string(strobj)
            cl.insert(getattr(obj, cl.att[0]))
            cl.last()
        elif prev_option == 'edit' and option == 'save':
            obj = cl.current()
            for i in range(1,len(cl.att)):
                setattr(obj, cl.att[i], request.form[cl.att[i]])
            cl.update(getattr(obj, cl.att[0]))
        else:
            if option == "edit":
                butshow = "disabled"
                butedit = "enabled"
            elif option == "delete":
                obj = cl.current()
                lines = sbl.getlines(sbl.att[1],getattr(obj, cl.att[0]))
                for line in lines:
                    sbl.remove(line.id)
                cl.remove(obj.id)
                if not cl.previous():
                    cl.first()
            elif option == "insert":
                butshow = "disabled"
                butedit = "enabled"
            elif option == 'cancel':
                pass
            elif option == "first":
                cl.first()
            elif option == "previous":
                cl.previous()
            elif option == "next":
                cl.nextrec()
            elif option == "last":
                cl.last()
            elif option[:6] == "delrow":
                row = int(option.split("_")[1])
                obj = cl.current()
                lines = sbl.getlines(sbl.att[1],getattr(obj, cl.att[0]))
                # print(row,lines[row])
                sbl.remove(lines[row])
            elif option == "addrow":
                butshow = "disabled"
                butedit = "disabled"
            elif option == "saverow":
                obj = cl.current()
                strobj = '0'
                # strobj = getattr(obj, cl.att[0])
                for i in range(1, len(sbl.att)):
                    strobj += ";" + request.form[sbl.att[i]]
                objl = sbl.from_string(strobj)
                # code = str(getattr(objl, sbl.att[0])) + str(getattr(objl, sbl.att[1]))
                sbl.insert(objl.id)
            elif option == 'exit':
                return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = cl.current()
        headers = list()
        objl = list()
        if option == 'insert' or len(cl.lst) == 0:
            obj = dict()
            obj[cl.att[0]] = 0
            for i in range(1, len(cl.att)):
                obj[cl.att[i]] = ""
        else:
            for i in range(1, len(sbl.att)):
                    headers.append(sbl.att[i][1:])        
            lines = sbl.getlines(sbl.att[1],getattr(obj, cl.att[0]))
            for line in lines:
                objl.append(sbl.obj[line])
        # return render_template("gform.html", butshow=butshow, butedit=butedit, cname=cname, code=code,name = name,dob=dob,salary=salary)
        return render_template("subform.html", cl_header=cl_header,sbl_header=sbl_header,butshow=butshow, butedit=butedit, cname=cname, obj=obj,att=cl.att,des=cl.des, ulogin=session.get("user"),objl=objl,desl=sbl.des, attl=sbl.att)
    else:
        return render_template("index.html", ulogin=ulogin)
# -*- coding: utf-8 -*-

