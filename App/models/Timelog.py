
from App.database import db
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

class Timelog(db.Model):
    __tablename__ = "timelog"
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    staff_id = db.Column(db.Integer, ForeignKey('staff.id'))
    shift_id = db.Column(db.Integer, ForeignKey('shift.id'))
    time_in = db.Column(db.DateTime)
    time_out = db.Column(db.DateTime)
   

   # def __init__(self):
        

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

   

