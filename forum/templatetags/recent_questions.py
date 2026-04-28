from django import template

from forum.models import PostBaseModel

register = template.Library()


class RecentQuestionsNode(template.Node):
    def __init__(self,count,searched_posts,varname):
        self.count=int(count)
        self.varname=varname
        self.searched_posts=template.Variable(searched_posts)

    def render(self,context):
        filtered_posts = self.searched_posts.resolve(context)
        recent_posts = filtered_posts.order_by('-created_at')[:self.count]
        context[self.varname]=recent_posts
        return ''



@register.tag(name='recent_questions')
def get_recent_questions(parser,token):
    try:
        name,count,searched_posts,varname = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            'The tag needs to requires exactly 4 arguments'
        )
    return RecentQuestionsNode(count,searched_posts,varname)
