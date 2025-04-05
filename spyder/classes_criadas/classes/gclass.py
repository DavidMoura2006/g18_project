"""
@author: António Brito / Carlos Bragança
(2025) objective: Generic class
"""""
# Generic Class
import sys
import datetime
import sqlite3
class Gclass:
    # Constructor: Called when an object is instantiated
    def __init__(self):
        pass
#################################################        
# generic code: no need to change for a new class    
    # Class method to implement constructor overloading
    @classmethod
    def from_string(cls, str_data):
        str_list = str_data.split(";")
        strarg = 'cls(str_list[0]'
        for i in range(1, len(str_list)):
            strarg += ',str_list[' + str(i) + ']'
        strarg += ')'
        return eval(strarg)
    # Reset the class
    @classmethod
    def reset(cls):
        cls.obj = dict()
        cls.lst = list()
        cls.pos = 0
    # Object identifier auto increment
    @classmethod
    def get_id(cls, id):
        # Compute the auto increment
        id = int(id)
        if id == 0:
            if len(cls.lst) == 0:
                id = 1
            else:
                id = max(cls.lst) + 1
        return id
    # Class method to return the list of object id's having an attribute 'att' = 'value'
    @classmethod
    def getlines(cls, att, value):
        return [obj.id for obj in list(cls.obj.values()) if getattr(obj, att) == value]
    # Class methods to iterate (forward and backward) through the class objects
    @classmethod
    def nextrec(cls):
        cls.pos += 1
        return cls.current()
    @classmethod
    def previous(cls):
        cls.pos -= 1
        return cls.current()
    @classmethod
    def current(cls, code = None):
        if code in cls.lst:
            cls.pos = cls.lst.index(code)
        if cls.pos < 0:
            cls.pos = 0
            return None
        elif cls.pos >= len(cls.lst):
            cls.pos = len(cls.lst) - 1
            return None
        else:
            code = cls.lst[cls.pos]
            return cls.obj[code]
    @classmethod
    def first(cls):
        cls.pos = 0
        return cls.current()
    @classmethod
    def last(cls):
        cls.pos = len(cls.lst) - 1
        return cls.current()
    # Object delete method
    @classmethod
    def remove(cls, p):
        obj = cls.obj[p]
        id = cls.att[0][1:]
        command = f'DELETE FROM {cls.__name__} WHERE {id}={cls.conv(obj,id,p)}'
        cls.sqlexe(command)
        cls.lst.remove(p)
        del cls.obj[p]
    # Object insert method
    @classmethod
    def insert(cls, p):
        obj = cls.obj[p]
        command = f'INSERT INTO {cls.__name__} VALUES('
        for att in cls.att:
            value = getattr(obj, att)
            command += f'{cls.conv(obj, att, value)},'
        command = command[:-1] + ")"
        cls.sqlexe(command)
    # Object update method
    @classmethod
    def update(cls, p):
        obj = cls.obj[p]
        command = f'UPDATE "{cls.__name__}" SET'
        for att in cls.att[1:]:
            value = getattr(obj, att)
            command += f' {att[1:]} = {cls.conv(obj, att, value)},'
        id = cls.att[0][1:]
        command = command[:-1] + f' WHERE {id} = {cls.conv(obj, id, p)}'
        print(command)
        cls.sqlexe(command)
    @staticmethod
    def conv(obj, att, value):
        v = getattr(obj, att)
        if type(v) == str or type(v) == datetime.date:
            ret = f'"{value}"'
        else:
            ret = f'{value}'
        return ret
    # Sort objects by attribute class methods
    @classmethod
    def orderfunc(cls, e):
        return getattr(cls.obj[e], cls.sortkey)
    @classmethod
    def sort(cls, att, reverse = False):
        cls.sortkey = att
        cls.lst.sort(key=cls.orderfunc, reverse= reverse)
    # Find objects having an attribute equal to value
    @classmethod
    def find(cls, value, att):
        lobj = cls.obj.values()
        fobj = [obj for obj in lobj if getattr(obj, att) == value]
        return fobj
    # Apply a filter by attribute class methods
    @classmethod
    def set_filter(cls, f_dic = {}):
        if f_dic:
            code = cls.att[0]
            lobj = cls.obj.values()
            s = set()
            for att,listf in f_dic.items():
                s1 = set([getattr(obj, code) for obj in lobj if getattr(obj, att) in listf])
                s = s.union(s1)
            if len(s) > 0:
                cls.lst = list(s)
                cls.pos = 0
        else:
            obj = cls.current()
            cls.lst = list(cls.obj.keys())
            code = cls.att[0]
            cls.current(getattr(obj, code))
    # Get a list of objects attribute values
    @classmethod
    def getatlist(cls, att):
        return [getattr(obj, att) for obj in list(cls.obj.values())]
    # Read objects from db file
    @classmethod
    def read(cls, path = ''):
        cls.obj = dict()
        cls.lst = list()
        cls.path = path
        try:
            fh = open(path, 'r')
            fh.close()
            lista = cls.sqlexe("select * from " + cls.__name__)
            if lista != None:
                for r in lista:
                    objstr = f'{r[0]}'
                    for att in range(1,len(lista[0])):
                        objstr += f';{r[att]}'
                    cls.from_string(objstr)
        except FileNotFoundError:
            print(f"ERROR: {path} data file not found")
        except BaseException as err:
            print(f"Error in read method:\n{err}\n{type(err)}")
            sys.exit()
    # Instance method to obtain object info
    def __str__(self):
        strprint = "f'"
        for att in type(self).att:
            strprint += '{self.' + att + '};'
        strprint = strprint[:-1] + "'"
        return eval(strprint)
    # Execute a db query
    @classmethod
    def sqlexe(cls, command):
        resul = None
        try:
            con = sqlite3.connect(cls.path)
            cur = con.cursor()
            con.row_factory = sqlite3.Row
            tname = cls.__name__
            cur = con.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tname}'")
            table = cur.fetchone()
            if table is None or table[0] != tname:
                print(f"ERROR: table {tname} missing in database {cls.path}")
                sys.exit()
            cur = con.execute(command)
            resul = cur.fetchall()
            con.commit()
            con.close()
        except sqlite3.Error as er:
            print(f'sqlite error: {er}')
        return resul
