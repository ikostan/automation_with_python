import http.client
import urllib.parse
params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
conn = http.client.HTTPConnection("127.0.0.1:5000")
conn.request("POST", "/shutdown", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
