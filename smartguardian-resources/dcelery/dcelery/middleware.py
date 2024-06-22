# from channels.auth import AuthMiddlewareStack
# from django.contrib.auth.models import AnonymousUser
# from rest_framework_simplejwt.tokens import UntouchedAccessToken
# from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
# from urllib.parse import parse_qs

# class TokenAuthMiddleware:
#     def __init__(self, inner):
#         self.inner = inner

#     def __call__(self, scope):
#         query_string = parse_qs(scope['query_string'].decode())
#         token = query_string.get('token')

#         if not token:
#             scope['user'] = AnonymousUser()
#             return self.inner(scope)

#         try:
#             UntouchedAccessToken(token[0])
#         except TokenError:
#             scope['user'] = AnonymousUser()
#         else:
#             # Replace with your own logic to get the user
#             user = ... 
#             scope['user'] = user

#         return self.inner(scope)

# TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))