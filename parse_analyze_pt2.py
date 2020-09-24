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
nov_count = 0
dec_count = 0
jan_count = 0
feb_count = 0
mar_count = 0
apr_count = 0
may_count = 0
jun_count = 0
jul_count = 0
aug_count = 0
sep_count = 0
oct95_count = 0

f = open(LOCAL_FILE)
for line in f:
    if 'Oct/1994' in line:
        oct_count += 1

    elif 'Nov/1994' in line:
        nov_count += 1

    elif 'Dec/1994' in line:
        dec_count += 1

    elif 'Jan/1995' in line:
        jan_count += 1

    elif 'Feb/1995' in line:
        feb_count += 1

    elif 'Mar/1995' in line:
        mar_count += 1

    elif 'Apr/1995' in line:
        apr_count += 1

    elif 'May/1995' in line:
        may_count += 1

    elif 'Jun/1995' in line:
        jun_count += 1

    elif 'Jul/1995' in line:
        jul_count += 1

    elif 'Aug/1995' in line:
        aug_count += 1

    elif 'Sep/1995' in line:
        sep_count += 1

    else:
        oct95_count += 1

print(f'October 1994 requests:', oct_count)
print(f'November 1994 requests:', nov_count)
print(f'December 1994 requests:', dec_count)
print(f'January 1995 requests:', jan_count)
print(f'February 1995 requests:', feb_count)
print(f'March 1995 requests:', mar_count)
print(f'April 1995 requests:', apr_count)
print(f'May 1995 requests:', may_count)
print(f'June 1995 requests:', jun_count)
print(f'July 1995 requests:', jul_count)
print(f'August 1995 requests:', aug_count)
print(f'September 1995 requests:', sep_count)
print(f'October 1995 requests:', oct95_count)

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
