#進数を変換するプログラム
select_input = int(input("変換元は何進数ですか? [2,8,10,16] : "))
select_output = int(input("変換先は何進数ですか? [2,8,10,16] : "))
original_deta = input("変換元の数値を入力してください : ")
if select_output == 2:
	print(bin(int(original_deta,select_input)))
elif select_output == 8:
	print(oct(int(original_deta,select_input)))
elif select_output == 10:
	print(int(original_deta,select_input))
elif select_output == 16:
	print(hex(int(original_deta,select_input)))
else:
	print("入力した数値が間違っています")

