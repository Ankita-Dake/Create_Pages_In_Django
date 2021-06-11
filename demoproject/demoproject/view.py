from django.http import HttpResponse


def Home(request):
    return HttpResponse('<h1 style="text-align:center; color:red; padding:50px;"> Hello from Django . This is Home '
                        'page</h1>')


def about(request):
    return HttpResponse('<h1 style="text-align:center; color:blue; padding:50px;"> This is About Page</h1>')


def contact(request):
    return HttpResponse('<h1 style="text-align:center; color:black; padding:50px;"> This is Contact Page</h1>')


def login(request):
    return HttpResponse('<h1 style="text-align:center; color:purple; padding:50px;"> This is Login Page</h1>')


def registration(request):
    return HttpResponse('<h1 style="text-align:center; color:pink; padding:50px;"> This is Contact Page</h1>')


def feedback(request):
    return HttpResponse('<h1 style="text-align:center; color:brown; padding:50px;"> This is Feedback Page</h1>')


def gallery(request):
    return HttpResponse('<h1 style="text-align:center; color:green; padding:50px;"> This is Gallery Page</h1>')


def info(request):
    return HttpResponse('<h1 style="text-align:center; color:orange; padding:50px;"> This is Info Page</h1>')


def form(request):
    return HttpResponse('<h1 style="text-align:center; color:gray; padding:50px;"> This is Form Page</h1>')


def logout(request):
    return HttpResponse('<h1 style="text-align:center; color:blue; padding:50px;"> This is Logout Page</h1>')
