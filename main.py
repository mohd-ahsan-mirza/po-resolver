import sys
def parse_po_file(file_name):
    file_object =  open(file_name,"r")
    result = []
    for line in file_object:
        print(line)
if __name__ == '__main__':
    #print(sys.argv)
    parse_po_file(sys.argv[1])

