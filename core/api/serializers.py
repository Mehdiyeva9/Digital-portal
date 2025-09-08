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

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class SiteSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"