import re
import shutil
import tempfile
import urllib.request
import urllib.parse

url = 'https://www.google.com/search'
data = {}
q = input()
data['q']=q
url_values = urllib.parse.urlencode(data)

full_url = url + '?' + url_values

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win65; x64)'
headers = {'User-Agent': user_agent}
req = urllib.request.Request(full_url, headers=headers)
# with urllib.request.urlopen(req) as response:
#     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
#         shutil.copyfileobj(response, tmp_file)
target_name = re.sub(r'[^a-zA-Z0-9_]','','_'.join(q.split()))
with urllib.request.urlopen(req) as response:
    with open(f"{target_name}.html","wb") as tmp_file:
        shutil.copyfileobj(response, tmp_file)

# with open(tmp_file.name) as html:
#     lines = html.readlines()
#     for l in lines:
#         print(l)
