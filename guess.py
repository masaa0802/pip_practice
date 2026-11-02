import random

RESULT_NUMBER = random.randint(1, 100)
COUNT = 0

while COUNT >= 0:
  print("1から100までの数字を当ててください。")
  print("入力してください:")
  user_input = int(input())
  COUNT += 1
  if user_input == RESULT_NUMBER:
    print("正解！" + str(COUNT) + "回目で当たりました。")
    break
  elif user_input < RESULT_NUMBER:
    print("もっと大きい数字です。")
  elif user_input > RESULT_NUMBER:
    print("もっと小さい数字です。")
