import sys , hashlib , zlib , time , random , os

if sys.platform == 'win32':
    white  = '\033[0m'
    red    = '\033[31;1m'
    green  = '\033[32;1m'
    yellow = '\033[33;1m'
    blue   = '\033[34;1m'
    pink   = '\033[35;1m'
    cyan   = '\033[36;1m'
    # white  = ''
    # red    = ''
    # green  = ''
    # yellow = ''
    # blue   = ''
    # pink   = ''
    # cyan   = ''
    r = (white, red, green, yellow, blue, pink, cyan)
    z = random.choice(r)
elif sys.platform == 'linux' or sys.platform == 'linux2':
    white  = '\033[0m'
    red    = '\033[31;1m'
    green  = '\033[32;1m'
    yellow = '\033[33;1m'
    blue   = '\033[34;1m'
    pink   = '\033[35;1m'
    cyan   = '\033[36;1m'

try:
    import passlib, progressbar
except ImportError:
    print(red+'\n['+white+'!'+red+'] '+green+'module '+white+'passlib or progressbar'+green+'not installed'+white+'\n')
    sys.exit()
os.system('clear')

print (z+"\n<------------------------------------------------------------------------------------------------------------------------------------------->")
print (z+"|..##.....##....###.....######..##.....##....######...########.##....##.########.########.......###....##########......##......########.....|")
print (z+"|..##.....##...##.##...##....##.##.....##...##....##..##.......###...##.##.......##.......##...##.##.......##.......##....##...##.......##..|")
print (z+"|..##.....##..##...##..##.......##.....##...##........##.......####..##.##.......##.......##..##...##......##.....##........##.##.......##..|")
print (z+"|..#########.##.....##..######..#########...##...####.######...##.##.##.######...########....##.....##.....##.....##........##.########.....|")
print (z+"|..##.....##.#########.......##.##.....##...##....##..##.......##..####.##.......##.##.......#########.....##.....##........##.##.##........|")
print (z+"|..##.....##.##.....##.##....##.##.....##...##....##..##.......##...###.##.......##....##....##.....##.....##.......##....##...##....##.....|")
print (z+"|..##.....##.##.....##..######..##.....##....######...########.##....##.########.##......##..##.....##.....##..........##......##......##...|")
print (z+"<---------------------------------------------------------"+red+" WELCOME "+z+"------------------------------------------------------------------------->\n")

try:
    s = input(red+'['+white+'!'+red+'] '+cyan+'Input String'+green+': '+white)
except NameError:
    print(red+"\n["+white+"!"+red+"] "+green+"use "+white+"python2.7\n")
print(red+'['+white+'*'+red+'] '+cyan+'processing'+white+'.../'+white)
time.sleep(0.6)
print()

#bcrypt
from passlib.hash import bcrypt
bcry = bcrypt.hash(s)
print (red+"["+white+"1"+red+"] "+z+"bluecrypt           "+blue+"|    "+white+bcry,end='\n\n')

#des
from passlib.hash import des_crypt
des = des_crypt.hash(s)
print (red+"["+white+"2"+red+"] "+z+"Des Crypt           "+blue+"|    "+white+des,end='\n\n')

#bsdi
from passlib.hash import bsdi_crypt
bsd = bsdi_crypt.hash(s)
print (red+"["+white+"3"+red+"] "+z+"BSDI Crypt          "+blue+"|    "+white+bsd,end='\n\n')

#Bigcrypt
from passlib.hash import bigcrypt
bgc = bigcrypt.hash(s)
print (red+"["+white+"4"+red+"] "+z+"Bigcrypt            "+blue+"|    "+white+bgc,end='\n\n')

#crypt16
from passlib.hash import crypt16
cry = crypt16.hash(s)
print (red+"["+white+"5"+red+"] "+z+"Crypt16             "+blue+"|    "+white+cry,end='\n\n')

#sha1
from passlib.hash import sha1_crypt
shacrypt = sha1_crypt.hash(s)
print (red+"["+white+"6"+red+"] "+z+"SHA1 Crypt          "+blue+"|    "+white+shacrypt,end='\n\n')

#sha512
from passlib.hash import sha512_crypt
sha512crypt = sha512_crypt.hash(s)
print (red+"["+white+"7"+red+"] "+z+"SHA512 Crypt        "+blue+"|    "+white+sha512crypt,end='\n\n')

#sha256
from passlib.hash import sha256_crypt
sha256crypt = sha256_crypt.hash(s)
print (red+"["+white+"8"+red+"] "+z+"SHA256 Crypt        "+blue+"|    "+white+sha256crypt,end='\n\n')

# md4
m = hashlib.new("md4",s.encode('utf-8'))
md4 = m.hexdigest()
print (red +"["+white+"9"+red +"] "+z+"MD4                 "+blue+"|    "+white+md4,end='\n\n')

# md5
m = hashlib.md5(s.encode('utf-8'))
md5 = m.hexdigest()
print (red +"["+white+"10"+red +"] "+z+"MD5                "+blue+"|    " +white+md5,end='\n\n')

# sha1
m = hashlib.sha1(s.encode('utf-8'))
sha1 = m.hexdigest()
print (red +"["+white+"07"+red +"] "+z+"SHA1               "+blue+"|    "+white+sha1,end='\n\n')

# Sha224
m = hashlib.sha224(s.encode('utf-8'))
sha224 = m.hexdigest()
print (red +"["+white+"08"+red +"] "+z+"SHA224             "+blue+"|    "+white+sha224,end='\n\n')

# Sha256
m = hashlib.sha256(s.encode('utf-8'))
sha256 = m.hexdigest()
print (red +"["+white+"09"+red +"] "+z+"SHA256             "+blue+"|    "+white+sha256,end='\n\n')

# Sha384
m = hashlib.sha384(s.encode('utf-8'))
sha384 = m.hexdigest()
print (red +"["+white+"10"+red +"] "+z+"SHA384             "+blue+"|    "+white+sha384,end='\n\n')

# Sha512
m = hashlib.sha512(s.encode('utf-8'))
sha512 = m.hexdigest()
print (red +"["+white+"11"+red +"] "+z+"SHA512             "+blue+"|    "+white+sha512,end='\n\n')

print ('<-----------------------------------------------------'+green+"All hashes are created successfully "+green+'--------------------------------------------------------------->')