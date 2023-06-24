from django.shortcuts import render
from .models import Contact

from .models import music,bharatanatyam,keyboard,guitar,kuchipudi,westerndance,video
# Create your views here.

def Home(request):
	return render(request,'App/home.html')

def About_us(request):
	return render(request,'App/about_us.html')

def Contact_us(request):
	if request.method == "POST":
		name = request.POST['name']
		mobile = request.POST['mobile']
		email = request.POST['email']
		message = request.POST['message']
		contact = Contact(name=name, email=email, mobile=mobile, message=message)
		contact.save()
	return render(request, "App/contact_us.html")

def Gallery(request):
	return render(request,'App/gallery.html')

def Courses(request):
	return render(request,'App/courses.html')

def Staff(request):
	return render(request,'App/staff.html')

# ________________________________________________________
def bharatanatyamview(request):
	images = bharatanatyam.objects.all()
	context = {
        'images': images,
    }
	return render(request,'App/gallery/bhar2.html',context)

def musicview(request):
	images = music.objects.all()
	context = {
        'images': images,
	}
	return render(request,'App/gallery/music.html',context)

def westerndanceview(request):
    images = westerndance.objects.all()
    context = {
        'images': images,
    }
    return render(request,'App/gallery/westerndance.html',context)


def kuchipudiview(request):
    images = kuchipudi.objects.all()
    context = {
        'images': images,
    }
    return render(request,'App/gallery/kuchipudi.html',context)

def guitarview(request):
    images = guitar.objects.all()
    context = {
        'images': images,
    }
    return render(request,'App/gallery/guitar.html',context)
def keyboardview(request):
    images = keyboard.objects.all()
    context = {
        'images': images,
    }
    return render(request,'App/gallery/keyboard.html',context)

def videoview(req):
    videos=video.objects.all()
    return render(req,'App/gallery/video.html',{"videos":videos})