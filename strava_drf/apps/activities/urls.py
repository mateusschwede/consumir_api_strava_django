from django.urls import path
from .views import ActivitiesView, StravaCallbackView

urlpatterns = [
    path("activities/", ActivitiesView.as_view(), name="activities"),
    path("strava/callback/", StravaCallbackView.as_view(), name="strava-callback"),
]