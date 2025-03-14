from django.db import models

"""
SELECT * FROM posts; ---> posts = Post.objects.all();

SELECT * FROM posts WHERE rate > 2; ---> posts = Post.objects.filter(rate_gt=2)

SELECT * FROM posts WHERE id=1; ---> posts = Post.objects.get(id=1);
"""


class Post(models.Model):
    title = models.CharField(max_length=156)
    content = models.CharField(max_length=356)
    rate = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


    def __str__(self):
        return f"{self.title} {self.content}"

