from django.shortcuts import render_to_response


def home_view(request):
    return render_to_response("CM_main/home.html")

def about_view(request):
    return render_to_response("CM_main/about.html")
