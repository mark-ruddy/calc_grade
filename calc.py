# second_grade = 84
#second_grade = round((84 + 92 + 70 + 91 + 86 + 82 + 76) / 7, 2)
second_grade = round((84 + 92 + 70 + 91 + 86 + (82 + 76 / 200)) / 6, 2)
final_grade = 50

sec = round(second_grade * 0.3, 2)
fin = round(final_grade * 0.7, 2)
overall = round(sec + fin, 2)

print(f"Second year overall: {second_grade}")
print(f"Final year overall: {final_grade}")
print(f"Second weighted: {sec}")
print(f"Final weighted: {fin}")
print(f"Overall: {overall}")
