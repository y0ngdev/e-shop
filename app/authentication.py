from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise AuthenticationFailed('Invalid token.')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted.')

        # Check if the user is logged in (has an active session)
        if not token.user.is_authenticated:
            raise AuthenticationFailed('User is not logged in.')

        return (token.user, token)
