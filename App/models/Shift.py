
from App.database import db
from sqlalchemy import ForeignKey

class Shift(db.Model):
   __tablename__ = "shift"
   id = db.Column(db.Integer, primary_key=True, nullable = False)
   staff_id = db.Column(db.Integer, ForeignKey('staff.id'))
   start_time = db.Column(db.DateTime)
   end_time = db.Column(db.DateTime)
   
   

def __init__(self, id, staff_id, start_time, end_time):
        self.id = id
        self.staff_id = staff_id
        self.start_time = start_time
        self.end_time = end_time
        
        
def __repr__(self):
        return f'<Shift-id {self.id}>'

def get_json(self):
        return{
            'id': self.id,
           # 'username': self.username
        }



