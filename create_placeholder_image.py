#!/usr/bin/env python
"""
Create a placeholder profile image
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image():
    """Create a professional placeholder image"""
    # Create a 400x400 image with a professional background
    size = (400, 400)
    
    # Professional blue gradient background
    img = Image.new('RGB', size, color='#2563eb')
    draw = ImageDraw.Draw(img)
    
    # Create gradient effect
    for y in range(size[1]):
        # Gradient from blue to darker blue
        color_value = int(37 + (99 - 37) * (y / size[1]))  # From #2563eb to #1d4ed8
        color = f'#{color_value:02x}{99:02x}{235:02x}'
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Add initials "MR" in the center
    try:
        # Try to use a nice font
        font_size = 120
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()
    
    # Draw initials
    text = "MR"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Add text shadow
    draw.text((x+2, y+2), text, font=font, fill=(0, 0, 0, 80))
    # Add main text
    draw.text((x, y), text, font=font, fill='white')

    # Add a subtle border
    draw.rectangle([0, 0, size[0]-1, size[1]-1], outline=(255, 255, 255, 50), width=3)
    
    # Save the image
    output_path = 'static/images/profile.jpg'
    img.save(output_path, 'JPEG', quality=95)
    print(f"✅ Placeholder image created: {output_path}")
    print("📝 Replace this with your actual profile image when ready!")

if __name__ == "__main__":
    create_placeholder_image()
