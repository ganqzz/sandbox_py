# copying files by manual

DATA = "../data/"
TMP = "../tmp/"

# copy text file
infile = open(DATA + "sample.txt", "rt", encoding="utf-8")
outfile = open(TMP + "sample-copy.txt", "wt", encoding="utf-8")
for line in infile:
    outfile.write(line)
    # print(line, end='', file=outfile)
    # print(line.rstrip(), file=outfile)
    print('.', end='', flush=True)
outfile.close()  # important
infile.close()

print()

# copy binary file
infile = open(DATA + "hotel_phillips.jpg", "rb")
outfile = open(TMP + "hotel_phillips-copy.jpg", "wb")
while True:
    buf = infile.read(8192)  # 8KB
    if buf:
        outfile.write(buf)
        print('.', end='', flush=True)
    else:
        break
outfile.close()  # important
infile.close()
