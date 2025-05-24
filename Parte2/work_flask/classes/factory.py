from classes.gclass import Gclass

class Factory(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_factories_id','_factories_name','_location']

    header = 'Factory'
    
    des = ['Id','Name','Location']
    
    def __init__(self, id, name, location):
        super().__init__()
        
        id = Factory.get_id(id)
        self._factories_id = id
        self._factories_name = name
        self._location = location
        
        Factory.obj[id] = self
        
        Factory.lst.append(id)
        self.maquinas=[]
        

    @property
    def factories_id(self):
        return self._factories_id
    @factories_id.setter
    def factories_id(self, id):
        self._factories_id = id
    
    @property
    def factories_name(self):
        return self._factories_name
    @factories_name.setter
    def name(self, name):
        self._factories_name = name
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        self._location = location
    
    
        
        
        
        
        
