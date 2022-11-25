from django.shortcuts import render


def admin_detail(request):
    return render(request, "pages/admin_detail.html")

def admin_staff(request):
    return render(request, "pages/admin_staff.html")

def admin_user(request):
    return render(request, "pages/admin_user.html")

def admin_login(req):
    return render(req,'pages/admin_login.html')
