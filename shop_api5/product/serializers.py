from rest_framework import serializers
from .models import Product, Category, Review, ReviewRating


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title description price category'.split()


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()

    class Meta:
        model = Category
        fields = 'id name product_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()




class ProductReviewSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    review = ReviewSerializer(many=True)



    class Meta:
        model = ReviewRating
        fields = ' title description price category id text stars  '.split()




def get_rating(obj):
    reviews = obj.reviews.all()
    if reviews.exists():
        return round(sum([review.stars for review in reviews]) / reviews.count(), 2)
    return None














