from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer
from app.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "username":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名必填",
                    "min_length": "用户名长度不够",
                }
            },
            "password": {
                "required": True,
                "min_length": 6,
                "error_messages": {
                    "required": "密码必填",
                    "min_length": "密码长度不够",
                }
            }
        }
    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")

        return attrs
class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id","emp_name","salary","img","age","check_age")
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名必填",
                    "min_length": "用户名长度不够",
                }
            }
        }
    def validate_emp_name(self, value):
        empname = Employee.objects.filter(emp_name=value)
        if empname:
            raise exceptions.ValidationError("该员工已存在")
        return value