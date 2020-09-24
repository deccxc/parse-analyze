#This portion of the code retrieves the log file from a network and saves a cached copy
from urllib.request import urlretrieve
import re

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
total_requests = 0
year_count = 0

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE);
#-------------------------------------------------------------------------------------------------
#This portion of the code opens the log file and counts the requests made in each month
FILE_NAME = 'path/to/file'

oct_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Oct/1994' in line:
    oct_count += 1
print(f'October requests:', oct_count)

nov_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Nov/1994' in line:
    nov_count += 1
print(f'November requests:', nov_count)

dec_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Dec/1994' in line:
    dec_count += 1
print(f'December requests:', dec_count)

jan_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jan/1995' in line:
    jan_count += 1
print(f'January requests:', jan_count)

feb_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Feb/1995' in line:
    feb_count += 1
print(f'February requests:', feb_count)

mar_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Mar/1995' in line:
    mar_count += 1
print(f'March requests:', mar_count)

apr_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Apr/1995' in line:
    apr_count += 1
print(f'April requests:', apr_count)

may_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'May/1995' in line:
    may_count += 1
print(f'May requests:', may_count)

jun_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jun/1995' in line:
    jun_count += 1
print(f'June requests:', jun_count)

jul_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jul/1995' in line:
    jul_count += 1
print(f'July requests:', jul_count)

aug_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Aug/1995' in line:
    aug_count += 1
print(f'August requests:', aug_count)

sep_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Sep/1995' in line:
    sep_count += 1
print(f'September requests:', sep_count)

pages = {}

f = open(LOCAL_FILE)

for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 4:
    continue

  filename = pieces[2]

  if filename in pages:
    pages[filename] += 1
  else:
    pages[filename] = 1
Keymax = max(pages, key=pages.get)
Keymin = min(pages, key=pages.get)
print('Most requested file:', Keymax)
print('Least requested file:', Keymin)

unsuccessful_count = 0
f = open(LOCAL_FILE)
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 3:
    continue
  if pieces[3] == '400':
    unsuccessful_count += 1
    continue
  if pieces[3] == '403':
    unsuccessful_count += 1
    continue
  if pieces[3] == '404':
    unsuccessful_count += 1
unsuccessful = (unsuccessful_count/726736)*100
formatted_unsuccessful = "{:.2f}".format(unsuccessful)

print('Percent of requests unsuccessful:',formatted_unsuccessful,'%')

redirected_count = 0
f = open(LOCAL_FILE)
for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 3:
    continue
  if pieces[3] == '300':
    redirected_count += 1
    continue
  if pieces[3] == '304':
    redirected_count += 1
    continue
  if pieces[3] == '302':
    redirected_count += 1
redirected = (redirected_count/726736)*100
formatted_redirected = "{:.2f}".format(redirected)

print('Percent of requests redirected:',formatted_redirected,'%')
