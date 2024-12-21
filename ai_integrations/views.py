import requests
from decouple import config
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class GenerateSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        description_text = request.data.get("description_text")
        if not description_text:
            return Response(
                {"error": "description_text is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Hugging Face API URL and headers
        API_TOKEN = config("HUGGINGFACE_API_TOKEN")
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

        headers = {"Authorization": f"Bearer {API_TOKEN}"}

        try:
            response = requests.post(
                API_URL, headers=headers, json={"inputs": description_text}
            )
            response.raise_for_status()

            summary = response.json()[0]["summary_text"]
            return Response({"description_summary": summary}, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
