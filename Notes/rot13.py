def rot13(inp):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    out = ""

    for i in range(len(inp)):
        character = inp[i]
        if letters.find(character) == -1:
            out = out + character
        else:
            index = letters.find(character)
            out = out + letters[index + 13]

    return out


print(
    rot13(
        "Jr'er ab fgenatref gb ybir. Lbh xabj gur ehyrf naq fb qb V. N shyy pbzzvgzrag'f jung V'z guvaxvat bs. Lbh jbhyqa'g trg guvf sebz nal bgure thl."
    )
)
