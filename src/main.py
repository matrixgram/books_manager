#!/usr/bin/env python3
import sys
import pdfplumber
import regex


def extract_ISBN(pdf_path):
    """Find ISBN13"""
    pattern = "\d{3}-\d-\d{3}-\d{5}-\d" "|" "\d{3}-\d-\d{5}-\d{3}-\d"
    pdf = pdfplumber.open(pdf_path)
    isbn = None
    for p in pdf.pages:
        if p.extract_text():
            isbn = regex.findall(pattern, p.extract_text())
            if isbn:
                break
    return isbn


if __name__ == "__main__":
    print(extract_ISBN(sys.argv[1]))
