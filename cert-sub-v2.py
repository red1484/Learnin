# program for grabbing subdonains from cert.sh

import argparse
import json
from urllib.request import urlopen

parser = argparse.ArgumentParser(prog='cert.sh', description='grabs subdomains from cert.sh')
parser.add_argument('domain', help='domain to grab subdomains of "example.com"')
parser.add_argument('-o', '--output', help='save the ouput to a file')
args = parser.parse_args()

# inputs the domain argument to cert.sh
# with json output and coverts that to a list

url = "https://crt.sh/?q=" + args.domain + "&output=json"
page = urlopen(url)
json_bytes = page.read()
json_page = json_bytes.decode("utf-8")
site_dict = json.loads(json_page)

# iterates through the list of dictionaries and grabs the name value
site_list = []

for i in site_dict:
	site = i['name_value']
	if site not in site_list and site != None:
		site_list.append(site)

# saves the output to a txt file in the local directory or prints to 
# command line depending on -o flag
if args.output == None:
    for site in site_list:
        print(site)
else:
    output_txt = args.output
    with open(output_txt, 'w') as output_file:
	    for site in site_list:
		    output_file.write(site + '\n')

