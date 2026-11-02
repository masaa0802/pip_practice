import random

RESULT_NUMBER = random.randint(1, 100)
COUNT = 0
LIMIT = 10

while COUNT < LIMIT:
  print("1から100までの数字を当ててください。あと" + str(LIMIT - COUNT) + "回です。")
  print("入力してください:")
  user_input = int(input())
  COUNT += 1
  if user_input == RESULT_NUMBER:
    print("正解！" + str(COUNT) + "回目で当たりました。")
    break
  elif COUNT == LIMIT:
    print("残念！正解は" + str(RESULT_NUMBER) + "でした。")
    break
  elif user_input < RESULT_NUMBER:
    print("もっと大きい数字です。")
  elif user_input > RESULT_NUMBER:
    print("もっと小さい数字です。")
