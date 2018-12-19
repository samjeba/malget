import urllib.request

response = urllib.request.urlopen('https://feodotracker.abuse.ch/downloads/malware_hashes.txt')
filehash = response.read().decode('utf-8')


print (filehash)