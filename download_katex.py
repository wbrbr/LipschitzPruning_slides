import urllib.request
import zipfile

urllib.request.urlretrieve('https://github.com/KaTeX/KaTeX/releases/download/v0.16.22/katex.zip', 'katex.zip')

with zipfile.ZipFile('katex.zip', 'r') as z:
    z.extractall()