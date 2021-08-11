from .models import App
import json


def apps(request):
    if request.user.is_authenticated:
        user = request.user
        app = App.objects.get(user=user)
        if app.display_list != None:
            return {'app_display_dict':json.loads(app.app_display_dict)}
        else:
            return {}
    else:  
        return {}

