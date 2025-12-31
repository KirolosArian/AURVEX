path = r"c:\Users\kero6\Desktop\New folder (3)\New folder\New folder\2\code.html"
s = open(path, 'r', encoding='utf-8').read()
start = s.find('<script>')
end = s.find('</script>', start)
script = s[start:end]
print('script length', len(script))
stack = []
pairs = {'{':'}','[':']','(':')'}
for i,ch in enumerate(script):
    if ch in pairs:
        stack.append((ch,i))
    elif ch in ')]}':
        if not stack:
            print('Unmatched closing', ch, 'at', i)
            break
        last, pos = stack.pop()
        if pairs[last] != ch:
            print('Mismatched', last, 'at', pos, 'with', ch, 'at', i)
            break
else:
    if stack:
        print('Unmatched openings sample:', stack[-6:])
    else:
        print('All matched')
print('Done')