import requests

# Set the request parameters
# url = 'https://{Your Domain}.zendesk.com/api/v2/deleted_tickets.json'
remove = 'https://{Your Domain}.zendesk.com/api/v2/deleted_tickets/destroy_many.json?ids='
user = '{Your Email}' + '/token'
pwd = '{Your API Token}'


# Do the HTTP get request
response = requests.get(url, auth=(user, pwd))

# Check for HTTP codes other than 200
# But this is not needed really.
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Empty thing
finalist = ''

# Decode the JSON response into a dictionary and use the data
data = response.json()
# This is the full list of deleted tickets
tkt_list = data['deleted_tickets']

# Go through the list of deleted tickets and find their IDs
# Concatenate a string based on commas
for tk in tkt_list:
    finalist += str(tk['id']) + ','
# Delete the last comma
finalist = finalist[:-1]

# Append the list to the API endpoint URL
finalist = remove + finalist
print(finalist)
# execute the request
response2 = requests.delete(finalist, auth=(user, pwd))
print(response2.status_code)

# IMPORTANT RUN THIS WITH : 'watch -n 600 python3 main.py &'
# The reason is that Zendesk takes FOREVER to remove bulk tickets so this may create 404s and competing requests that fail.
# Running this every 10 min. its easier than setting the loop in Python and checking the job status, etc. Too much unnecessary code.
# Turn this on and leave on background. Code can be better and stop with 3-5 404s ina row, but easier just turn it off at some point.
