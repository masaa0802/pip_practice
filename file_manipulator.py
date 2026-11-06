import sys

if sys.argv[1] == "reverse":
  with open(sys.argv[2], "r", encoding="utf-8") as f:
    content = f.read()
  with open(sys.argv[3], "w", encoding="utf-8") as f:
    f.write(content[::-1]) # content[::-1]で文字列を逆順にする
elif sys.argv[1] == "copy":
  with open(sys.argv[2], "r", encoding="utf-8") as f:
    content = f.read()
  with open(sys.argv[3], "w", encoding="utf-8") as f:
    f.write(content)
elif sys.argv[1] == "duplicate-contents":
  with open(sys.argv[2], "r", encoding="utf-8") as f:
    content = f.read()
  with open(sys.argv[2], "w", encoding="utf-8") as f:
    f.write(content * int(sys.argv[3]))
elif sys.argv[1] == "replace-string":
  with open(sys.argv[2], "r", encoding="utf-8") as f:
    content = f.read()
  with open(sys.argv[2], "w", encoding="utf-8") as f:
    f.write(content.replace(sys.argv[3], sys.argv[4]))