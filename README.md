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
but it should also work on other operating systems.

## Dependencies
Because this implementation builds upon the projects SubjectiveChat,
Sneakernet, LogMerge and FeedControl, their dependencies are required
for our implementation to work. Please note that their READMEs
are outdated for the following dependencies, because they
use outdated versions. Therefore, the following dependencies
should be downgraded as such in July 2021:

`pip3 install sqlAlchemy==1.3.23`

`sudo apt-get install python3-tk`

`sudo apt-get install python3-pyglet`

`sudo apt-get install python-pil.imagetk`

Our implementation additionally requires the following dependencies:

`pip3 install pyDH`