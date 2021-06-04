from django.http import response
from django.shortcuts import redirect

# class AuthMiddleware():
#     def 


def authmiddleware(get_response):
    print("----------------------------middleware-start---------------------------")
    def middleware(request):
        print("---------------------",request.session.get('name'))
        if not request.session.get('name'):
            return redirect('login')
       
        response = get_response(request)
        print("-----------------------------------=>after view")
        return response

    return middleware