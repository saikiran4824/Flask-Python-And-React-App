from app import db

class Friend(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  role = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)


  def to_json(self):
    return {
      "id":self.id,
      "name":self.name,
      "role":self.role,
      "description":self.description,
    }

 