from pyramid.response import Response
from pyramid.view import view_config


from .lib import ticketer


@view_config(route_name='home', renderer='templates/ticket_home.mako')
def ticket_home(request):
    return {}

@view_config(route_name='ticket', renderer='json')
def get_fare(request):
    ticket_machine = ticketer.Ticketer(request)
    return ticket_machine.calculate_fare(request.POST.get('start_station'), request.POST.get('end_station') )

