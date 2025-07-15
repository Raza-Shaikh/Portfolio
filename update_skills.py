#!/usr/bin/env python
"""
Update Skills Script
Updates the portfolio skills to reflect only the technologies you actually know
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Skill

def update_skills():
    """Update skills to reflect actual knowledge"""
    print("🔄 Updating skills to reflect your actual knowledge...")
    
    # Clear existing skills
    Skill.objects.all().delete()
    print("✅ Cleared existing skills")
    
    # Your actual skills with appropriate proficiency levels and categories
    actual_skills = [
        # Backend
        {'name': 'Python', 'category': 'backend', 'proficiency': 85, 'icon': 'fab fa-python'},
        {'name': 'Django', 'category': 'backend', 'proficiency': 80, 'icon': 'fab fa-python'},
        {'name': 'Flask', 'category': 'backend', 'proficiency': 75, 'icon': 'fab fa-python'},
        {'name': 'REST API', 'category': 'backend', 'proficiency': 80, 'icon': 'fas fa-exchange-alt'},
        
        # Database
        {'name': 'MySQL', 'category': 'database', 'proficiency': 75, 'icon': 'fas fa-database'},
        
        # Frontend
        {'name': 'HTML5', 'category': 'frontend', 'proficiency': 85, 'icon': 'fab fa-html5'},
        {'name': 'CSS3', 'category': 'frontend', 'proficiency': 80, 'icon': 'fab fa-css3-alt'},
        {'name': 'JavaScript', 'category': 'frontend', 'proficiency': 70, 'icon': 'fab fa-js-square'},
        
        # Tools
        {'name': 'Git', 'category': 'tools', 'proficiency': 80, 'icon': 'fab fa-git-alt'},
        {'name': 'GitHub', 'category': 'tools', 'proficiency': 80, 'icon': 'fab fa-github'},
        {'name': 'Postman', 'category': 'tools', 'proficiency': 75, 'icon': 'fas fa-paper-plane'},
    ]
    
    # Create new skills
    created_skills = []
    for skill_data in actual_skills:
        skill = Skill.objects.create(**skill_data)
        created_skills.append(skill)
        print(f"✅ Added: {skill.name} ({skill.proficiency}%) - {skill.category}")
    
    print(f"\n🎉 Successfully updated {len(created_skills)} skills!")
    
    # Display summary by category
    print("\n📊 Skills Summary:")
    categories = ['backend', 'frontend', 'database', 'tools']
    
    for category in categories:
        skills = Skill.objects.filter(category=category)
        if skills:
            print(f"\n{category.upper()}:")
            for skill in skills:
                print(f"  • {skill.name} ({skill.proficiency}%)")

if __name__ == "__main__":
    update_skills()
