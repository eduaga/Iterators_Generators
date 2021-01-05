import hashlib

def md5forline(file_name):
  with open(file_name, 'rb') as f:
    for line in f:
      yield(hashlib.md5(line))

for enc_line in md5forline('my.txt'):
  print(enc_line.hexdigest())
