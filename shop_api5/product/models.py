from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # review = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title



class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveSmallIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not 1 <= self.stars <= 5:
            raise ValueError("Значение рейтинга должно быть от 1 до 5")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.text

