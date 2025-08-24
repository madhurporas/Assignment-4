try:
    file = open('sample.txt','r')
    file1= file.readline().strip()
    file2= file.readline()
    print('Reading file content: ')
    print('Line 1: ',file1)
    print('Line 2: ',file2)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")