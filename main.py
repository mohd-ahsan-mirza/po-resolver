import sys
def parse_po_file():
    pos = []
    for run in range(1,len(sys.argv)):
        file_object =  open(sys.argv[run],"r")
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
    return pos
def generate_combined_po(pos):
    result = []
    for po in pos:
        for element in po:
            if element not in result:
                result.append(element)
    return result
def generate_result_file(result):
    with open('result.po', 'w') as f:
        for item in result:
            f.write("%s\n" % item)

if __name__ == '__main__':
    #print(sys.argv)
    pos = parse_po_file()
    result = generate_combined_po(pos)
    generate_result_file(result)


