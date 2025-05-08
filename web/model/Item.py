from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from web import db

class Item(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  name = db.Column(db.String(100), unique=True, nullable=False)
  price = db.Column(db.Integer(), default=0, nullable=False)
  createdAt = db.Column(db.DateTime, default=datetime.utcnow)
  updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 