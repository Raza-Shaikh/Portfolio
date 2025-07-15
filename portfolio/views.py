from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
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
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact message
            contact = form.save()

            # Send email notification (optional)
            try:
                send_mail(
                    subject=f'New Contact Form Submission: {contact.subject}',
                    message=f'''
                    New message from your portfolio website:

                    Name: {contact.name}
                    Email: {contact.email}
                    Subject: {contact.subject}

                    Message:
                    {contact.message}
                    ''',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                # Log the error but don't fail the form submission
                print(f"Email sending failed: {e}")

            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
