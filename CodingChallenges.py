def designerPdfViewer(h, word):
    # Write your code here
    # h.replace(" ","")
    hh = [int(h_temp) for h_temp in h]

    st = string.ascii_lowercase
    w_len = len(word)
    dic_st = {}
    i = 0
    for ch in st:
      dic_st[ch] = hh[i]
      i += 1
    h_char = 0
    for ch in word:
      h_char = dic_st[ch] if dic_st[ch] > h_char else h_char
    return h_char*w_len
