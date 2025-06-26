from app.models.deal_with import deal_with
from ..extensions import db


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(100), nullable=False)
    members = db.relationship(
        'Member', secondary=deal_with, back_populates='skills')
