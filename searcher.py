import re, sys, requests;

s=requests.get("https://subscene.com/subtitles/title?q="+str(sys.argv[1:]))
first = re.compile(r'<a href="/subtitles/(.*)"')
found = first.search(str(s.text))
link2 = 'https://subscene.com/subtitles/' + found.group(1) +'/english/'

print(found.group(1))
