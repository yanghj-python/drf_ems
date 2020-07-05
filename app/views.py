from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from app.serializers import EmployeeModelSerializer
from app.models import User, Employee
from utils.response import APIResponse
from app.serializers import UserModelSerializer
class UserAPIView(APIView):
    def post(self,request,*args,**kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        return APIResponse(200,True,results=UserModelSerializer(user_obj).data)
    def get(self,request,*args,**kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")
        user = User.objects.filter(username=username,password=password).first()
        if user:
            data = UserModelSerializer(user).data
            return APIResponse(200,True,results=data)

        return APIResponse(400,False)
class EmployeeView(ListModelMixin,GenericAPIView,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = "id"
    def get(self,request,*args,**kwargs):
        if kwargs.get("id"):
            res = self.retrieve(request,*args,**kwargs)
        else:
            res = self.list(request,*args,**kwargs)
        return APIResponse(200,True,results=res.data)
    def post(self,request,*args,**kwargs):
        res = self.create(request,*args,**kwargs)
        return APIResponse(200,True,results=res.data)
    def patch(self,request,*args,**kwargs):
        res = self.update(request,*args,**kwargs)
        return APIResponse(200,True,results=res.data)
    def delete(self,request,*args,**kwargs):
        ids = kwargs.get("id")
        if ids:
            self.destroy(request, *args, **kwargs)
        return APIResponse(200,True)

