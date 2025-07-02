# @article{yaltirakli,
#   title   = "Blitzortung",
#   author  = "Yaltirakli, Gokberk",
#   journal = "gkbrk.com",
#   year    = "2025",
#   url     = "https://www.gkbrk.com/blitzortung"
# }

# LZW decoder
def LZW_decode(b):
    e = {}
    d = list(b.decode())
    c = d[0]
    f = c
    g = [c]
    h = 256
    o = h
    for i in range(1, len(d)):
        a = ord(d[i])
        a = d[i] if h > a else e[a] if e.get(a) else f + c
        g.append(a)
        c = a[0]
        e[o] = f + c
        o += 1
        f = a
    return ''.join(g).encode()


