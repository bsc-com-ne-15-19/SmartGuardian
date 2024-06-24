from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView

class LoginAPIView(APIView):
    """
    API view for handling user login requests.
    
    This view authenticates a user with a username and password, and returns
    JWT tokens upon successful authentication.
    """
    
    def post(self, request):
        """
        Handle POST request to authenticate a user.
        
        Parameters:
        - request: HttpRequest object containing the login credentials.
        
        Returns:
        - Response object with JWT tokens if authentication is successful.
        - Response object with error message and status code 400 if authentication fails.
        """
        # Extract username and password from request data
        username = request.data.get("username")
        password = request.data.get("password")
        
        # Attempt to authenticate the user with the provided credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # User is authenticated, generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),  # Token to obtain new access token upon expiration
                'access': str(refresh.access_token),  # Token to access protected resources
            })
        else:
            # Authentication failed, return error response
            return Response({"error": "Wrong Credentials"}, status=400)