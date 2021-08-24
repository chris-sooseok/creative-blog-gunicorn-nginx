from .models import Setting
import json
from django.contrib.auth.decorators import login_required
from config.settings import DISPLAY_APPS
# pass app_display_dict from setting model if the value is set

def apps(request):
    if request.user.is_authenticated:
        user = request.user
        app = Setting.objects.get(user=user)
        if app.app_display_dict != None:
            return {'app_display_dict':json.loads(app.app_display_dict), 'display_apps': DISPLAY_APPS}
        else:
            return {'emtpy':"empty"}
    else:  
        return {'empty':'empty'}

