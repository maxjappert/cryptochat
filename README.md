# I&S Group #3: Cryptochat

This implementation is based on the SubjectiveChat,
which was implemented by Group #3 in the spring semester
of 2020. It adds asymmetric encryption to that implementation,
such that the cleartext messages neither get saved in the feed,
nor on the USB-sticks used within the Sneakernet. For a detailed
description of the functionality of the SubjectiveChat, the
Sneakernet, LogMerge, LogStore and FeedControl, please refer to their 
respective READMEs, which can be found in this same Repository.

Our implementation has only been tested on devices running Linux,
but it should also work on other operating systems. Python 3.8 was used 
for implementation and testing.

## Dependencies
Because this implementation builds upon the projects SubjectiveChat,
Sneakernet, LogMerge and FeedControl, their dependencies are required
for our implementation to work. Please note that their READMEs
are outdated for the following dependencies, because they
use outdated versions. Therefore, the following dependencies
should be downgraded as such in July 2021:

`$ pip3 install sqlAlchemy==1.3.23`

`$ sudo apt-get install python3-tk`

`$ sudo apt-get install python3-pyglet`

`$ sudo apt-get install python-pil.imagetk`

Our implementation additionally requires the following dependencies:

`$ pip3 install pyDH`

`$ pip3 install pycryptodome`

`$ pip install pybase64`

## How to use

The usage of our implementation requires the interplay between multiple
different implementations. We'll demonstrate the usage in a private chat,
yet a team chat can be operated in more or less exactly the same way.
For a more detailed dissection of the SubjectiveChat's interface and
functionality we kindly ask the reader to consult the relevant README.
This README concerns itself primarily with demonstrating what we have
actively contributed to the BACnet.

### Initiation

Client 1 needs to create a Masterfeed by starting FeedControl.
That is done by running the following command:

`$ python3 feed_control.py ui`

A window will open, which can be immediately closed. The the SubjectiveChat
can be started by running the following command:

`$ python3 subjective_chat.py`

A window will open. In there a private chat can be created by clicking
**create** and then **Private Chat**. A random string of characters will
show, which can be edited and which will represent the chat ID. By clicking
**OK** the chat can be started.

This all happens locally. In order to export this information (the newly
started chat) the Sneakernet needs to be started, which is done by running
the following command:

`$ python3 guiSneakernet.py`

There the USB-stick used for the Sneakernet needs to be chosen and an Update
needs to be performed, so that the Masterfeed of Client 1 gets exported
onto the USB-stick.

Thereafter, the USB-stick needs to be transferred to Client 2. They first
have to create a Masterfeed by starting FeedControl. Then they need to 
start Sneakernet and perform an update. Now their Masterfeed is exported
to the USB-stick.

The stick then needs to be transferred back to Client 1, who again starts
Sneakernet in order to get Client 2's Masterfeed and to gain knowledge
that a second user exists. After transfering it back to Client 2, they need
to again start Sneakernet to get that information.

Then the Client 2 needs to trust Client 1's Chat Feed by starting
FeedControl, then clicking **Update FeedIDs**, then clicking on the arrow
on the left of *Anon* (representing Client 1's Masterfeed), then 
clicking on *chat* (representing Client 1's Chat Feed). Then the button
**Trust** needs to be pressed, whereafter Client 2 trusts Client 1's
Chat Feed. After again starting Sneakernet and performing an update
with the USB-stick, the SubjectiveChat can be started.

Therein the button **join** needs to be pressed. After entering the chat
ID specified by Client 1, we have successfully started a chat.

As previously  mentioned, starting a group chat works in an almost identical manner,
only trivially different to starting a private chat.

### Actual Conversation

In order to continue chatting, the Client 1 must first trust the Client 2's
Chat Feed and both clients must im- and export using Sneakernet after 
receiving and before passing on the USB-stick.

## Encryption

### Method

This implementation uses *Cipher Block Chaining* (CBC) for encryption.
CBC is a block cipher which works by XORing the previously encrypted
block with the next plaintext block before encryption. Thereby patterns
in the plaintext aren't recognizable in the ciphertext, which is especially
useful for images, which can also be encrypted with our implementation.
The first block is encrypted with the *Initialisation Vector* (IV), which is 
different for every encrypted message and is attached to the ciphertext, which
is stored in the Chat Feed.

![Alt text](https://upload.wikimedia.org/wikipedia/commons/8/80/CBC_encryption.svg "a title")

### Key Exchange

Our implementation encrypts the messages asymmetrically, which is achieved
with a Diffie-Hellman-Merkle key exchange. The implementation uses a 32-byte
private key, which is obtained by sharing a public key. The public key is
attached to the first Chat Event and once the private key has been established
it is no longer attached to future Chat Events (in order to spare the transport
layer).

### Problems

In order to minimise seemingly redundant transportation of the USB-stick, we decided to
implement the key exchange as part of the first chat messages. Because the program
needs both public keys to generate the common private key, the first batch of messages
is only encrypted with a temporary symmetric key, which is also transmitted as part
of the Chat Event. Consequently, the first batch of messages is not securely encrypted,
because the symmetric key is transmitted together with the ciphertext which it encrypted.
Only the batch of replying messages and all thereafter are encrypted securely with a
truly private key.

