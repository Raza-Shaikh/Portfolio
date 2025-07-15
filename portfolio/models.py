from django.db import models
from django.urls import reverse
from django.utils import timezone


class Skill(models.Model):
    """Model for skills/technologies"""
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        default=50,
        help_text="Proficiency level (0-100%)"
    )
    category = models.CharField(
        max_length=50,
        choices=[
            ('frontend', 'Frontend'),
            ('backend', 'Backend'),
            ('database', 'Database'),
            ('tools', 'Tools & Technologies'),
            ('other', 'Other'),
        ],
        default='other'
    )
    icon = models.CharField(max_length=50, blank=True, help_text="CSS class for icon (e.g., fab fa-python)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', '-proficiency', 'name']

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, help_text="Brief description for project cards")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Skill, blank=True, related_name='projects')
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    completed_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-featured', '-completed_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'pk': self.pk})


class Experience(models.Model):
    """Model for work experience"""
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if current position")
    location = models.CharField(max_length=100, blank=True)
    company_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

    @property
    def is_current(self):
        return self.end_date is None


class Education(models.Model):
    """Model for education"""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Contact(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
