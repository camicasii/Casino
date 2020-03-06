from datetime import datetime
from uuid import uuid1
class Ticket:
    def __init__(self,serial=uuid1().hex,value=[]):
        super().__init__()
        self.serial =serial
        self.value = value
        self.date =datetime.now()
    def __repr__(self):
            return f"ticket serial {self.serial} numero {self.value}"
