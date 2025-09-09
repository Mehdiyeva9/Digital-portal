from rest_framework import serializers
from core.models import Collab, OurService, ContactForm, Program, Blog, Comment, SiteSettings
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, attrs):
        validate_password(attrs["password"])
        return attrs
    
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username = username,
            password = password
        )
        return user

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