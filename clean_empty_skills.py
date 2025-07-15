#!/usr/bin/env python
"""
Simple script to clean empty skills from the database
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
django.setup()

from portfolio.models import Skill

def clean_empty_skills():
    """Remove empty or invalid skills"""
    print("=== Cleaning Empty Skills ===")

    # First, let's see all skills by category
    all_skills = Skill.objects.all()
    print(f"Total skills in database: {all_skills.count()}")

    categories = ['backend', 'frontend', 'database', 'tools', 'other']
    for category in categories:
        skills_in_category = all_skills.filter(category=category)
        print(f"\n{category.upper()} ({skills_in_category.count()} skills):")
        for skill in skills_in_category:
            print(f"  • ID: {skill.id}, Name: '{skill.name}', Length: {len(skill.name)}")

    # Find skills with empty names or just whitespace
    empty_skills = []
    for skill in all_skills:
        if not skill.name or skill.name.strip() == '':
            empty_skills.append(skill)

    if empty_skills:
        print(f"\nFound {len(empty_skills)} empty skill(s):")
        for skill in empty_skills:
            print(f"  • ID: {skill.id}, Name: '{skill.name}', Category: {skill.category}")

        # Delete the empty skills
        for skill in empty_skills:
            skill.delete()
        print(f"✅ Deleted {len(empty_skills)} empty skill(s)")
    else:
        print("\n✅ No empty skills found")

    # Check if there are any skills in 'other' category
    other_skills = all_skills.filter(category='other')
    if other_skills.exists():
        print(f"\n⚠️  Found {other_skills.count()} skill(s) in 'other' category:")
        for skill in other_skills:
            print(f"  • ID: {skill.id}, Name: '{skill.name}'")
    else:
        print("\n✅ No skills in 'other' category")

if __name__ == "__main__":
    clean_empty_skills()
