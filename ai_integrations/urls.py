from django.urls import path

from .views import GenerateSummaryView

urlpatterns = [
    path("generate-summary/", GenerateSummaryView.as_view(), name="generate_summary"),
]
