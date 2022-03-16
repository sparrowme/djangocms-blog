from django import template
#from .models import BlogPostCategory
register = template.Library()

#@register.simple_tag #simple_tag is now working... TODO: check versions?
def has_access(request,post):
    try:
        cats=post.categories.all()
        print(cats)
        if cats==None:
            ccat=0
        else:
            ccat=len(cats)
        if ccat==0: #no category - default to public
            return True
        else:
            for cat in cats:
                allcg=cat.groups.all()
                intersect=allcg & request.user.groups.all()
                if len(intersect)>0 or len(allcg)==0:
                    return True
        return False
    except Exception as err:
        print('blog_tags exception:',str(err))
        return False

def has_category_access(request,cat):
    try:
        allcg=cat.groups.all()
        intersect=allcg & request.user.groups.all()
        if len(intersect)>0 or len(allcg)==0:
            return True
        return False
    except Exception as err:
        print('blog_tags exception:',str(err))
        return False

#@register.simple_tag
def trim_content(textin,len,append='...'):
    
    return textin[:len]+append


register.filter('trim_content', trim_content)
register.filter('has_access', has_access)
register.filter('has_category_access', has_category_access)
