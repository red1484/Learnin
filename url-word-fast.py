from urllib.parse import urlparse, parse_qs



def url_parser(url):
    # breaks the url down and returns it in a dictionary
    parts = urlparse(url)
    direc = parts.path

    # breaks down the path into files and directories
    directories = []
    files = ''
    while len(direc) > 0:
        slash = direc.find('/')
        if slash != -1:
            temp_str = direc[0:slash+1]
            direc = direc.replace(temp_str, '', 1)
            directories.append(temp_str)
        elif slash == -1 and len(direc) > 0:
            temp_str = direc
            direc = direc.replace(temp_str, '', 1)
            files = temp_str
        else:
            print('WTF did i fubar')
            print(direc)
            print(files)
            direc = 0

    # breaks the queries down into a dictionary
    queries = parse_qs(parts.query, keep_blank_values=True)
    
    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'files': files,
        'queries': queries,
    }
    
    return elements

# ask the user for a clean url file to parse apart
user_prompt = input("Select a file to parse: ")
# user_prompt = 'mid_good.txt'

save_prompt = input('Save list as: ')
dir_prompt = save_prompt + '-dir-wordlist.txt'
sub_prompt =  save_prompt + '-sub-wordlist.txt'
file_prompt = save_prompt + '-file-wordlist.txt'
query_prompt = save_prompt + '-queries-wordlist.txt'
query_key_prompt = save_prompt + '-query-key-wordlist.txt'
query_value_prompt =  save_prompt + '-query-value-wordlist.txt'

user_file = open(user_prompt, 'r')
file_dir= open(dir_prompt, 'a')
file_sub = open(sub_prompt, 'a')
file_file = open(file_prompt, 'a')
file_query = open(query_prompt, 'a')
file_query_key = open(query_key_prompt, 'a')
file_query_value = open(query_value_prompt, 'a')


count = 1
for line in user_file:
    url = url_parser(line)
    for dir in url['directories']:
        clean = dir.strip('/')
        file_dir.write(clean + '\n')
            
    sub = url['netloc'].split('.')
    if len(sub) > 2:
        sub.pop()
        sub.pop()
        for item in sub:
            file_sub.write(item + '\n')
    elif len(sub) <= 2:
        print(f'something weird with line {count}')
        print(sub)
            
    path_file =  url['files']
    file_file.write(path_file + '\n')

    query =  url['queries']
    for x,y in query.items():
        combined = x + '=' + y[0]
        file_query.write(combined + '\n')
        file_query_key.write(x + '\n')
        file_query_value.write(y[0] + '\n')
    print(count, end='\r')
    count += 1

# for dir in dir_list:
#     print(dir)
# print('\n')
# print('-----------------------------------------------------------')


# for query in query_list:
#     print(query)   
user_file.close()
file_dir.close()
file_sub.close()
file_file.close()
file_query.close()
file_query_key.close()
file_query_value.close()