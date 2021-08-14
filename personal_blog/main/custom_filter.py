from django.template.defaulttags import register



# filter the value that the key is matched from dict
@register.filter(name='lookup')
def lookup(dict, key):
    return dict[key]

