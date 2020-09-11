from django.shortcuts import render, get_object_or_404
from subjects.models import Subject, SubjectVideo
from subjects.filters import OrderFilter

# Create your views here.
def subjectPage(request):
    allSubject = Subject.objects.all()

    # search filter = https://www.youtube.com/watch?v=G-Rct7Na0UQ
    Myfilter = OrderFilter(request.GET,queryset=allSubject)
    allSubject = Myfilter.qs

    context = {
        'subject':allSubject,
        'filterSub':Myfilter,
    }
    return render(request,'subjects/subject.html',context)

def messagePage(request):
    return render(request,'subjects/message.html')

def videoPage(request,id):
    video = get_object_or_404(SubjectVideo, pk=id)
    context = {
        'video':video,
    }

    return render(request, "subjects/video.html", context)