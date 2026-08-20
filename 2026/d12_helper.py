###########################################################################
# import

# r varies
bingo = [1, 2, 3, 4, 5]         # default
# c varies
#bingo = [1, 6, 11, 16, 21]
# p varies
#bingo = [1, 26, 51, 76, 101]
# y varies
#bingo = [1, 126, 251, 376, 501]

# y and p constant, c and r equal
#bingo = [1, 7, 13, 19, 25]
# y and p constant, c and r opposed
#bingo = [5, 9, 13, 17, 21]
# y and c constant, p and r equal
#bingo = [1, 27, 53, 79, 105]
# y and c constant, p and r opposed
#bingo = [5, 29, 53, 77, 101]
# y and r constant, c and p equal
#bingo = [1, 31, 61, 91, 121]
# y and r constant, c and p opposed
#bingo = [21, 41, 61, 81, 101]

# p and c constant, y and r equal
#bingo = [1, 127, 253, 379, 505]
# p and c constant, y and r opposed
#bingo = [5, 129, 253, 377, 501]
# p and r constant, c and y equal
#bingo = [1, 131, 261, 391, 521]
# p and r constant, c and y opposed
#bingo = [21, 141, 261, 381, 501]

# r and c constant, y and p equal
#bingo = [1, 151, 301, 451, 601]
# r and c constant, y and p opposed
#bingo = [101, 201, 301, 401, 501]

# y constant, p = r = c
#bingo = [1, 32, 63, 94, 125]
# y constant, p = - r = c
#bingo = [5, 34, 63, 92, 121]
# y constant, p = r = -c
#bingo = [21, 42, 63, 84, 105]
# y constant, - p = r = c
#bingo = [101, 82, 63, 44, 25]

# p constant, y = r = c
#bingo = [1, 132, 263, 394, 525]
# p constant, y = r = - c
#bingo = [21, 142, 263, 384, 505]
# p constant, y = - r = c
#bingo = [5, 134, 263, 392, 521]
# p constant, - y = r = c
#bingo = [501, 382, 263, 144, 25]

# r constant, y = p = c
#bingo = [1, 156, 311, 466, 621]
# r constant, y = p = - c
#bingo = [21, 166, 311, 456, 601]
# r constant, y = - p = c
#bingo = [101, 206, 311, 416, 521]
# r constant, - y = p = c
# bingo = [501, 406, 311, 216, 121]

# c constant, y = p = r
#bingo = [1, 152, 303, 454, 605]
# c constant, y = p = - r
#bingo = [5, 154, 303, 452, 601]
# c constant, y = - p = r
#bingo = [101, 202, 303, 404, 505]
# c constant, - y = p = r
# bingo = [501, 402, 303, 204, 105]

# y = p = r = c
#bingo = [1, 157, 313, 469, 625]

# y = p = -r = c
#bingo = [5, 159, 313, 467, 621]
# y = p = r = -c
#bingo = [21, 167, 313, 459, 605]
# y = -p = r = c
#bingo = [101, 207, 313, 419, 525]
# -y = p = r = c
#bingo = [501, 407, 313, 219, 125]

# y = p = -r = -c
#bingo = [25, 169, 313, 457, 601]
# -y = p = r = -c
#bingo = [105, 209, 313, 417, 521]
# y = -p = r = -c
#bingo = [505, 409, 313, 217, 121]

for i in bingo:
    print("%d " % i, end="")
print("")

# numbers
for i in range(1,625+1,25):
    for j in range(i,i+25):
        if not j in bingo:
            print("%d " % j, end="")
    print("")

print("")

# hypercube
for i in range(1,625+1,25):
    for j in range(i,i+25):
        print("%d " % j, end="")
    print("")
