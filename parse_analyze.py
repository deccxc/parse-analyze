from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'
total_requests = 0
year_count = 0

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE);

FILE_NAME = 'path/to/file'
f = open(LOCAL_FILE)

for line in f:
    total_requests += 1
    if '1995' in line:
        year_count += 1

print(f'The total number of requests made in the time period of this file is', total_requests)
print(f'The total number of requests made in 1995 is', year_count)
