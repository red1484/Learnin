# Uses a scope file(lines of domains) to check if url domains are in scope
# outputs the results to two saved files name + Ins.txt and Oos.txt.
# if scope is something like *.example.com just putting .example.com should work


raw_file = input('Name of file to check: ')
scope_file = input('Name of scope file: ')
save_file = input('Name of files to save: ')

file_raw = open(raw_file, 'r')
file_scope = open(scope_file, 'r')
# Had to convert the scope file to a list to get it to work otherwise
# running after first loop through scope file.
scope_list = file_scope.readlines()
file_ins= open(save_file + 'Ins.txt', 'a')
file_oos = open(save_file + 'Oos.txt', 'a')

# Strip the newline from both or otherise will not work for string matching
for line in file_raw:
    sl = line.strip("\n")
    in_scope = None
  
    for scope in scope_list:
        ss = scope.strip("\n")
       
        if sl.find(ss) >= 0:
            in_scope = True
            break
        elif sl.find(ss) < 0:
            in_scope = False
      
    if in_scope == True:
        file_ins.write(line)
    elif in_scope == False:
        file_oos.write(line)
