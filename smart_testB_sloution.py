import os #for operating system module
path = input("please write your path: ")   # if not working please add two backslash (\\) instead of (\)
#'D:\\D\\smartpeep_test\\Test B\\testcase2'
#'D:\\D\\smartpeep_test\\Test B\\testcase1'

file_names = []         #containing the names of files 
files_content = []      #containing the numbers in the text files
output_name = ''        #the output file name (team/friend)

for directory_path, dirnames, files in os.walk(path): #getting the path and files into the subdirectories
    
    for f in files:
        if f.endswith(".txt"):
            splitted = f.split('.',1)
            file_names.append(splitted[0])

            read_num = open(os.path.join(directory_path, f), 'r')   #reading the text files
            files_content.append(int(read_num.readline()))

zipped = zip(file_names, files_content)

zip_list =list(zipped)
sorted_files = sorted(zip_list, key= lambda x: x[1] )   #sorting the files

for i,x in sorted_files:        #joining the letters together into one word
    output_name = output_name + str(i)

print(output_name)

