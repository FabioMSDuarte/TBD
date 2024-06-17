from marshmallow import Schema, fields
#This class has no store ID. It is used to create a new item with no relation to a store.
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True) #You cannot send an ID through the API (as payload). These IDs can only be sent back to the client from the database.
    name = fields.Str(required=True) #This field must be in the JSON payload
    price = fields.Float(required=True)

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    
class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()

# Inherits from PlainItemSchema and adds the store_id field.
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True,load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)

class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema())
    tag = fields.Nested(TagSchema())

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
