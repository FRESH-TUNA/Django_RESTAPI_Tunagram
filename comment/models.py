from django.db import models
from account.models import User
from post.models import Post

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parentComment = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE, related_name='siblings')
    depth = models.IntegerField(default=0)
    content = models.CharField(max_length=200)
    pub_Date = models.DateTimeField(auto_now_add=True)
    up_Date  = models.DateTimeField(auto_now=True)

    


