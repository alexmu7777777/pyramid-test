from deform import ValidationFailure, Form
from pyramid.view import view_config

from apps.todo.forms import MySchema

INCOMING_DATE_FMT = '%d/%m/%Y %H:%M:%S'


# @view_config(route_name="tasks", request_method="POST", renderer='json')
# def create_task(request):
#     """Create a task for one user."""
#     print("create_task")
#     response = request.response
#     response.headers.extend({'Content-Type': 'application/json'})
#     user = request.dbsession.query(User).filter_by(username=request.matchdict['username']).first()
#     if user:
#         due_date = request.json['due_date']
#         task = Task(
#             name=request.json['name'],
#             note=request.json['note'],
#             due_date=datetime.strptime(due_date, INCOMING_DATE_FMT) if due_date else None,
#             completed=bool(request.json['completed']),
#             user_id=user.id
#         )
#         request.dbsession.add(task)
#         response.status_code = 201
#         return {'msg': 'posted'}


# @view_config(route_name="info", renderer='templates/form.pt')
def create_task(request):
    schema = MySchema()
    my_form = Form(schema, buttons=('submit',))
    template_values = {}
    template_values.update(my_form.get_widget_resources())

    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            my_form.validate(controls)
        except ValidationFailure as e:
            template_values['form'] = e.render()
        else:
            template_values['form'] = 'OK'
        return template_values

    template_values['form'] = my_form.render()
    return template_values
