import csv
import re

def format_answers_to_csv(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Split the content into individual questions
    questions = re.split(r'\n\n', content)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Answer', 'Answer Text', 'Explanation'])

        i = 1

        for question in questions:
            # Skip empty lines
            if not question.strip():
                continue

            # Extract answer, answer text, and explanation
            parts = question.split(')', 1)
            if len(parts) > 1:
                question_number = parts[0].strip()
                
                if str(i) != question_number:
                    print(f"Question number mismatch: {i} != {question_number}")
                    print(question)
                    exit()

                i += 1

                rest = parts[1].strip()
                
                answer_parts = rest.split('/', 1)
                if len(answer_parts) > 1:
                    answer = answer_parts[0].strip()
                    rest = answer_parts[1].strip()
                    
                    text_parts = rest.split('|', 1)
                    if len(text_parts) > 1:
                        answer_text = text_parts[0].strip()
                        explanation = text_parts[1].strip()
                        
                        writer.writerow([answer, answer_text, explanation])
                    else:
                        print(f"No answer text found for question {question_number}")
                        print(question)
                else:
                    print(f"No answer found for question {question_number}")
                    print(question)
            else:
                print(f"Invalid question format: {question}")

# Usage
format_answers_to_csv('data/Practice-Questions-Answers-100.md', 'data/Practice-Questions-Answers-100.csv')
