from os import listdir
from os.path import isfile, join

path = './processing.org/reference'
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('html') ]

newLines = []

for htmlFile in files:
    htmlFilePath = join(path, htmlFile)
    newLines = []
    with open(join(path, htmlFile)) as f:
        for line in f:
            if line.strip().startswith('<link href="/css'):
                newLines.append('<link href="../css/style.css" rel="stylesheet" type="text/css" />')
            if line.strip().startswith('<a href="/reference/" class'):
                newLines.append('<a href="./index.html" class="active">Reference</a><br />')
            else:
                newLines.append(line)
    with open(join(path, htmlFile), 'w') as f:
        f.writelines(newLines)


print 'done replaceing css and reference link'
