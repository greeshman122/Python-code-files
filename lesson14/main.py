with open("coding.txt" , "w") as file:
  file.write("Hi ! I am Bunny and I am 14 yrs old.")
file.close()

with open("coding.txt" , "r") as file:
  data = file.readlines()
  print("The words in this file are ")
  for line in data:
      word = line.split()
      print(word)
file.close()