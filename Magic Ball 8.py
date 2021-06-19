###Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
# Magic 8-Ball, should I do this project?
#We’ll be using the following 9 possible answers for our Magic 8-Ball
#1.Yes - definitely.
#2.It is decidedly so.
#3.Without a doubt.
#4.Reply hazy, try again.
#5.Ask again later.
#6.Better not tell you now.
#7.My sources say no.
#8.Outlook not so good.
#9.Very doubtful.


#Needed Variables
Name = input("Enter you Name: ")
Question =input("Ask your question: ")
Answer = ""

#Genrating random numbers
import random

Random_number = random.randint(1 , 9)
# print(random_number)  #Uncomment to check whether random function is working or not

#CONTROL FLOW
if Random_number==1:
 Answer = "Yes - definitely."
elif Random_number==2:
 Answer ="It is decidedly so."
elif Random_number==3:
  Answer ="Without a doubt."
elif Random_number==4:
  Answer ="Reply hazy, try again."
elif Random_number==5:
  Answer ="Ask again later."
elif Random_number==6:
  Answer ="Better not tell you now."
elif Random_number==7:
 Answer ="My sources say no."
elif Random_number==8:
 Answer = "Outlook not so good."
elif Random_number==9:
  Answer ="Very doubtful."
else :
  Answer = "ERROR"

# OUTPUT
print(Name +"asks: "+ Question)

print("Magic 8-Ball's answer:" + Answer )

