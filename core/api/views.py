from core.models import Collab, OurService, ContactForm, Program, Blog, Comment, SiteSettings
from core.api.serializers import UserCreateSerializer, CollabSerializer, OurServiceSerializer, ContactFormSerializer, ProgramSerializer, BlogSerializer, CommentSerializer, SiteSettingSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer