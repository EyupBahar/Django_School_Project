from django.shortcuts import render
from .forms import ContactForm
from .models import Teacher
# Create your views here.


def home(request):
    teacher = Teacher.objects.order_by('speciality').distinct()

    if request.method == "POST":
        form = ContactForm(request.POST or None)

        if form.is_valid():
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form,
        'teachers': teacher
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def teacher(request):
    teacher = Teacher.objects.all()
    context = {

        'teachers': teacher

    }
    return render(request, 'teacher.html', context)
