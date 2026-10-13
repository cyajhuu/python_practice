year = int(input("請輸入年份："))

def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    elif year % 3200 != 0:
        return True
    else:
        return False

print(is_leap(year))

# 3200的計算被漏掉，
# year = int(input("請輸入年份："))

# def is_leap():
# 	if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
# 		print('平年')
# 	elif year % 4 == 0 or (year % 400 == 0 and year % 3200 != 0):
# 		print('閏年')
# 	return

# is_leap()