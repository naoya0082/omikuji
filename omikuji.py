import random

omikuji = ["大吉", "吉", "大凶"]

chose = random.randint(0, 2)
result = omikuji[chose]

print(f"今日の運勢は{result}")
