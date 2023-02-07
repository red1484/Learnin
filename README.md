# Learnin
<h3>some usefull scripts I have came up with wile learning python and bugbounty</h3>

<h3>cert-sub-v2.py</h3>
  <p>
  updated version of certsubd.py to grab donains from cert.sh
  that takes arguments from comand line
  <br>
  example: python3 cert-sub-v2.py [example.com] -o [output file]
  </p>
  

<h3>certsubd.py</h3>
  <p>
  asks user a domain to search( example.com ) then inputs
  that into crt.sh with json output and coverts that to a file
  </p>
  
<h3>checkurl.py</h3>
  <p>
  Asks user for an input text file of urls separated by line
  and checks that they are valid url format.
  Outputs the results in two files based on a userinputed name
  with Good.txt and Bad.txt added to the chosen name.
  Only works with urls that include a scheme(ex. http://, https://, ftp://).
  </p>
  
<h3>scope.py</h3>
  <p>
  Uses a scope file(lines of domains) to check if url domains are in scope
  outputs the results to two saved files name + Ins.txt and Oos.txt.
  if scope is something like *.example.com just putting .example.com should work
  </p>
  
<h3>timer.py</h3>
  <p>
  study or workout timer program. Can use it to make a number of different timers and then repeat them
  a number of times. Also lets you save timers and load previous timers frome files.
  examples - task1 x min task2 x min task 3 xmin ect.. repeat n times, 
  workout run 5 min walk 1 min repeat 5 times, study 50 min break 10 min repeat x times.
  </p>
  
<h3>url-word-fast.py</h3>
  <p>
  takes a list of urls and breaks them down into subdomains, directories, files, parameters, parameter keys, and parameter values.
  </p>
  
<h3>url-wordlist.py</h3>
  <p>
  slower version of the url-word-fast.py but sorts all the results to eliminate duplicates. do not use on very large list. faster to use
  the fast one then just sort -u the files afterward
  </p>
