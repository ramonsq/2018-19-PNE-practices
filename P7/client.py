import requests
import sys
from Seq import Seq

SERVER = "http://rest.ensembl.org/"
ext = "sequence/id/ENSG00000165879?"
PORT = 8000
headers = {"Content-Type": "application/json", "Accept": "application/json"}

r = requests.get(SERVER + ext, headers = headers)

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

seq = Seq(decoded['seq'])

bases = "A", "C", "T", "G"
basesperc = {}
numofbases = {}
numbases = ''
popular = ''
le = seq.len()

# -- doing count and percentage operations
for i in bases:
    basesperc.update({i: seq.perc(i)})
    numofbases.update({i: seq.count(i)})


# -- calculating the maximum

for i in bases:
    if str(seq.count(i)) > str(numbases) : popular, numbases = i, seq.count(i)


# -- print results
print("The number of bases in the FRAT1 gene is {}".format(le))
print("The number of T bases in the FRAT1 gene is {}".format(numofbases["T"]))
print("The most popular base in the FRAT1 is {} with a percentage of {}%.".format(popular, str(seq.perc(popular))))
print("The percentages of all the bases in the FRAT1 are {}".format(basesperc))