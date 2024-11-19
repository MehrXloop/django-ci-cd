from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

fakeUsers = [
    {
    'name':'mehr',
    'email':'mehr@gmail.com',
    'age':22
},
    {
    'name':'mehr',
    'email':'mehr@gmail.com',
    'age':22
},
    {
    'name':'mehr',
    'email':'mehr@gmail.com',
    'age':22
}
]


@api_view(['GET'])
def get_user(request):
    user = User.objects.all()
    return Response(UserSerializer(user, many=True).data)


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        print(request)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PATCH','DELETE','GET'])
def user_details(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response("user not found")
    
    if request.method == "DELETE":
        user.delete()
        return Response("user deleted", status=status.HTTP_200_OK)
    
    if request.method == "GET":
       gettingUser = UserSerializer(user)
       return Response(gettingUser.data, status=status.HTTP_200_OK)
    
    if request.method == "PATCH":
        gettingUser = UserSerializer(user, data=request.data)
        if gettingUser.is_valid():
            gettingUser.save()
            return Response("user Updated")
        return Response(gettingUser.errors, status=status.HTTP_400_BAD_REQUEST)

