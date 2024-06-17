from db import db

class ItemModel(db.Model): #Inherits from db.Model
    __tablename__ = 'items' #New Table named items

    id = db.Column(db.Integer, primary_key=True) #Auto incrementing primary key
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False) #Foreign key. Has to match an ID from a store
    store = db.relationship("StoreModel", back_populates="items") #Gets the store object associated with the item
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")