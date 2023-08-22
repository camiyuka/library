from rest_framework import serializers 
from books import models

#nome do nome + serializer 
class BookSerializer(serializers.ModelSerializer):
    class Meta: # class interna
        model= models.Book
        fields= '__all__'