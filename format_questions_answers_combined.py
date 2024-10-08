import csv

input_file = 'data/Practice-Questions-Answers-Combined-100.csv'
output_file = 'data/Data-Set-Practice-Questions-Answers.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Write the header
    writer.writerow(['Combined Question', 'Answer', 'Answer Text', 'Explanation'])
    
    # Skip the header row of the input file
    next(reader)
    
    for row in reader:
        combined_question = f"{row[0]}\nA) {row[1]}\nB) {row[2]}\nC) {row[3]}\nD) {row[4]}"
        writer.writerow([combined_question] + row[5:])

print(f"Combined questions have been written to {output_file}")