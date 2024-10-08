import re
import csv

def format_questions_to_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content into questions
    questions = re.split(r'\d+\)', content)[1:]

    csv_data = []
    for question in questions:
        # Split question into text and answers
        parts = question.strip().split('\n\n', 1)
        if len(parts) < 2:
            continue

        question_text, answers = parts
        question_text = question_text.replace('\n', ' ').strip()

        # Format answers
        answers = re.findall(r'([A-D])\.\s*(.*?)(?=[A-D]\.|$)', answers, re.DOTALL)
        formatted_answers = {letter: answer.replace('\n', ' ').strip() for letter, answer in answers}

        # Prepare CSV row
        csv_row = [
            question_text,
            formatted_answers.get('A', ''),
            formatted_answers.get('B', ''),
            formatted_answers.get('C', ''),
            formatted_answers.get('D', '')
        ]
        csv_data.append(csv_row)

    # Write formatted questions to CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Multiple Choice Question', 'A', 'B', 'C', 'D'])
        writer.writerows(csv_data)

# Usage
input_file = 'data/Practice-Questions-100-Formatted.md'
output_file = 'data/Practice-Questions-100.csv'
format_questions_to_csv(input_file, output_file)