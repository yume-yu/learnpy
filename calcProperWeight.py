bmi = 22
print("適正体重を算出します。")
height = float(input("身長を入力してください[cm] : "))
proper_weight = bmi * (height / 100) ** 2
print("身長"+str(height)+"cmの人の適正体重は"+str(proper_weight)+"kgです")
