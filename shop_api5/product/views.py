from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, ProductReviewSerializer
from rest_framework.views import APIView
from django.db.models import Count

@api_view(http_method_names=['GET'])
def product_list_view(request):
    products = Product.objects.all()

    data = ProductSerializer(products, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    try:
         data = ProductSerializer(product).data
         return Response(data=data,
                         status=status.HTTP_200_OK)
    except Product.DoesNotExist:
         return Response (data=data,
                          status=status.HTTP_404_NOT_FOUND)





@api_view(['GET'])
def category_view(request):
    category = Category.objects.all()

    data = CategorySerializer(category, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def category_detail_view(request, id):
    category = Category.objects.get(id=id)
    try:
         data = CategorySerializer(category).data

         return Response(data=data,
                         status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response (data=data,
                         status=status.HTTP_404_NOT_FOUND)


class CategoryListAPIView(APIView):
        def get(self, request):
            categories = Category.objects.annotate(product_count=Count('product'))
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()

    data = ReviewSerializer(reviews, many=True).data

    return Response(data=data,
                    status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, id):
    review = Review.objects.get(id=id)
    try:
         data = ReviewSerializer(review).data
         return Response(data=data,
                         status=status.HTTP_200_OK)
    except Review.DoesNotExist:
         return Response(data=data,
                         status=status.HTTP_404_NOT_FOUND)

class ProductReviewListAPIView(generics.ListAPIView):
        queryset = Product.objects.prefetch_related('reviews').all()
        serializer_class = ProductReviewSerializer






