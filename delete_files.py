import glob
import re
import os

for name in glob.glob('*'):
    if re.search("key$|^key|sqlite$|.pkl$", name):
        os.remove(name)
