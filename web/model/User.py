from web import db
import uuid
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  username = db.Column(db.String(100), unique=True, nullable=False)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(100), nullable=False)
