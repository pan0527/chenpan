from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # print(request.headers.get("User-Agent")) #python-requests/2.22.0
        return self.get_response(request)

    def process_response(self, request, response):
        # print("处理了响应")
        # response.set_cookie("name","xdc")
        # return response
        # 访问所有页面响应都是helloworld
        ua=request.headers.get("User-Agent")
        if ua.__contains__("python"):
            return HttpResponse("非法请求")
        else:
            return response

