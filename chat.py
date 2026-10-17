# # 讀取檔案
# def read_file(filename):
#     lines = []
#     with open(filename, 'r', encoding='utf-8-sig') as f:
#         for line in f:
#             lines.append(line.strip())  #把換行符號去掉再裝進lines
#     return lines

# #主要程式
# def main():
#     lines = read_file('input.txt')
#     print(lines)

# main()

# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  #把換行符號去掉再裝進lines
    return lines

#調整檔案內容
def convert(lines):
    new = []
    person = None
    for line in lines:   #把lines清單裡的東西(line)一行一行叫出來
        if line == 'Allen':
            person = 'Allen'
        continue
        if line == 'Tom':
            person = 'Tom'
        continue
    if person:
        new.append(person + ':' + line)
    return new

#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

#主要呼叫程式
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()
