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
#This portion of the code opens the log file and counts the total requests made in the time period and 1995
FILE_NAME = 'path/to/file'

oct_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Oct/1994' in line:
    oct_count += 1
print(f'October count:', oct_count)

nov_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Nov/1994' in line:
    nov_count += 1
print(f'November count:', nov_count)

dec_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Dec/1994' in line:
    dec_count += 1
print(f'December count:', dec_count)

jan_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jan/1995' in line:
    jan_count += 1
print(f'January count:', jan_count)

feb_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Feb/1995' in line:
    feb_count += 1
print(f'February count:', feb_count)

mar_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Mar/1995' in line:
    mar_count += 1
print(f'March count:', mar_count)

apr_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Apr/1995' in line:
    apr_count += 1
print(f'April count:', apr_count)

may_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'May/1995' in line:
    may_count += 1
print(f'May count:', may_count)

jun_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jun/1995' in line:
    jun_count += 1
print(f'June count:', jun_count)

jul_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Jul/1995' in line:
    jul_count += 1
print(f'July count:', jul_count)

aug_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Aug/1995' in line:
    aug_count += 1
print(f'August count:', aug_count)

sep_count = 0
f = open(LOCAL_FILE)
for line in f:
  if 'Sep/1995' in line:
    sep_count += 1
print(f'September count:', sep_count)
