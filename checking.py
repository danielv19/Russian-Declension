import csv

def cyrillic_check(target):
  false = 0
  for c in target: 
    if ord(c) < 1072 or ord(c) > 1103:
      false += 1
      if ord(c) == 1105 or ord(c) == 32 or c == "-":
        false = 0
  if false > 0:
    hold = True
    while hold:
      count = 0
      cyrillic = input("Please type in cyrillic: ")
      for c in cyrillic:
        if ord(c) < 1072 or ord(c) > 1103:
          count += 1
          if ord(c) == 1105 or ord(c) == 32:
            count -= 1
      if count == 0:
        hold = False
      target = cyrillic
  return target

def is_noun(word):
  with open("words.csv", "r") as words:
    reader = csv.reader(words, delimiter='\t')
    tipa = ""
    article = ""
    count = 0
    for r in reader:
      if r[0].isnumeric():
        if word == r[2].lower():
          count += 1
          length = len(r)
          if r[length-1] == "noun" or r[length-2] == "noun":
            Word_ID = r[0]
            tipa = "NOUN"
          elif r[length-1] == "adjective" or r[length-2] == "adjective":
            tipa = "ADJECTIVE"
            article = "an"
          elif r[length-1] == "verb" or r[length-2] == "verb":
            tipa = "VERB"
            article = "a"
          elif r[length-1] == "other" or r[length-2] == "other":
            tipa = "OTHER"
            article = "an"
          elif r[length-1] == "expression" or r[length-2] == "expression":
            tipa = "EXPRESSION"
            article = "an"
    if count == 0:
      print(f"{word.upper()} is not a Russian word")
      return 0
    elif tipa != "NOUN":
      print(f"{word.upper()} is not a NOUN, it is {article} {tipa}")
      return 0
    else:
      print(f"{Word_ID}: {word.upper()} found")
      return Word_ID
    
def get_declension_id(plurality, noun_id):
  with open("nouns.csv", "r") as words:
    reader = csv.reader(words, delimiter='\t')
    if int(plurality) == 2:
      for r in reader:
        length = len(r)
        if r[0] == noun_id:
          declension_id = r[length-1]
          return declension_id
    elif int(plurality) == 1:
      for r in reader:
        length = len(r)
        if r[0] == noun_id:
          declension_id = r[length-2]
          return declension_id

def get_case_name(number):
  if number == 1:
    case_name = "Prepositional"
  elif number == 2:
    case_name = "Istrumental"
  elif number == 3:
    case_name = "Accusative"
  elif number == 4:
    case_name = "Dative"
  elif number == 5:
    case_name = "Genitive"
  return case_name

def get_plurality(number):
  if number == 1:
    plural = "Singluar"
  elif number == 2:
    plural = "Plural"
  return plural

def plurality_terminal(word):
  leave = 3
  while leave > 2 or leave < 1:
    print()
    print("--------------------------------------------------")
    print(f"Please Select Plurality for {word}: ")
    print("For Singular: Enter [1]")
    print("  For Plural: Enter [2]")
    plurality = int(input("                    |"))
    leave = plurality
    print("--------------------------------------------------")
  return leave
