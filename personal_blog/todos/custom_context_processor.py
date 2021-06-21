from datetime import date

def current_date_renderer(request):
    return {
       'current_date': date.today()
    }

