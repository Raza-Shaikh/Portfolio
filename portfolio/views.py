from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, Http404
from django.utils.encoding import smart_str
import os
import mimetypes
from .models import Project, Skill, Experience, Education, Contact
from .forms import ContactForm


def home_view(request):
    """Home page view with featured projects and skills"""
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()

    context = {
        'featured_projects': featured_projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)


def about_view(request):
    """About page view with experience, education, and skills"""
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()

    context = {
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


class ProjectListView(ListView):
    """Projects page view with pagination"""
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6
    ordering = ['-featured', '-completed_date']


class ProjectDetailView(DetailView):
    """Individual project detail view"""
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'


def contact_view(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        # Get form data directly
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Basic validation
        if name and email and subject and message:
            try:
                # Save to database
                contact = Contact.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )

                # Send email notification
                send_mail(
                    subject=f'New Contact Form Submission: {subject}',
                    message=f'''
New message from your portfolio website:

Name: {name}
Email: {email}
Subject: {subject}

Message:
{message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['raza.shaikh.work@gmail.com'],
                    fail_silently=False,
                )

                messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
                return redirect('portfolio:contact')

            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
        else:
            messages.error(request, 'Please fill in all required fields.')

    # For GET requests, create a new form
    form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})


def download_resume(request):
    """Download resume file"""
    # Define the resume file path
    resume_filename = 'Mohd_Raza_Amin_Shaikh_Resume.pdf'
    resume_path = os.path.join(settings.STATIC_ROOT or os.path.join(settings.BASE_DIR, 'static'), 'resume', resume_filename)

    # Check if file exists
    if not os.path.exists(resume_path):
        # If STATIC_ROOT doesn't work, try the development static path
        resume_path = os.path.join(settings.BASE_DIR, 'static', 'resume', resume_filename)
        if not os.path.exists(resume_path):
            raise Http404("Resume file not found")

    # Get the file's content type
    content_type, _ = mimetypes.guess_type(resume_path)
    if content_type is None:
        content_type = 'application/octet-stream'

    # Open and read the file
    with open(resume_path, 'rb') as resume_file:
        response = HttpResponse(resume_file.read(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{smart_str(resume_filename)}"'
        return response



