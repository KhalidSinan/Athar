from flask import Blueprint, jsonify
from ..models.manager import Manager
from ..schemas.manager_schema import ManagerSchema

manager_bp = Blueprint('manager', __name__)
manager_schema = ManagerSchema()
managers_schema = ManagerSchema(many=True)


@manager_bp.route('/', methods=['GET'])
def get_managers():
    managers = Manager.query.all()
    return jsonify(managers_schema.dump(managers))
