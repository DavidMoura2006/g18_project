from classes.gclass import Gclass
from classes.machine import Machine
from classes.factory import Factory

class Inventory(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_factories_id','_machines_id']
    header = 'Inventory'
    des = ['factories_id','machines_id']

    def __init__(self, factories_id, machines_id):
        super().__init__()

        # Verifica se a factory_id e machine_id existem nas listas (assumindo que as listas contêm apenas IDs)
        if int(factories_id) not in Factory.lst:
            print('Factory', factories_id, 'not found')
            return

        if int(machines_id) not in Machine.lst:
            print('Machine', machines_id, 'not found')
            return

        # self._id = int(id)
        self._factories_id = int(factories_id)
        self._machines_id = int(machines_id)

        # Inventory.obj[self._id] = self
        # Inventory.lst.append(self._id)

    # @property
    # def id(self):
    #     return self._id
    # @id.setter
    # def id(self, id):
    #     self._id = id

    @property
    def factories_id(self):
        return self._factories_id
    @factories_id.setter
    def factories_id(self, factories_id):
        self._factories_id = factories_id

    @property
    def machines_id(self):
        return self._machines_id
    @machines_id.setter
    def machines_id(self, machines_id):
        self._machines_id = machines_id
    
