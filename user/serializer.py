from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from user.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        # 字段应该写哪些  应该写参与序列化与反序列化的并集
        fields = ("username", "password")

        # 添加DRF官方所提供的校验规则
        extra_kwargs = {
            "username": {
                "required": True,  # 设置为必填项
                "min_length": 8,  # 最小长度
                "error_messages": {
                    "required": "用户名必须填写",
                    "min_length": "用户名长度太短了"
                }
            },
            "password": {
                "required": True,  # 设置为必填项
                "min_length": 8,  # 最小长度
                "error_messages": {
                    "required": "密码必须填写",
                    "min_length": "密码长度太短了"
                }
            },
        }

    def validate_username(self, value):
        book = User.objects.filter(username=value)
        if book:
            raise exceptions.ValidationError("用户名已存在")
        return value

class UserModelSerializer2(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        # 添加DRF官方所提供的校验规则
        extra_kwargs = {
            "username": {
                "required": True,  # 设置为必填项
                "error_messages": {
                    "required": "用户名必须填写",
                }
            },
            "password": {
                "required": True,  # 设置为必填项
                "error_messages": {
                    "required": "密码必须填写",
                }
            },
        }



