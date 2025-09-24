from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

from App.models.user import User
from sqlalchemy import ForeignKey

class Admin(User):
   __tablename__ = "admin"

   id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
   
   __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
   
   def __init__(self, username, password):
          super().__init__(username, password)
    
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

