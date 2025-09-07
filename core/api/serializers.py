from rest_framework import serializers
from core.models import Collab, OurService, ContactForm, Program, Blog, Comment, SiteSettings

class CollabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collab
        fields = "__all__"

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = "__all__"

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"