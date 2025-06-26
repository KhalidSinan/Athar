from app.models.deal_with import deal_with
from ..extensions import db


class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birth = db.Column(db.Date)
    university = db.Column(db.String(100))
    qualification = db.Column(db.Text)
    academic_experience = db.Column(db.Text)
    rating = db.Column(db.Numeric(2, 1))
    photo = db.Column(db.Text)
    status = db.Column(db.Enum('WORKING', 'NOT_WORKING',
                       'BUSY', name='status_enum'), nullable=False)
    skills = db.relationship(
        'Skill', secondary=deal_with, back_populates='members')
