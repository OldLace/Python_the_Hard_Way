#I got it... I think
from sys import argv

script, filename1, filename2 = argv
# txt = filename.read()

text_file1 = open(filename1)
info = text_file1.read()
# print(info)


text_file2 = open(filename2, 'w')
text_file2.write(info)
text_file2.close()
text_file2 = open(filename2, 'r')
info2 = text_file2.read()
# text_file2.write(info)
print(info2)


# filename2 = 




# script, file1, file2 = argv


# text_file2 = open(file2, 'w')
# text_file2.write(text_file)
# text_file2.close()
# text_file2 = open(file2)
# print(file2.read())



