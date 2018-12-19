import urllib.request

response = urllib.request.urlopen('https://feodotracker.abuse.ch/downloads/malware_hashes.txt')
filehash = response.read()

print (filehash)

# for line in filehash:
#     li=line.strip()
#     if not li.strip().startswith("#"):
#         print (line.rstrip())