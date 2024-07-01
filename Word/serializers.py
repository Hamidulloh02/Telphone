from rest_framework import serializers
from .models import Word,Wordturkum

class WordturkumSerializers(serializers.ModelSerializer):
    class Meta:
        model= Wordturkum
        fields = ('__all__')

class WordSerializers(serializers.ModelSerializer):
    wordturkumi = WordturkumSerializers()
    class Meta:
        model = Word
        fields = ('id','wordyordamchi','wordturkumi','wordxalqaroteg','worduzbekteg','wordsof','wordshakl','wordmanotur','worduslubiyxoslanish','wordsofturkum','text')