s='the lyrics is not that poor'
start=s.find("not")
end=s.find("poor")
poor='poor'
if end>start:
    s=s[:start]+"good"+s[end+len(poor):]
    print(s)