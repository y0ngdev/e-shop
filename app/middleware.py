# from django.utils import timezone
# from django.conf import settings
# from django.contrib.auth import logout
# from rest_framework.authtoken.models import Token


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

#     def __call__(self, request):

#         if not request.user.is_authenticated:
#             header = request.headers.get('Authorization')
#             if header:
#                 try:
#                     token_type, token = header.split(' ')
#                     if token_type.lower() == 'token':
#                         Token.objects.filter(key=token).delete()
#                 except ValueError:
#                     print("Invalid Authorization header format")

#         response = self.get_response(request)
#         return response
