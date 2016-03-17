from django.http import HttpResponse

def __is_valid_credential(secret):


    if secret == 'SuperSecret':
        return True
    else:
        return False

def project(request,project_id):
    try:
        secret = request.META['HTTP_SIGNATURE']
    except:
        return False

    if not __is_valid_credential(secret):
        return HttpResponse('Invalid credentital:')
    if request.method == "GET":
        return HttpResponse('Fetching information for project: '+project_id)
    if request.method == "PUT":
        return HttpResponse('Creating/Updating project: '+project_id)
    if request.method == "POST":
        return HttpResponse('Creating/Updating project: '+project_id)
    if request.method == "DELETE":
        return HttpResponse('Removing project: '+project_id)
    if request.method == "OPTIONS":
        return HttpResponse('Valid options for'+request.path+'GET,PUT,PUSH,DELETE,OPTIONS')
