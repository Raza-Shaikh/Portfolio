#!/usr/bin/env python
"""
Email Setup Helper Script
This script helps you set up Gmail SMTP for your portfolio contact form.
"""

import os
import sys

def setup_email():
    print("="*60)
    print("📧 GMAIL SMTP SETUP FOR PORTFOLIO CONTACT FORM")
    print("="*60)
    
    print("\n🔐 STEP 1: Get Gmail App Password")
    print("1. Go to: https://myaccount.google.com/")
    print("2. Click 'Security' → Enable '2-Step Verification'")
    print("3. Go to 'App passwords' → Generate password for 'Mail'")
    print("4. Copy the 16-character password (like: abcd efgh ijkl mnop)")
    
    print("\n📝 STEP 2: Enter Your App Password")
    app_password = input("Enter your Gmail App Password: ").strip()
    
    if not app_password:
        print("❌ No password entered. Exiting...")
        return
    
    # Remove spaces from app password
    app_password = app_password.replace(" ", "")
    
    print("\n⚙️ STEP 3: Setting up environment variable...")
    
    # For Windows
    if os.name == 'nt':
        # Set environment variable for current session
        os.environ['EMAIL_HOST_PASSWORD'] = app_password
        print(f"✅ Environment variable set for current session")
        
        # Create a batch file for permanent setup
        with open('set_email_env.bat', 'w') as f:
            f.write(f'@echo off\n')
            f.write(f'setx EMAIL_HOST_PASSWORD "{app_password}"\n')
            f.write(f'echo Environment variable set permanently!\n')
            f.write(f'pause\n')
        
        print("📁 Created 'set_email_env.bat' - run this file to set permanently")
    
    print("\n🧪 STEP 4: Testing email configuration...")
    
    # Test the email setup
    try:
        import django
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
        django.setup()
        
        from django.core.mail import send_mail
        from django.conf import settings
        
        # Test email
        send_mail(
            subject='Portfolio Contact Form - Test Email',
            message='This is a test email to verify your Gmail SMTP setup is working correctly!',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['raza.shaikh.work@gmail.com'],
            fail_silently=False,
        )
        
        print("✅ Test email sent successfully!")
        print("📬 Check your inbox at raza.shaikh.work@gmail.com")
        
    except Exception as e:
        print(f"❌ Email test failed: {e}")
        print("💡 Make sure your App Password is correct and 2-Step Verification is enabled")
    
    print("\n🚀 NEXT STEPS:")
    print("1. Check your Gmail inbox for the test email")
    print("2. If received, your contact form will now work!")
    print("3. Deploy your portfolio - contact form emails will come to you")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    setup_email()
