
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import (
    Banner,
    SchoolInfo,
    SchoolClass,
    Facility,
    ContactEnquiry,
)


def home(request):
    if request.method == 'POST':
        ContactEnquiry.objects.create(
            name=request.POST.get('name', '').strip(),
            email=request.POST.get('email', '').strip(),
            phone=request.POST.get('phone', '').strip(),
            subject=request.POST.get('subject', '').strip(),
            message=request.POST.get('message', '').strip(),
        )

        messages.success(
            request,
            'Thank you! Your enquiry has been submitted successfully.'
        )
        return redirect('school:home')

    context = {
        'banners': Banner.objects.filter(is_active=True),
        'school_info': SchoolInfo.objects.first(),
        'classes': SchoolClass.objects.filter(is_active=True),
        'facilities': Facility.objects.filter(is_active=True),
    }

    return render(request, 'school/home.html', context)
