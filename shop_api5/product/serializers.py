from rest_framework import serializers
from .models import Product, Category, Review


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


def get_rating(obj):
    reviews = obj.reviews.all()
    if reviews.exists():
        return round(sum([review.stars for review in reviews]) / reviews.count(), 2)
    return None


class ProductReviewSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id name reviews rating'.split()


    def get_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.exists():
            return get_rating(reviews)
        return None







