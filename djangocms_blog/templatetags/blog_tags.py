from django import template
#from .models import BlogPostCategory
register = template.Library()

#@register.simple_tag #simple_tag is now working... TODO: check versions?
def has_access(request,post):
    try:
        cats=post.categories.all()
        if cats==None:
            ccat=0
        else:
            ccat=len(cats)
        if ccat==0: #no category - default to public
            return True
        else:
            for cat in cats:
                intersect=cat.groups.all() & request.user.groups.all()
                if len(intersect)>0:
                    return True
        return False
    except Exception as err:
        print('blog_tags exception:',str(err))
        return False

#@register.simple_tag
def trim(textin,cnt,append='...'):
    
    return textin[:cnt]+append


register.filter('trim', trim)
register.filter('has_access', has_access)