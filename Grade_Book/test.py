# delete_word = "john"
# with open('students.txt') as open_students, open('words_cleaned.txt', 'wt') as write_students:
#     list(write_students.write(line) for line in open_students if line.rstrip() != delete_word)


delete_word = 'john'
with open('students.txt') as fin, open('words_cleaned.txt', 'wt') as fout:
    list(fout.write(line) for line in fin if line.rstrip() != delete_word)