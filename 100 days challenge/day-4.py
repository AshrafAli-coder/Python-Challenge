import random
rock='''
    -------
---'   ____)
      (_____)
      (______)
      (_____)
---.__(____)
'''
paper='''
    -------
---'  ____)____
         ______)
         _______)
---.__________)      
'''
scissor='''
    -------
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
hand_image=[rock,paper,scissor]
gesture=["Rock","Paper","Scissor"]
print("Welcome to the Rock Paper Scissor Game.\n")
print("Rock=0,Paper=1,Scissor=2\n")
user=int(input("Choose your move: "))
if user>3:
    print("Invalid Choice. You lose.")
else:
    computer=random.randint(0,2)
    if user==computer:
        print(f"You Choose: {gesture[user]}\n{hand_image[user]}\nComputer Choice: {gesture[computer]}\n{hand_image[user]}\n")
        print("It's a Draw.")
    elif user==0 and computer==1:
        print(f"You Choose: {gesture[user]}\n{hand_image[0]}\nComputer Choice: {gesture[computer]}\n{hand_image[1]}\n")
        print("You loose!!!")
    elif user==0 and computer==2:
        print(f"You Choose: {gesture[user]}\n{hand_image[0]}\nComputer Choice: {gesture[computer]}\n{hand_image[2]}\n")
        print("You Win!!!!")
    elif user==1 and computer==0:
        print(f"You Choose: {gesture[user]}\n{hand_image[1]}\nComputer Choice: {gesture[computer]}\n{hand_image[0]}\n")
        print("You Win!!!!")
    elif user==1 and computer==2:
        print(f"You Choose: {gesture[user]}\n{hand_image[1]}\nComputer Choice: {gesture[computer]}\n{hand_image[2]}\n")
        print("You loose!!!")
    elif user==2 and computer==0:
        print(f"You Choose: {gesture[user]}\n{hand_image[2]}\nComputer Choice: {gesture[computer]}\n{hand_image[0]}\n")
        print("You loose!!!")
    elif user==2 and computer==1:
        print(f"You Choose: {gesture[user]}\n{hand_image[2]}\nComputer Choice: {gesture[computer]}\n{hand_image[1]}\n")
        print("You Win!!!!")
    else:
        print("Invalid Choice...")