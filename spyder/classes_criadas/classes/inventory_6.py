from classes.gclass import Gclass
from machines import Machine
from factorys import Factory

class Inventory(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id','_factory_id','_machine_id']
    header = 'Inventory'
    des = ['id','factory_id','machine_id']

    def __init__(self, id, factory_id, machine_id):
        super().__init__()

        # Verifica se a factory_id e machine_id existem nas listas (assumindo que as listas contêm apenas IDs)
        if int(factory_id) not in Factory.lst:
            print('Factory', factory_id, 'not found')
            return

        if int(machine_id) not in Machine.lst:
            print('Machine', machine_id, 'not found')
            return

        self._id = int(id)
        self._factory_id = int(factory_id)
        self._machine_id = int(machine_id)

        Inventory.obj[self._id] = self
        Inventory.lst.append(self._id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def factory_id(self):
        return self._factory_id
    @factory_id.setter
    def factory_id(self, factory_id):
        self._factory_id = factory_id

    @property
    def machine_id(self):
        return self._machine_id
    @machine_id.setter
    def machine_id(self, machine_id):
        self._machine_id = machine_id
