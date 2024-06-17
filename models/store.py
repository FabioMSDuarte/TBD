from db import db

class StoreModel(db.Model):
    __tablename ="stores" #Table named stores

    id = db.Column(db.Integer, primary_key=True) #Auto incrementing primary key
    name = db.Column(db.String(80), unique=True, nullable=False)
    #Gets the item from the database."back_populates" creates a relation between items and stores. 
    #"Lazy" means the items are not loaded until they are needed.
    #Cascade deletes the item when the store is deleted.
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic") 
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")