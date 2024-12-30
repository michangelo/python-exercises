def find_and_string_slice():
    text = "X-DSPAM-Confidence:    0.8475"
    # print(text)
    ipos = text.find(":")
    # print(ipos) 
    piece = text[ipos+1:].strip() # strip whitespace
    # print(piece)
    value = float(piece)
    print(value)

