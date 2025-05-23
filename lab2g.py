#!/usr/bin/env python3
# Author: Shazma Hussain
# Author ID: shussain133 (167689223)
# Date Created: 2025/05/23

import sys
if len(sys.argv) > 1:
    timer = int(sys.argv[1])  
else:
    timer = 3  


while timer != 0:
    print(timer)
    timer -= 1
print('blast off!')