from django.shortcuts import render

from django.http import  HttpResponse,HttpResponseRedirect

from django.core.mail import send_mail
from django.conf import settings

import mimetypes

import os
def vik(request):
    s="hello world"
    data={'s':s}
    return render(request,'home.html',context=data)

def gus(request):

    return render(request,'contact.html')


def emaill(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        subject=subject
        message=message
        email_from=settings.EMAIL_HOST_USER

        send_mail(
            subject,
            message,
            email_from,
            ['vikashgusain1999@gmail.com'],

        )

        return render(request,'contact.html')

    else:
        return render(request,'contact.html')




def download(request):
        filename='resume.pdf'
        # Define Django project base directory
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '\\pdf\\' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
