import os
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from PIL import Image

def create_pdf():
    images = [file for file in os.listdir() if file.endswith(('jpg', 'jpeg', 'png'))]
    if not images:
        print("No images found in the directory.")
        return
    
    pdf_file = "images.pdf"
    c = canvas.Canvas(pdf_file)

    for image in images:
        try:
            img = Image.open(image)
            width, height = img.size
            c.setPageSize((width, height))
            c.drawImage(image, 0, 0, width, height)
            c.showPage()
            print(f"Added {image} to PDF.")
        except Exception as e:
            print(f"Error processing {image}: {e}")
    
    c.save()
    print(f"PDF created successfully: {pdf_file}")

if __name__ == "__main__":
    create_pdf()
