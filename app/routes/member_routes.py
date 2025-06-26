from flask import Blueprint, abort, jsonify, request
from marshmallow import ValidationError
from app.schemas.pagination_schema import PaginationSchemaFactory
from ..models.member import Member
from ..models.skill import Skill
from ..schemas.member_schema import MemberSchema
from ..schemas.skill_schema import SkillSchema
from ..services.pagination_response import pagination_response
from ..extensions import db
from ..helpers.message_response import message_response

member_bp = Blueprint('member', __name__)
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
members_pagination_schema = PaginationSchemaFactory(
    MemberSchema, items_key="members")
skills_schema = SkillSchema(many=True)


# MARK: GET ALL MEMBERS
@member_bp.route('/', methods=['GET'])
def get_all_members():
    status = request.args.get('status')
    min_rating = request.args.get('min_rating', type=float)
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    query = Member.query

    if status:
        query = query.filter_by(status=status)
    if min_rating is not None:
        query = query.filter(Member.rating >= min_rating)

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    result = pagination_response(pagination, items_key="members")
    return jsonify(members_pagination_schema.dump(result))


# MARK: GET ONE MEMBER
@member_bp.route('/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get(member_id)
    if not member:
        return message_response("Member Not Found", 404)
    return jsonify(member_schema.dump(member))


# MARK: SEARCH MEMBER
@member_bp.route('/search', methods=['GET'])
def search_members():
    query_text = request.args.get('q', '')
    if not query_text:
        return message_response("No Members Found", 404)

    members = Member.query.filter(Member.name.ilike(f"%{query_text}%")).all()
    if not members:
        return message_response("No Members Found", 404)
    return jsonify(members_schema.dump(members))


# MARK: ADD MEMBER
@member_bp.route('/', methods=['POST'])
def add_member():
    data = request.get_json()

    name = data.get('name')
    birth = data.get('birth')

    existing_member = Member.query.filter_by(name=name, birth=birth).first()
    if existing_member:
        return message_response("Member already exists", 400)

    try:
        new_member = member_schema.load(data, session=db.session)
    except ValidationError as err:
        return message_response(err.messages, 400)

    db.session.add(new_member)
    db.session.commit()
    return jsonify(member_schema.dump(new_member)), 201


# MARK: DELETE MEMBER
@member_bp.route('/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = Member.query.get(member_id)
    if not member:
        return message_response("Member Not Found", 404)

    db.session.delete(member)
    db.session.commit()
    return message_response("Member Deleted Successfully")

# MARK: MEMBER SKILLS


@member_bp.route('/<int:member_id>/skills', methods=['GET'])
def get_skills_for_member(member_id):
    member = Member.query.get(member_id)
    if not member:
        return message_response("Member Not Found", 404)

    if not member.skills:
        return message_response("Member Has No Skills")

    return jsonify(skills_schema.dump(member.skills))
