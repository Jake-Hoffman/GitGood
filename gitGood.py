#This script will make a push to gitHub everyday to make you and your employer's happy

import os

os.system('git commit --allow-empty -m "Empty Test"')
os.system('git push')