from main.models import Product, Category, Tag, Review
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    product_reviews = ReviewSerializer(many=True)
    filtered_reviews = serializers.SerializerMethodField()
    filtered_reviews_2 = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id filtered_reviews_2 name price created_at category tags product_reviews filtered_reviews'.split()  # Чтобы вывести из БД только эти поля
        # fields = ['id', 'name', 'price']
        # exclude = 'update_at'.split()  # Чтобы вывести все поля кроме этого указанного

    def get_filtered_reviews(self, product):
        # reviews = product.product_reviews.filter(stars__gt=3)
        reviews = Review.objects.filter(product=product, stars__gt=3)
        return ReviewSerializer(reviews, many=True).data


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
