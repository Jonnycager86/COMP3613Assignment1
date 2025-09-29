from App.database import db
from sqlalchemy import ForeignKey

class Staff_shift(db.Model):
    __tablename__ ="staff_shift"
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    shift_id = db.Column(db.Integer, db.ForeignKey('shift.id'))
    
    