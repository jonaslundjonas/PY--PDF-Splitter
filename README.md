# PY--PDF-Splitter
Splits files to smaller files

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
