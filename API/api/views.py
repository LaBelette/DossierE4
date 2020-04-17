from django.contrib.auth.models import User
from api.serializers import UserSerializer, ProfilSerializer, StrangethingSerializer, LikeSerializer, CommentSerializer
from api.models import Profil, Strangething, Like, Comment
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfilViewSet(viewsets.ModelViewSet):
    serializer_class= ProfilSerializer
    queryset = Profil.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class StrangethingViewSet(viewsets.ModelViewSet):
    serializer_class= StrangethingSerializer
    queryset = Strangething.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def like_strangething(self, request, pk=None):
        strangething = Strangething.objects.get(id=pk)
        user = request.user
        try:
            like = Like.objects.get(user=user, strangething=strangething)
            like.delete()
            response = {'message': 'Like retiré'}
        except:
            like = Like(user=user,strangething=strangething)
            like.save()
            response = {'message': 'Vous avez bien like'}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def comment_strangething(self, request, pk=None):
        if 'text' in request.data:
            user = request.user
            strangething = Strangething.objects.get(id=pk)
            text = request.data['text']
            try:
                comment = Comment(user=user, strangething=strangething, text=text)
                comment.save()
                response = {'message': 'Commentaire posté !'}
            except:
                comment = Comment.objects.get(user=user, strangething=strangething, text=text)
                response = {'message': 'Vous avez déjà posté un commentaire identique'}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Votre commentaire est vide..!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class= LikeSerializer
    queryset = Like.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class= CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)