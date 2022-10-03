# Asks user for an input text file of urls separated by line
# and checks that they are valid url format.
# Outputs the results in two files based on a userinputed name
# with Good.txt and Bad.txt added to the chosen name.
# Only works with urls that include a scheme(ex. http://, https://, ftp://).

# Must include the validators package(pip3 install validators).
import validators


file_to_read = input('Select a file to validate: ')
name_of_output = input('Seclect name of output files: ')

file_one = open(file_to_read, 'r')
file_good = open(name_of_output + 'Good.txt', 'a')
file_bad = open(name_of_output + 'Bad.txt', 'a')

line_count = 0
bad_count = 0
good_count = 0

for line in file_one:
    line_count += 1
    if not validators.url(line):
        file_bad.write(line)
        bad_count += 1
        print(f'Bad url found at line {line_count}')
    elif validators.url(line):
        file_good.write(line)
        good_count += 1

file_one.close()
file_good.close()
file_bad.close()

print(f'Bad total: {bad_count}')
print(f'Good total: {good_count}')