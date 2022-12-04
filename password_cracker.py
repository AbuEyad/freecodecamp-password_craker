import hashlib

pass_array = []
salt_array = []
with open('top-10000-passwords.txt', 'rb') as f:
  line = f.readline().strip()
  while line:
    pass_array.append(line)
    line = f.readline().strip()
  f.close()
with open('known-salts.txt', 'rb') as f2:
  line = f2.readline().strip()
  while line:
    salt_array.append(line)
    line = f2.readline().strip()
  f2.close()


def crack_sha1_hash(hash, use_salts=False):
  if use_salts:
    for psd in pass_array:
      for salt in salt_array:
        hashed_password = hashlib.sha1(psd + salt).hexdigest()
        hashed_password2 = hashlib.sha1(salt + psd).hexdigest()
        if (hashed_password == hash) or (hashed_password2 == hash):
          return psd.decode('utf-8')
    return "PASSWORD NOT IN DATABASE"

  else:
    for psd in pass_array:
      hashed_password = hashlib.sha1(psd).hexdigest()
      if hashed_password == hash:
        return psd.decode('utf-8')
    return "PASSWORD NOT IN DATABASE"
