from rest_framework import serializers
from .models import Article

# class ArticleSerializers(serializers.Serializer):
#     id=serializers.IntegerField(required=False)
#     titel=serializers.CharField(max_length=50)
#     text=serializers.CharField(max_length=400)
#     status=serializers.BooleanField()
#
#
#     def create(self, validated_data):
#
#         return Article.objects.create(**validated_data)

class ArticleSerializers(serializers.ModelSerializer):
    text=serializers.CharField(write_only=True)

    class Meta:
        model=Article
        fields=["text","titel","status","id"]
        read_only_fields=("id",)
