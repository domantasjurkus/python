def rotn(string, n):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[n:]+chars[:n]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in string )

var = "cqrb lryqna rb fjh, fjh qjamna cqjw axc cqracnnw. qnan, hxd wnena twxf qxf oja cx bqroc! xq kh cqn fjh, cqn jwbfna rb mnjmvjwblqnbc."
var = var.lower()

for i in xrange(1, 27):
    print "Rotated by:", i
    print rotn(var, i)
