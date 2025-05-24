from classes.gclass import Gclass
import datetime

class Machine(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_machines_id','_machines_type','_capacity','_purchase_date']

    header = 'Machine'
    
    des = ['Id','Type','Capacity','Purchase Date']
    
    def __init__(self, id, type, capacity, data_compra):
        super().__init__()
        
        id = Machine.get_id(id)
        self._machines_id = id
        self._machines_type = type
        self._capacity = capacity
        self._purchase_date = datetime.datetime.strptime(data_compra, "%Y/%m/%d").date()
        
        Machine.obj[id] = self
        
        Machine.lst.append(id)
        self.factories=[]
        
    @property
    def machines_id(self):
        return self._machines_id
    @machines_id.setter
    def machines_id(self, id):
        self._machines_id = id
    
    @property
    def machines_type(self):
        return self._machines_type
    @machines_type.setter
    def machines_type(self, name):
        self._machines_type = name
    
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, c):
        self._capacity = c
    
    @property 
    def purchase_date(self):
        return self._purchase_date
    
    @purchase_date.setter 
    def purchase_date(self,nd):
        self._purchase_date = nd
    
    
