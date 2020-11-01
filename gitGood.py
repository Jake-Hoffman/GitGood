#This script will get work done

import os
import time

while (True):
    os.system('git commit --allow-empty -m "Empty Test"')
    os.system('git push')

    print("Very productive day today!")

    time.sleep(86400)