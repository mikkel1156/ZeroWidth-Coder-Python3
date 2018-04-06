import random
ZERO_WIDTH_JOINER = "‍"
ZERO_WIDTH_NONJOINER = "‌"
ZERO_WIDTH_SPACE = "​"
ZERO_WIDTH_NOBREAK_SPACE = "⁠"

def encode(sec, msg=None):
    #   Convert message to binary, keeping leading zeros.
    secBin = ' '.join(["{0:b}".format(ord(x)) for x in sec])
    print(secBin)
    
    #   Set the start of the encoded message.
    secZeroWidth = ZERO_WIDTH_NOBREAK_SPACE
    for bin in secBin.split(" "):
        for bit in bin:
            if bit == "1":
                secZeroWidth += ZERO_WIDTH_JOINER
            elif bit == "0":
                secZeroWidth += ZERO_WIDTH_NONJOINER

        #   Indicate when that binary string is done.
        secZeroWidth += ZERO_WIDTH_SPACE

    #   Indicate the end of the encoded message.
    secZeroWidth += ZERO_WIDTH_NOBREAK_SPACE

    #   Check if there is any message to insert it into.
    if msg is not None:
        #   Get a random index someone in the message.
        randIndex = random.randrange(0, len(msg))

        #   Return the message with the zero-width encoded secret at a random point.
        return msg[:randIndex] + secZeroWidth + msg[randIndex:]
    else:
        #   Return the zero-width encoded secret.
        return secZeroWidth

def decode(msg):
    secBin = ""
    triggerd = False

    for c in msg:
        #   Did we find the start of the string?
        if triggerd == True:
            if c == ZERO_WIDTH_JOINER:
                secBin += "1"
            elif c == ZERO_WIDTH_NONJOINER:
                secBin += "0"
            elif c == ZERO_WIDTH_SPACE:
                secBin += " "
            elif c == ZERO_WIDTH_NOBREAK_SPACE:
                break

        #   Set triggered to TRUE when we see the start zero-width character.
        if c == ZERO_WIDTH_NOBREAK_SPACE:
            triggerd = True

    try:
        #   Convert the binary message into a string and return it.
        return ''.join([chr(int(x, 2)) for x in secBin[:len(secBin)-1].split(" ")])
    except Exception:
        print("An error has occured. Maybe no zero-width characters were found.")
        exit()