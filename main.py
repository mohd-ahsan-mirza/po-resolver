import sys
def parse_po_file(file_name):
    file_object =  open(file_name,"r")
    pos = []
    for run in range(1,len(sys.argv)):
        index = 0
        po = []
        po.append("")
        for line in file_object:
            if not line.strip():
                index = index + 1
                po.append("")
            else:
                po[index] = po[index] + line
        pos.append(po)
if __name__ == '__main__':
    #print(sys.argv)
    parse_po_file(sys.argv[1])

