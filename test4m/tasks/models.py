from django.db import models


"""
SELECT * FROM posts; ---> posts = Post.objects.all();

SELECT * FROM posts WHERE rate > 2; ---> posts = Post.objects.filter(rate_gt=2)

SELECT * FROM posts WHERE id=1; ---> posts = Post.objects.get(id=1);

"""




class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name



class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return  f"{self.title} {self.description}"
