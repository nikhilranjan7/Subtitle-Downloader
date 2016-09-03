import re, zipfile, os

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
