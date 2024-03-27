
from django.http import HttpResponse


def home(request):
    return HttpResponse(f"""Hello users  !!!  welcome to developers """)
