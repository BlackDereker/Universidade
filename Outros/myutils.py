def fixedprint(text, after, pos):

    text = str(text)
    after = str(after)

    if pos < len(text) + 1:
        pos = len(text) + 1

    pos = pos - len(text)

    print(text + (" " * pos) + after)
