import json
from urllib.request import urlopen


# asks user a domain to search( example.com ) then inputs
# that into crt.sh with json output and coverts that to a list

input_directory = input("domain to search:")

url = "https://crt.sh/?q=" + input_directory + "&output=json"
page = urlopen(url)
json_bytes = page.read()
json_page = json_bytes.decode("utf-8")
site_dict = json.loads(json_page)


# comment out above and uncomment below section to use with a
# saved json file from crt.sh

# input_path = input("path to json file: ")
# with open(input_path,'r') as myfile:
# 	data =myfile.read()
# site_dict = json.loads(data)


# iterates through the list of dictionaries and grabs the name value
site_list = []

for i in site_dict:
	site = i['name_value']
	if site not in site_list and site != None:
		site_list.append(site)

# saves the output to a txt file in the local directory
output_txt = input("name of file to save:") + ".txt"

with open(output_txt, 'w') as output_file:
	for site in site_list:
		output_file.write(site + '\n')




