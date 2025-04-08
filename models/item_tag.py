from db import db

class ItemTags(db.Modle):
    __tablename__ = "items_tag"
    
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Colum(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Colum(db.Integer, db.ForeignKey("tag.id"))
    