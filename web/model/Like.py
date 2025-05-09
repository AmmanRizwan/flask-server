from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from web import db
from web.model.Item import Item

# Small one-to-many relation with the Item
class Like(db.Model):
  id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
  like = db.Column(UUID(as_uuid=True), db.ForeignKey("item.id"))