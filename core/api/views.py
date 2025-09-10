from core.models import Collab, OurService, ContactForm, Program, Blog, Comment, SiteSettings
from core.api.serializers import UserCreateSerializer, CollabSerializer, OurServiceSerializer, ContactFormSerializer, ProgramSerializer, BlogSerializer, CommentSerializer, SiteSettingSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class CollabListAPIView(ListAPIView):
    queryset = Collab.objects.all()
    serializer_class = CollabSerializer

class OurServiceListAPIView(ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer

class ContactFormListAPIView(ListAPIView):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

