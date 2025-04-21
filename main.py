"""
Main entry point for extracting questions from PDF files
"""

from extractor import extract_questions


def main():
    # Example PDF path - replace with actual path
    # pdf_path = input("Enter the path to the PDF file: ")
    pdf_path = "cre_paper1_2022.pdf"

    try:
        questions = extract_questions(pdf_path)
        for question in questions:
            print("question", question)
    except Exception as e:
        print(f"Error extracting questions: {e}")


if __name__ == "__main__":
    main()
