from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models.manager import Manager


class ManagerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Manager
        load_instance = True
