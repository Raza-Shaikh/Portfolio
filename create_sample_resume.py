#!/usr/bin/env python
"""
Create a sample resume PDF file for testing
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_sample_resume():
    """Create a sample resume PDF"""
    
    # Create the resume directory if it doesn't exist
    resume_dir = os.path.join('static', 'resume')
    os.makedirs(resume_dir, exist_ok=True)
    
    # Define the output file path
    output_path = os.path.join(resume_dir, 'Mohd_Raza_Amin_Shaikh_Resume.pdf')
    
    # Create the PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=30,
        alignment=1  # Center alignment
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=12,
        textColor='blue'
    )
    
    # Content
    content = []
    
    # Header
    content.append(Paragraph("Mohd Raza Amin Shaikh", title_style))
    content.append(Paragraph("Python/Django Developer", styles['Normal']))
    content.append(Paragraph("Phone: +91 8108426690 | Email: raza.shaikh.work@gmail.com", styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Professional Summary
    content.append(Paragraph("Professional Summary", heading_style))
    content.append(Paragraph("Passionate Python/Django developer with expertise in building robust, scalable web applications. Experienced in creating efficient solutions and delivering exceptional user experiences.", styles['Normal']))
    content.append(Spacer(1, 15))
    
    # Technical Skills
    content.append(Paragraph("Technical Skills", heading_style))
    content.append(Paragraph("<b>Backend:</b> Python, Django, REST API, Flask", styles['Normal']))
    content.append(Paragraph("<b>Frontend:</b> HTML5, CSS3, JavaScript", styles['Normal']))
    content.append(Paragraph("<b>Database:</b> MySQL", styles['Normal']))
    content.append(Paragraph("<b>Tools:</b> Git, GitHub, Postman", styles['Normal']))
    content.append(Spacer(1, 15))
    
    # Projects
    content.append(Paragraph("Featured Projects", heading_style))
    content.append(Paragraph("<b>E-commerce Store</b>", styles['Normal']))
    content.append(Paragraph("A functional e-commerce store built with Django, featuring product catalog, shopping cart, and user authentication.", styles['Normal']))
    content.append(Spacer(1, 10))
    
    content.append(Paragraph("<b>Plagiarism Checker</b>", styles['Normal']))
    content.append(Paragraph("A web-based plagiarism checker built using Flask and Scikit-learn. Upload documents and instantly see similarity percentage.", styles['Normal']))
    content.append(Spacer(1, 15))
    
    # Footer
    content.append(Spacer(1, 30))
    content.append(Paragraph("This is a sample resume generated for portfolio demonstration.", styles['Normal']))
    
    # Build the PDF
    doc.build(content)
    print(f"✅ Sample resume created: {output_path}")

if __name__ == "__main__":
    try:
        create_sample_resume()
    except ImportError:
        print("❌ ReportLab not installed. Installing...")
        import subprocess
        subprocess.run(["pip", "install", "reportlab"])
        create_sample_resume()
