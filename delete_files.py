import glob
import re
import os

for name in glob.glob('*'):
    if re.search("key$|^shared_key|^key|sqlite$|.pkl$|^stored_messages|diffie_hellman", name):
        os.remove(name)
