
from App.database import db
from sqlalchemy import ForeignKey

class Shift(db.Model):
   __tablename__ = "shift"
   id = db.Column(db.Integer, primary_key=True, nullable = False)
   start_time = db.Column(db.DateTime)
   end_time = db.Column(db.DateTime)
   
   

def __init__(self, id, start_time, end_time):
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        
        
def __repr__(self):
        return f" Shift {self.id}  {self.start_time, self.end_time} "

def get_json(self):
        return{
            'id': self.id,
           # 'username': self.username
        }



