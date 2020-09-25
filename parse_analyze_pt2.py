#This portion of the code retrieves the log file from a network and saves a cached copy
from urllib.request import urlretrieve
import re
import datetime

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
jan_match = 0
feb_match = 0
mar_match = 0
apr_match = 0
may_match = 0
jun_match = 0
jul_match = 0
aug_match = 0
sep_match = 0
oct_match = 0
oct95_match = 0
nov_match = 0
dec_match = 0

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
mon = 0
tue = 0
wed = 0
thur = 0
fri = 0
sat = 0
sun = 0



for line in f:
  pieces = re.split('.+ \[(.+) .+\] "[A-Z]{3,4} (.+) HTTP/1.0" ([0-9]{3})', line)
  if len(pieces) < 4:
    continue
  date_time = re.split('.*\[([^:])', pieces[1])
  dt = datetime.datetime.strptime(date_time, '%Y %b %d')
  weekday = datetime.datetime.weekday(dt)

  if weekday == 0:
    mon += 1
  
  elif weekday == 1:
    tue += 1
  
  elif weekday == 2:
    wed += 1
  
  elif weekday == 3:
    thur += 1

  elif weekday == 4:
    fri += 1

  elif weekday == 5:
    sat += 1

  elif weekday == 6:
    sun += 1


  filename = pieces[2]
  
  if 'Jan' in line:
      jan_match += 1
  if 'Feb' in line:
      feb_match += 1
  if 'Mar' in line:
      mar_match += 1
  if 'Apr' in line:
      apr_match += 1
  if 'May' in line:
      may_match += 1
  if 'Jun' in line:
      jun_match += 1
  if 'Jul' in line:
      jul_match += 1
  if 'Aug' in line:
      aug_match += 1
  if 'Sep' in line:
      sep_match += 1
  if 'Oct/1994' in line:
      oct_match += 1
  if 'Oct/1995' in line:
      oct95_match += 1
  if 'Nov' in line:
      nov_match += 1
  if 'Dec' in line:
      dec_match += 1

  if filename in pages:
    pages[filename] += 1
  else:
    pages[filename] = 1
Keymax = max(pages, key=pages.get)
Keymin = min(pages, key=pages.get)
print('Most requested file:', Keymax)
print('Least requested file:', Keymin)
print(f'The number of requests made in January 1995 was:', jan_match)
print(f'The number of requests made in February 1995 was: {feb_match}')
print(f'The number of requests made in March 1995 was: {mar_match}')
print(f'The number of requests made in April 1995 was: {apr_match}')
print(f'The number of requests made in May 1995 was: {may_match}')
print(f'The number of requests made in June 1995 was: {jun_match}')
print(f'The number of requests made in July 1995 was: {jul_match}')
print(f'The number of requests made in August 1995 was: {aug_match}')
print(f'The number of requests made in September 1995 was: {sep_match}')
print(f'The number of requests made in October 1994 was: {oct_match}')
print(f'The number of requests made in October 1995 was: {oct_match}')
print(f'The number of requests made in November 1994 was: {nov_match}')
print(f'The number of requests made in December 1994 was: {dec_match}')

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
