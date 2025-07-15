#!/usr/bin/env python
"""
Portfolio Management Script
A helper script to quickly add/update portfolio content
"""

import os
import sys
import django
from datetime import date

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Skill, Project, Experience, Education

def add_skill():
    """Add a new skill"""
    print("\n=== Add New Skill ===")
    name = input("Skill name: ")
    category = input("Category (backend/frontend/database/tools/other): ")
    proficiency = int(input("Proficiency (0-100): "))
    icon = input("Font Awesome icon class (optional): ")
    
    skill = Skill.objects.create(
        name=name,
        category=category,
        proficiency=proficiency,
        icon=icon
    )
    print(f"✅ Added skill: {skill.name}")

def add_project():
    """Add a new project"""
    print("\n=== Add New Project ===")
    title = input("Project title: ")
    short_desc = input("Short description: ")
    description = input("Full description: ")
    github_url = input("GitHub URL: ")
    live_url = input("Live URL (optional): ")
    featured = input("Featured project? (y/n): ").lower() == 'y'
    
    project = Project.objects.create(
        title=title,
        short_description=short_desc,
        description=description,
        github_url=github_url,
        live_url=live_url if live_url else None,
        featured=featured,
        completed_date=date.today()
    )
    
    # Add technologies
    print("\nAvailable skills:")
    skills = Skill.objects.all()
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill.name}")
    
    tech_indices = input("Enter skill numbers (comma-separated): ").split(',')
    for index in tech_indices:
        try:
            skill = skills[int(index.strip()) - 1]
            project.technologies.add(skill)
        except (ValueError, IndexError):
            continue
    
    print(f"✅ Added project: {project.title}")

def list_projects():
    """List all projects"""
    print("\n=== Your Projects ===")
    projects = Project.objects.all()
    for project in projects:
        status = "⭐ Featured" if project.featured else "📄 Regular"
        print(f"{status} {project.title}")
        print(f"   Technologies: {', '.join([t.name for t in project.technologies.all()])}")
        print(f"   GitHub: {project.github_url}")
        if project.live_url:
            print(f"   Live: {project.live_url}")
        print()

def list_skills():
    """List all skills by category"""
    print("\n=== Your Skills ===")
    categories = ['backend', 'frontend', 'database', 'tools', 'other']
    
    for category in categories:
        skills = Skill.objects.filter(category=category)
        if skills:
            print(f"\n{category.upper()}:")
            for skill in skills:
                print(f"  • {skill.name} ({skill.proficiency}%)")

def main():
    """Main menu"""
    while True:
        print("\n" + "="*50)
        print("🚀 PORTFOLIO MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add new skill")
        print("2. Add new project")
        print("3. List all projects")
        print("4. List all skills")
        print("5. Exit")
        print("-"*50)
        
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_skill()
        elif choice == '2':
            add_project()
        elif choice == '3':
            list_projects()
        elif choice == '4':
            list_skills()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
