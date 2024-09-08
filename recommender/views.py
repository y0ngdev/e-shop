from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from recommender.recommender import recommend


# Create your views here.


class RecommenderView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        top_n = 9
        recommended_products = recommend(pk, top_n)

        return Response({'Top {top_n} products recommended for customer {pk}':  recommended_products}, status=status.HTTP_200_OK)
