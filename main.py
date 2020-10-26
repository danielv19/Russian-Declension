import csv
from checking import cyrillic_check, is_noun, get_declension_id, get_case_name, get_plurality, plurality_terminal

print("Welcome to the Russian Noun Declension Program")
print("--------------------------------------------------")
print("Please type in the desired Russian noun")
intial_word = input("(in cyrillic & the nominative case / original form): ").strip().lower()
#Checks for cyrillic
word = cyrillic_check(intial_word)
#check if a word/noun
noun_id = is_noun(word)
while noun_id == 0:
  print()
  print("Please type in a russian NOUN")
  again = input("(in cyrillic & the nominative case / original form): ").strip().lower()
  noun_id = is_noun(again)
  word = again
word = word.upper()
#declension
plurality = plurality_terminal(word)
numbers = get_plurality(plurality)
#Find Declension id
declension_id = get_declension_id(plurality, noun_id)
#print(declension_id)
leave = 8
while leave > 6 or leave < 0:
  print()
  print("--------------------------------------------------")
  print(f"Please Select Case for {word}: ")
  print("For Prepositional: Enter [1]")
  print("  For Istrumental: Enter [2]")
  print("   For Accusative: Enter [3]")
  print("       For Dative: Enter [4]")
  print("     For Genitive: Enter [5]")
  print("             Back: Enter [0]")
  case = int(input("                         |"))
  leave = case
  print("--------------------------------------------------")
case_name = get_case_name(leave)
#print out the case declension
with open("declensions.csv", "r") as declension:
  reader = csv.reader(declension, delimiter='\t')
  for r in reader:
    if r[0] == declension_id:
      length = len(r)
      target = r[length - case]
      if target == "":
        print(f"ERROR: NO INFO FOUND FOR {case_name.upper()} {numbers.upper()} // {word} //")
        break
      subs = 0
      subs2 = 0
      for c in target:
        if c == "'":
          break
        subs += 1
      seek = False
      for c in target:
        if c == "," or seek:
          seek = True
          if c == "'":
            break
        subs2 += 1
      if subs == 0:
        print(f"{case_name} {numbers}: {target}")
      if subs2 > 0:
        print(f"{case_name} {numbers}: {target[:subs]}{target[subs+1:subs2]}{target[subs2+1:]}")
      else:
        print(f"{case_name} {numbers}: {target[:subs]}{target[subs+1:]}")
