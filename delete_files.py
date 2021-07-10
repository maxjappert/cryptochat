import glob
import re
import os

for name in glob.glob('*'):
    if re.search("key$|^key|sqlite$|.pkl$|diffie_hellman", name):
        os.remove(name)
