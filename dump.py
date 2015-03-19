import subprocess
from sys import argv

file, db, csvdump = argv

cmdline = "mongoexport -db {} --collection Tweets --csv --fieldFile fields.txt \
-o {}".format(db, csvdump)

create_csv = cmdline.split(' ')
subprocess.call(create_csv)
