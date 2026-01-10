import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StravaCallbackView(APIView):
    def get(self, request):
        code = request.GET.get("code")

        if not code:
            return Response(
                {"error": "Code não informado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        token_url = "https://www.strava.com/oauth/token"

        payload = {
            "client_id": settings.STRAVA_CLIENT_ID,
            "client_secret": settings.STRAVA_CLIENT_SECRET,
            "code": code,
            "grant_type": "authorization_code",
        }

        response = requests.post(token_url, data=payload)

        if response.status_code != 200:
            return Response(
                {
                    "error": "Erro ao autenticar no Strava",
                    "details": response.text,
                },
                status=response.status_code,
            )
        return Response(response.json(), status=status.HTTP_200_OK)

class ActivitiesView(APIView):
    def get(self, request):
        url = "https://www.strava.com/api/v3/athlete/activities"

        headers = {
            "Authorization": f"Bearer {settings.STRAVA_ACCESS_TOKEN}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            return Response(
                {
                    "error": "Erro ao buscar atividades no Strava",
                    "details": response.text,
                },
                status=response.status_code,
            )
        return Response(response.json(), status=status.HTTP_200_OK)