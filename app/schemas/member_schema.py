from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_sqlalchemy.fields import Nested
from app.models.member import Member
from app.schemas.skill_schema import SkillSchema


class MemberSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Member
        load_instance = True
        include_relationships = True
        include_fk = True

    skills = Nested(SkillSchema, many=True)
