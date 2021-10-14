import re

phoneNum = re.compile(r"(\(\d\d\)) (\d\d\d\d-\d\d\d-\d\d\d)")

mo = phoneNum.search("My number is (91) 9325-874-285.")

print("Phone number found : " + mo.group())
print(mo.group(1) + " " + mo.group(2))
