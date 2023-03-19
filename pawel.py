# psw = "2E1##V3dR$7L"
#
key = "piwo"
#
# out = ""
k = len(key)
#
# for i in range(len(psw)):
#     out += chr(ord(psw[i]) + ord(key[i % k]))
#
# print(out)

psw = "¢®¨¿ªÓÂ®»"
out = ""
for i in range(len(psw)):
    out += chr(ord(psw[i]) - ord(key[i % k]))

print(out)