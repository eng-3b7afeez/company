from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def endpoints(request):
    urls = [
        "admin/",
        "api/ auth/",
        "api/ token/ [name='token_obtain_pair']",
        "api/ token/refresh/ [name='token_refresh']",
    ]
    return Response(urls)
