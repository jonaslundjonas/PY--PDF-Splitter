"""
PDF Splitter Script
Written by Jonas Lund 2024

Description:
This script splits a PDF file into multiple smaller PDF files of approximately equal size.
The script will automatically detect all PDF files in the same directory where this script is located
and let you choose which one to split.

Requirements:
- Python 3.6 or higher
- PyPDF2 library (install using: pip install PyPDF2)

How to use:
1. Place this script in the same folder as your PDF file(s)
2. Run the script (python pdf_splitter.py)
3. Select which PDF to split from the listed files
4. Enter the number of pieces you want to split the PDF into
5. The script will create a new folder called 'split_pdfs' and save the split files there

Output:
- Creates a new folder called 'split_pdfs'
- Splits the PDF into the specified number of parts
- Names the files as: original_part_1.pdf, original_part_2.pdf, etc.
- Original file remains unchanged
- Displays which pages are included in each split file

Note: Make sure you have write permissions in the directory where you run this script.
"""

import os
from PyPDF2 import PdfReader, PdfWriter
import math

def get_pdf_files():
    """Get all PDF files in the script's directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_files = [f for f in os.listdir(script_dir) if f.lower().endswith('.pdf')]
    return pdf_files, script_dir

def split_pdf(input_path, num_pieces):
    """
    Split a PDF into a specified number of approximately equal pieces.
    
    Args:
        input_path (str): Path to the input PDF file
        num_pieces (int): Number of pieces to split the PDF into
    """
    # Create output directory if it doesn't exist
    output_dir = 'split_pdfs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Read the PDF
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)  # Fixed: Using reader.pages instead of reader
    
    # Calculate pages per piece (rounded up)
    pages_per_piece = math.ceil(total_pages / num_pieces)
    
    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(input_path))[0]
    
    print(f"\nSplitting {base_filename}.pdf ({total_pages} pages) into {num_pieces} parts...")
    
    # Split the PDF
    for i in range(num_pieces):
        writer = PdfWriter()
        
        # Calculate start and end pages for this piece
        start_page = i * pages_per_piece
        end_page = min((i + 1) * pages_per_piece, total_pages)
        
        # Add pages to the writer
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])
        
        # Save the output file
        output_filename = f"{base_filename}_part_{i+1}.pdf"
        output_path = os.path.join(output_dir, output_filename)
        
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        print(f"Created: {output_filename} (Pages {start_page + 1}-{end_page})")

def main():
    # Get all PDF files in the directory
    pdf_files, script_dir = get_pdf_files()
    
    if not pdf_files:
        print("No PDF files found in the script's directory!")
        return
    
    # Print available PDFs
    print("\nAvailable PDF files:")
    for i, pdf in enumerate(pdf_files, 1):
        reader = PdfReader(os.path.join(script_dir, pdf))
        print(f"{i}. {pdf} ({len(reader.pages)} pages)")  # Fixed: Using reader.pages
    
    # Get number of pieces
    while True:
        try:
            num_pieces = int(input("\nEnter the number of pieces to split the PDF into: "))
            if num_pieces > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Process each PDF in the directory
    for pdf_file in pdf_files:
        try:
            input_path = os.path.join(script_dir, pdf_file)
            split_pdf(input_path, num_pieces)
        except Exception as e:
            print(f"An error occurred processing {pdf_file}: {str(e)}")
    
    print("\nPDF splitting completed successfully!")
    print(f"Split files can be found in the 'split_pdfs' directory")

if __name__ == "__main__":
    main()
