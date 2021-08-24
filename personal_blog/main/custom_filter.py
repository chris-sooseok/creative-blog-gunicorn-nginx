from django.template.defaulttags import register



# filter the value that the key is matched from dict
@register.filter(name='lookup')
def lookup(dict, key):
    try:
        return dict[key]
    except:
        return False

