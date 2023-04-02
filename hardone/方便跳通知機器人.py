import requests

# Set the IFTTT webhooks URL and event name
url = 'https://maker.ifttt.com/trigger/{event_name}/with/key/{your_key}'

# Set the event name and your key
event_name = 'your_event_name'
your_key = 'your_ifttt_key'

# Send an HTTP request to trigger the IFTTT event
response = requests.post(url.format(event_name='TSEY', your_key='RIpRmm9hfdmqEQnELSULG'))

# Check the response status code
if response.status_code == 200:
    print('Event triggered successfully!')
else:
    print('Error triggering event.')