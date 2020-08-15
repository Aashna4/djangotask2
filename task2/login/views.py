from django.shortcuts import render,redirect
from .models import userinfo

def index(request):
    if request.method == 'POST' :
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        ph_no = request.POST['phno']
        email = request.POST['email']
        gender = request.POST['gender']

        profile= userinfo(f_name=f_name, l_name=l_name, ph_no=ph_no, email=email, gender=gender)
        profile.save()

        return redirect('index')
    else:
        return render(request, 'login/p1.html')

def check(request):
    if request.method == 'POST' :
        email = request.POST['email']

        try: 
            profile = userinfo.objects.get(email=email)
            return render(request, 'login/p3.html', {'message':'Found User!', 'profile': profile})
        except userinfo.DoesNotExist:
            return render(request, 'login/p3.html', {'message': 'Could not find user with', 'email':email})

    else :
        return render(request, 'login/p2.html')