#!/usr/bin/env python3

import  zipfile, requests, os, sys, re;

todown = (sys.argv[1:])
joined=''
for i in todown:
    joined=joined+' '+i


os.makedirs('/Users/nikhilranjan/Desktop/'+joined,exist_ok=True)
os.chdir('/Users/nikhilranjan/Desktop/'+joined)

def download(url):
    page = requests.get(url)
    with open('subtitle.zip', 'wb') as subtitle:
        subtitle.write(page.content)
    zipf = zipfile.ZipFile("subtitle.zip")
    srt = re.compile(r'(.*)srt')
    try:
        for a in zipf.namelist():
            print (a)
            k=srt.search(a)
            m=k.group(1)+'srt'

        zipf.extract(m)
    except:
        zipf.close()
    os.remove("subtitle.zip")


def search(name):
    r=requests.get("https://subscene.com/subtitles/%s/english"%name)
    form = re.compile(r'<a href="/subtitles/(.*)/english/(.*)">')
    number = form.findall(str(r.text))
    numbers=[]
    for n in number:
        numbers.append(n[1])


    for a in numbers:
        url1 = ("https://subscene.com/subtitles/%s/english/"%name) + a

        g=requests.get(url1)
        print(url1)
        pattern = re.compile(r'<a href="/subtitle/download?(.*)"\srel')
        numbers= pattern.search(str(g.text))
        link = 'https://subscene.com/subtitle/download' + numbers.group(1)


        download(link)

s=requests.get("https://subscene.com/subtitles/title?q="+joined)
first = re.compile(r'<a href="/subtitles/(.*)"')
found = first.search(str(s.text))
search(found.group(1))
