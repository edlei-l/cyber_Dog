class Dog:
    def __init__(self,name,mood,energy):
        self.name=name
        self.mood=mood
        self.energy=energy
    def chat(self):
        self.energy=self.energy-10
        if self.mood>80:
            print(f"[chat]mood={self.mood}\n[chat]energy={self.energy}")
            print("I am happy now")
        elif  self.mood<50 :
           print(f"[chat]mood={self.mood}"+"\n[chat]energy={self.energy}")
           print("perfunctory....")
        else:
            print(f"[chat]mood={self.mood}\n[chat]energy={self.energy}")
            print(f"{self.name} was not bad,but not good either")
    def sleep(self):
        self.energy+=50
        print(f"{self.name} is sleeping\n[energy]={self.energy}\n[mood]={self.mood}")
    def work(self):
        self.mood-=20
        self.energy-=30
        print(f"{self.name} is working very hard...")
        print(f"[work]mood={self.mood}")
        print(f"[work]energy={self.energy}")
name=input("please enter the name of your dog\n")
mood=int(input("mood value\n"))
energy=int(input("energy value\n"))
while mood>100 or mood<0:
    print(" ERROR!!!! mood value should be between 0 and 100")
    mood=int(input("please enter a valid mood value\n"))
while energy>100 or energy<0:
    print("ERROR!!! the energy value must between 0 and 100")
    energy=int(input("please enter the right energy value"))
my_Dog=Dog(name,mood,energy)
while True:
    print("Welcome to the cyber-Dog,enter the number to enjoy the game!!!\n\tNO1.chat\n\tNo2.sleep\n\tNo3.work\n\tNo0.exit")
    option=int(input())
    if option==1:
        my_Dog.chat()
        if my_Dog.energy<=0:
            print(f"{my_Dog.name} is tired")
            break
    elif option==2:
        my_Dog.sleep()
        if my_Dog.energy<=0:
            print(f"{my_Dog.name} is tired")
            break
        elif my_Dog.energy>100:
            my_Dog.energy=100
            print(f"The max energy value is 100!!!\n[energy]={my_Dog.energy}\n[mood]={my_Dog.mood}")
    elif option==3:
        my_Dog.work()
        if my_Dog.energy<=0:
            print(f"{my_Dog.name} is tired")
            break
    elif option==0:
        break