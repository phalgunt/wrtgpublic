print("Enter your name:")
x = input()
trex=0
argentinosaurus=0
velociraptor=0
oculudentavis=0
pterodactyl=0
spinosaurus=0
print("Hello, " + x + " I need you to answer a few yes or no questions, and from this I can tell you which dinosaur you are(make sure everything is in lower case)")

tall = input("Are you above 5 feet? ")
if tall=='yes':
    argentinosaurus+=1
    spinosaurus+=1

small = input("Are you below 4 feet? ")
if small=='yes':
    oculudentavis+=1

hunt=input("Have you ever gone hunting? ")
if hunt=='yes':
    trex+=1
    pterodactyl+=1
    spinosaurus+=1

flight=input("Do you enjoy flying? ")
if flight=='yes':
    pterodactyl+=1
    oculudentavis+=1

swim=input("Do you enjoy swimming? ")
if swim=='yes':
    spinosaurus+=1

speed=input("Can you run fast? ")
if speed=='yes':
    velociraptor+=1
    trex+=1

vegeterian=input("Are you vegetarian or vegan? ")
if vegeterian=='yes':
    argentinosaurus+=1

fishing=input("Have you ever gone fishing? ")
if fishing=='yes':
    spinosaurus+=1

fight=input("Have you ever gotten into a fight? ")
if fight=='yes':
    trex+=1
    velociraptor+=1
    pterodactyl+=1

#print("Thank you for playing this game, now lets see which dinosaur you most resemble!")
#list1=[trex, argentinosaurus, velociraptor, oculudentavis, pterodactyl, spinosaurus]

var = {trex:"trex",argentinosaurus:"argentinosaurus",velociraptor:"velociraptor",oculudentavis:"oculudentavis",pterodactyl:"pterodactyl",spinosaurus:"spinosaurus"}
print("Your dinosaur is: ", var.get(max(var)))
