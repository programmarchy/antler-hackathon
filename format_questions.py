import re

def format_questions(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content into questions
    questions = re.split(r'\d+\)', content)[1:]

    formatted_questions = []
    for i, question in enumerate(questions, 1):
        # Split question into text and answers
        parts = question.strip().split('\n\n', 1)
        if len(parts) < 2:
            continue

        question_text, answers = parts
        question_text = question_text.replace('\n', ' ').strip()

        # Format answers
        answers = re.findall(r'([A-D]\..*?)(?=[A-D]\.|$)', answers, re.DOTALL)
        formatted_answers = [answer.replace('\n', ' ').strip() for answer in answers]

        # Combine formatted question and answers
        formatted_question = f"{i}) {question_text}\n\n"
        formatted_question += '\n'.join(formatted_answers)
        formatted_questions.append(formatted_question)

    # Write formatted questions to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(formatted_questions))

# Usage
input_file = 'data/Practice-Questions-100.md'
output_file = 'data/Practice-Questions-100-Formatted.md'
format_questions(input_file, output_file)