import glob
import re
import os

for name in glob.glob('*'):
    if re.search("key$|^shared_key|^key|sqlite$|.pkl$|^stored_messages|^partners_pubkey|^initiator_|diffie_hellman", name):
        os.remove(name)
