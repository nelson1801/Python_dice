import random
min=1
max=212

roll_again="yes"

while roll_again=="yes" or roll_again=="y":
  print("Rolling the dices...")
  print("The values are....")
  a= (random.randint(min,max))
  b= (random.randint(min,max))
 # print(a)
 #print (b)
  c="UR12CS"
  x=str(a)
  y=str(b)
  print ("The student selected are ",c+x)
  print ("The student selected are ",c+y)
  roll_again=input("Roll the Dices again?")
