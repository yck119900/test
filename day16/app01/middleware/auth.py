from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info=='/login/':
            return

        # 1.读取当前访问用户的session信息，如果能读到，说明已登陆过，就可以继续向后走
        info_dict = request.session.get('info')
        if info_dict:
            return
        return redirect('/login/')
