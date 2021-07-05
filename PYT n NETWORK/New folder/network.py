import hashlib
str2hash = "ishapythonproject"
result = hashlib.md5(str2hash.encode())
print("The hexadecimal equivalent of hash is : ", end ="")
print(result.hexdigest())
