from classes.gclass import Gclass
import datetime

class MaintenanceLog(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_maintenance_id','_details_maintenancelogs','_log_date','_technician','_maintenance_date']

    header = 'MaintenanceLog'
    
    des = ['maintenance_id','details_maintenancelogs','log_date','technician','maintenance_date']
    
    def __init__(self, id, details, data_log, tecnicos, data_manutencao):
        super().__init__()
        
        id = MaintenanceLog.get_id(id)
        self._maintenance_id = id
        self._details_maintenancelogs = details
        self._date_log = datetime.datetime.strptime(data_log, "%d/%m/%Y").date()
        self._technician = tecnicos
        self._date_maintenance = datetime.datetime.strptime(data_manutencao, "%d/%m/%Y").date()
        
        MaintenanceLog.obj[id] = self
        
        MaintenanceLog.lst.append(id)
        
    @property
    def maintenance_id(self):
        return self._maintenance_id
    @maintenance_id.setter
    def maintenance_id(self, id):
        self._maintenance_id = id
    
    @property
    def details_maintenancelogs(self):
        return self._details_maintenancelogs
    @details_maintenancelogs.setter
    def details_maintenancelogs(self, newdetails):
        self._details_maintenance = newdetails
    
    @property
    def log_date(self):
        return self._log_date
    
    @log_date.setter
    def log_date(self, newdatalog):
        self._log_date = newdatalog
    
    @property 
    def technician(self):
        return self._technician
    
    @technician.setter 
    def technician(self,newtecnico):
        self._technician = newtecnico
    
    @property 
    def maintenance_date(self):
        return self._maintenance_date
    
    @maintenance_date.setter 
    def maintenance_date(self,newdatemaintenance):
        self._maintenance_date = newdatemaintenance
