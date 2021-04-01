from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ViewSet, GenericViewSet

from user.models import User
from user.serializer import UserModelSerializer, UserModelSerializer2
from utils.response import APIResponse

# class UserGenericAPIView(ListModelMixin,
#                          RetrieveModelMixin,
#                          CreateModelMixin,
#                          DestroyModelMixin,
#                          UpdateModelMixin,
#                          GenericAPIView):
#     # 获取当前视图类要操作的模型
#     queryset = User.objects.all()
#     # 指定当前视图要使用的序列化器类
#     serializer_class = UserModelSerializer
#     # 获取主键名
#     lookup_field = "id"
#
#     def get(self, request, *args, **kwargs):
#         if "id" in kwargs:
#             # 查询单个
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     # 全部
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     # 局部
#     def patch(self, request, *args, **kwargs):
#         response = self.partial_update(request, *args, **kwargs)
#         return APIResponse(results=response.data)


class UserAPIView(ViewSet):


    def user_login(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer2(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = User.objects.filter(username=request.data['username'],password=request.data['password'])
        if user_obj:
            return APIResponse(200,"登录成功")
        else:
            return APIResponse(400,"登录失败")


    def get_user_count(self, request, *args, **kwargs):
        user_obj = User.objects.all()
        j = 0
        for i in user_obj:
            j += 1
        return APIResponse(200,f"查询完成共{j}个用户")

    def user_register(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        if user_obj:
            return APIResponse(200,"注册成功")
        else:
            return APIResponse(400,"注册失败")



