from ..extensions import db


deal_with = db.Table(
    'deal_with',
    db.Column('member_id', db.Integer, db.ForeignKey(
        'member.id'), primary_key=True),
    db.Column('skill_id', db.Integer, db.ForeignKey(
        'skill.id'), primary_key=True)
)
