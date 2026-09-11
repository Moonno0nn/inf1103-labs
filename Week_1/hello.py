###Activity 1: Creating your first Python program and add it to the repository
print("========================")
print("Welcome here")
print("My first post!")
print("========================")

## Activity 2: Update your Profile and add it to the repository
username = "cool_creator"
bio = "Fun Blogger"
followers = 100

print("Username:", username)
print("Bio:", bio)
print("Followers:", followers)

##Activity 3: Follower growth tracker
followers += 50
print("Day 1:", followers)

followers += 20 
print("Day 2:", followers)

followers -= 10 
print("Day 3:", followers)

##Interactive Profiles Creator
username = input("Enter Username: ")
age = int(input("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("==============================")
print("Username: ", username)
print("Age: ", age)
print("Category:", category)

#Activity 5: Something fun to think about. 
if age>40 and category == "fun":
    print("You are old what is fun for you?? This is mean")
