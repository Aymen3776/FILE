import os, platform, time
os.system('git pull -q')
os.system('clear')
print('\n\n\n\n\n Use VPN for Login Cookies')
input('Press Enter')
#yy = input('Did You Know How to Make EAAB Token??(y/n)')
#if yy at in 'yes Y y Yes YES':
 #pass
#else:
# os.system('xdg-open https://www.facebook.com/100074059501726/posts/150776190734364/?app=fbl')
uu = os.popen('play').read()

if 'Usage summary' in uu:
 pass
else:
 print(uu)
 os.system('pkg install sox -y')

bit = platform.architecture()[0]
if bit == '64bit':
 import FILE64
elif bit == '32bit':
 import FILE32
