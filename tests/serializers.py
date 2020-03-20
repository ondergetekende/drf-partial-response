from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from drf_partial_response.serializers import FieldsListSerializerMixin
from rest_framework import serializers

from .models import Comment, Ticket


class UserSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class CommentSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Comment
        fields = ('body', 'author')


class TicketSerializer(FieldsListSerializerMixin, serializers.ModelSerializer):

    author = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ('title', 'body', 'author', 'comments',)
