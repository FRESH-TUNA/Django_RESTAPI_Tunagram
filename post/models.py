from django.db import models
from tunagramAuth.models import User
import logging

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    pub_Date = models.DateTimeField(auto_now_add=True)
    up_Date  = models.DateTimeField(auto_now=True)

    def traverse_comment_tree(self, obj_with_comments):
        result = []
        for comment in obj_with_comments.siblings.all():
            result += [comment] + self.traverse_comment_tree(comment)
        return result


    def all_comments(self):
        result = []
        for comment in self.comment_set.all().filter(depth=0):
            result += [comment] + self.traverse_comment_tree(comment)
        logging.error(result)
        return result


    def __str__(self):
        return self.title
    
    @property
    def nickname(self):
        return self.user.nickname

    @property
    def getPartOfContent(self):
        return self.content[:3] + '...'

