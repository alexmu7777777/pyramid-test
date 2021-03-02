from datetime import datetime
from pyramid.view import view_config
from apps.todo.models import Task, User

INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'


@view_config(route_name="tasks", request_method="POST", renderer='json')
def create_task(request):
    """Create a task for one user."""
    print("create_task")
    response = request.response
    response.headers.extend({'Content-Type': 'application/json'})
    user = request.dbsession.query(User).filter_by(username=request.matchdict['username']).first()
    if user:
        due_date = request.json['due_date']
        task = Task(
            name=request.json['name'],
            note=request.json['note'],
            due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
            completed=bool(request.json['completed']),
            user_id=user.id
        )
        request.dbsession.add(task)
        response.status_code = 201
        return {'msg': 'posted'}

#
# @view_config(route_name="info", renderer='templates/index.html')
# def create_task(request):
#     return {'msg': 'test'}
