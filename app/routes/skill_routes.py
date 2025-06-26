from flask import Blueprint, jsonify
from ..models.skill import Skill
from ..schemas.member_schema import MemberSchema
from ..helpers.message_response import message_response

skill_bp = Blueprint('skill', __name__)
members_schema = MemberSchema(many=True)


@skill_bp.route('/<int:skill_id>/members', methods=['GET'])
def get_members_by_skill(skill_id):
    skill = Skill.query.get(skill_id)
    if not skill:
        return message_response("Skill Not Found", 404)

    if not skill.members:
        return message_response("Skill Has No Members")

    return jsonify(members_schema.dump(skill.members))
