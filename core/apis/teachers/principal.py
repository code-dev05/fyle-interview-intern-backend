from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from .schema import TeacherSchema

principal_teacher_resources = Blueprint("principal_teacher_resources", __name__)

@principal_teacher_resources.route('/teachers', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list all teachers"""
    principal_teachers = Teacher.get_teachers_by_principal()
    principal_teachers_dump = TeacherSchema().dump(principal_teachers, many=True)
    return APIResponse.respond(data=principal_teachers_dump)