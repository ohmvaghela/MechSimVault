"""
Site User API Views
--------------------

This module contains API views for managing site users.
"""

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    SiteUserSerializer,
    SiteUserCreateSerializer,
    SiteUserLoginSerializer,
    SiteUserUpdateSerializer
)
from rest_framework.views import APIView
from .models import SiteUser
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SiteUserList(APIView):
    """
    Retrieves a list of all site users.

    **GET** /site-users/

    Returns:
        200 OK: List of site users

    Notes:
        This view does not require authentication.
        It returns a list of all site users, including their details.
    """
    def get(self, request):
        # Retrieve all site users from the database
        users = SiteUser.objects.all()
        
        # Serialize the users using SiteUserSerializer
        # The 'many=True' argument indicates that we're serializing multiple objects
        serializer = SiteUserSerializer(users, many=True)
        
        # Return the serialized data with a 200 OK status code
        return Response(serializer.data, status=status.HTTP_200_OK)

class SiteUserById(APIView):
    """
    Retrieves a site user by ID.

    **GET** /site-users/<pk>/

    Args:
        pk (int): Site user ID

    Returns:
        200 OK: Site user details
        404 Not Found: If the user is not found

    Notes:
        This view does not require authentication.
        It returns the details of a single site user.
    """
    def get(self, request, pk):
        # Attempt to retrieve the site user by ID from the database
        try:
            user = SiteUser.objects.get(pk=pk)
        except SiteUser.DoesNotExist:
            # If the user is not found, return a 404 Not Found response
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the user using SiteUserSerializer
        serializer = SiteUserSerializer(user)
        
        # Return the serialized data with a 200 OK status code
        return Response(serializer.data, status=status.HTTP_200_OK)

class SiteUserCreate(APIView):
    """
    Creates a new site user.

    **POST** /site-users/

    Args:
        request.data (dict): Site user data (e.g., email, password, name)

    Returns:
        201 Created: Site user details and access token
        400 Bad Request: Validation errors

    Notes:
        This view creates a new site user and generates an access token.
        The access token is returned in the response and set as an HTTP-only cookie.
    """
    def post(self, request):
        # Create a serializer instance with the request data
        serializer = SiteUserCreateSerializer(data=request.data)
        
        # Validate the request data
        if serializer.is_valid():
            # Save the new user to the database
            user = serializer.save()
            
            # Generate a refresh token and access token for the new user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            # Create a response with the user details, access token, and success message
            response = Response({
                "message": "User created successfully",
                "user": SiteUserCreateSerializer(user).data,
                "access_token": access_token
            }, status=status.HTTP_201_CREATED)
            
            # Set the refresh token as an HTTP-only cookie
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='Strict'
            )
            return response
        # Return validation errors if the request data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteUserLogin(APIView):
    """
    Logs in a site user.

    **POST** /site-users/login/

    Args:
        request.data (dict): Site user credentials (e.g., email, password)

    Returns:
        200 OK: Site user details and access token
        400 Bad Request: Validation errors

    Notes:
        This view authenticates a site user and generates an access token.
        The access token is returned in the response and set as an HTTP-only cookie.
    """
    def post(self, request):
        # Create a serializer instance with the request data
        serializer = SiteUserLoginSerializer(data=request.data)
        
        # Validate the request data
        if serializer.is_valid():
            # Get the authenticated user from the serializer
            user = serializer.validated_data['user']
            
            # Generate a refresh token and access token for the user
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            # Serialize the user data
            user_data = SiteUserSerializer(user).data
            
            # Create a response with the user details, access token, and success message
            response = Response({
                "message": "Login successful",
                "user": user_data,
                "access_token": access_token,
            }, status=status.HTTP_200_OK)
            
            # Set the refresh token as an HTTP-only cookie
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='Strict'
            )
            return response
        # Return validation errors if the request data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteUpdateUser(APIView):
    """
    Updates a site user's profile information.

    **POST** /site-users/update/

    Args:
        request.data (dict): Site user data (e.g., name, profile picture)

    Returns:
        202 Accepted: Updated site user details
        400 Bad Request: Validation errors

    Notes:
        This view requires JWT authentication and IsAuthenticated permission.
        Email and password updates are not allowed through this endpoint.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handles user profile update.

        Args:
            request (Request): API request object

        Returns:
            Response: API response object
        """
        # Get the authenticated user
        user = request.user
        
        # Check if email or password is being updated
        if 'email' in request.data or 'password' in request.data:
            # Return error if email or password update is attempted
            return Response({'error': 'Email and password updates are not allowed'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a serializer instance with the user and request data
        serializer = SiteUserUpdateSerializer(user, data=request.data, partial=True)
        
        # Validate the request data
        if serializer.is_valid():
            # Save the updated user data
            serializer.save()
            
            # Return the updated user details
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # Return validation errors if the request data is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SiteUpdatePassword(APIView):
    """
    Updates a site user's password.

    **POST** /site-users/password/

    Args:
        request.data (dict): New password

    Returns:
        200 OK: Success message and access token
        400 Bad Request: Validation errors

    Notes:
        This view requires JWT authentication and IsAuthenticated permission.
        It generates a new access token after updating the password.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Handles password update.

        Args:
            request (Request): API request object

        Returns:
            Response: API response object
        """
        # Get the authenticated user
        user = request.user

        # Get the new password from the request data
        password = request.data.get('password')
        
        # Check if a new password is provided
        if password:
            # Update the user's password
            user.set_password(password)
            user.save()
            
            # Generate a new refresh token and access token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            # Create a response with a success message, user email, and access token
            response = Response({
                "message": "password update successful",
                "user": user.email,
                "access_token": access_token,
            }, status=status.HTTP_200_OK)

            # Set the new refresh token as an HTTP-only cookie
            response.set_cookie(
                key='refresh_token',
                value=refresh_token,
                httponly=True,
                secure=True,
                samesite='Strict'
            )
            return response
        # Return error if no new password is provided
        return Response({"message": "password not found"}, status=status.HTTP_400_BAD_REQUEST)