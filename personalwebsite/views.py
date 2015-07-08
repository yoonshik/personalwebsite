from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/index.pt')
def home_view(request):
    return {'project': 'personalwebsite'}

@view_config(route_name='pyramid', renderer='templates/mytemplate.pt')
def pyramid_view(request):
    return {'project': 'personalproject2'}
