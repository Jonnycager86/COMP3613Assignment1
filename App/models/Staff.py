from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

from App.models.user import User
from sqlalchemy import ForeignKey

class Staff(User):
   __tablename__ = 'staff'
   id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
   position = db.Column(db.String(60))
   shifts = db.relationship("Shift", secondary = 'staff_shift', backref=db.backref('staff_members'), lazy=True)
   time_logs = db.relationship("Timelog", backref='staff', lazy=True)
   
   __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }
   
   
   def __init__(self, username, password):
          super().__init__(username, password)
          
   def __repr__(self):
        return f'<Staff {self.username}>'
    
   def get_json(self):
          return {
             'id': self.id,
             'username': self.username
          }
    
   def set_password(self, password):
          """Create hashed password."""
          self.password = generate_password_hash(password)

   def check_password(self, password):
          """Check hashed password."""
          return check_password_hash(self.password, password)

