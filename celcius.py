degree_celsius = input("請輸入攝氏溫度：")  #會被存成為字串
degree_fahrenheit = float(degree_celsius) * 9 / 5 + 32  #先做casting變數字  
print("華氏溫度為:", degree_fahrenheit)