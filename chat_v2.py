# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())  #把換行符號去掉再裝進lines
    return lines

#調整檔案內容
def convert(lines):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:   #把lines清單裡的東西(line)一行一行叫出來
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen said:',allen_word_count, 'words')
    print('Allen send:',allen_image_count, 'images')
    print('Allen send:',allen_sticker_count, 'stickers')
    print('Viki said:',viki_word_count, 'words')
    print('Viki send:',viki_image_count, 'images')
    print('Viki send:',viki_sticker_count, 'stickers')

#寫入檔案
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

#主要呼叫程式
def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)

main()
