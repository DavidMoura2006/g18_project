from classes.gclass import Gclass
from classes.machine import Machine
from classes.factory import Factory

class Inventory(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    att = ['_id', '_factories_id', '_machines_id']
    header = 'Inventory'
    des = ['Id', 'Factory Id', 'Machine Id']

    def __init__(self, id, factories_id, machines_id):
        super().__init__()

        factories_id = int(factories_id)
        machines_id = int(machines_id)

        # Verificar se IDs existem
        if factories_id not in Factory.lst:
            print(f'Factory {factories_id} not found')
            return

        if machines_id not in Machine.lst:
            print(f'Machine {machines_id} not found')
            return

        id = Inventory.get_id(id)
        self._id = id
        self._factories_id = factories_id
        self._machines_id = machines_id

        Inventory.obj[id] = self
        Inventory.lst.append(id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def factories_id(self):
        return self._factories_id
    @factories_id.setter
    def factories_id(self, value):
        self._factories_id = value

    @property
    def machines_id(self):
        return self._machines_id
    @machines_id.setter
    def machines_id(self, value):
        self._machines_id = value

