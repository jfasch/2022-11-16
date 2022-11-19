import os
import os.path
import shutil
import sys
import time

def iter_new_files(srcdir, interval):
    seen = set()
    while True:
        entries = os.listdir(srcdir)
        for entry in entries:
            if entry not in seen:
                yield os.path.join(srcdir, entry)
                seen.add(entry)
        time.sleep(interval)

sourcedir = sys.argv[1]
destdir = sys.argv[2]
interval = int(sys.argv[3])

for filename in iter_new_files(sourcedir, interval):
    #print(filename)
    shutil.move(filename, destdir)
