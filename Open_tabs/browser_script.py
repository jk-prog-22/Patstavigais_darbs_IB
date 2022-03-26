import os
import re
import sys
import webbrowser

# Atver un nolasa teksta failu 
with open(os.path.join(sys.path[0], 'majaslapas.txt')) as f:
    urls = f.read()
    links = re.findall(r'(https?://[^\s]+)', urls)

# Atver visus linkus, kas ir teksta failā
for url in links:
    webbrowser.open(url, new=0, autoraise=True)
    print('Atvērts: ' + url)


