def encoding(str :list[str]) ->str:
    encoded = []
    for elements in str:
        encoded += (f"{len(elements)}" + "#" + elements)
    return encoded

def decoding(s: str ) -> list[str]:
    decoded = []
    pointer = -1
    bridge = 0
    while pointer < len(s) -1:
        pointer +=1
        if s[pointer] == "#" and pointer > bridge:
            value = int(s[bridge : pointer])
            decoded.append(s[pointer + 1 : value + (pointer + 1)])
            bridge = value + (pointer + 1)
    return decoded
