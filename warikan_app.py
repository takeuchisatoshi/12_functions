amount = int(input("合計金額を入力してね > "))
number_of_people = int(input("人数を入力してね > "))

payment = amount // number_of_people
remainder = amount % number_of_people

print(f"1人: {payment}円､ 端数: {remainder}円")