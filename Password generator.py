from random import shuffle
lis = ['!', '@', '#', '$', '%', '¨', '&', '*', '(', ')', '-', '_', '=', '+', '1', '2', '3', '4', '5', '6', '7', '8',
       '9', '0', '"', "'", '.', ',', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'X', 'Z', '<', '>', ':', ':', '?', '/', '|', ' ']
shuffle(lis)
lis2 = lis[:21]
for c in lis2:
    print(c, end='')