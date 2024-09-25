import random as r
import time as t
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys 
from pathlib import Path
import pwnedpasswords
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#---------------------------------------------------------------------------------------------------------------------

def analysing(password):
    score = 0
    upper = 0
    lower = 0
    special = 0
    digits = 0
    space = 0
    

    for i in password:
        if(i.isupper()):
            upper += 1
        elif(i.islower()):
            lower += 1
        elif(i in "!@#$%^&*()-_+=|\;:><,.?/" or i == "\'" or i == "\""):
            special += 1
        elif(i in "0123456789"):
            digits += 1
        elif(i == " "):
            space += 1 
        else:
            continue

    if(len(password)>=12):
        score = 12
        score += upper*2
        score += lower*2
        score += special*6
        score += digits*4
        score += space*6
    elif(len(password)<12 and len(password)>=8):
        score = 5
        score += upper*2
        score += lower*2
        score += special*6
        score += digits*4
        score += space*6
    elif(len(password)<8 and len(password)>=5):
        score = 4
        score += upper*2
        score += lower*2
        score += special*4
        score += digits*3
        score += space*4
    elif(len(password)<5 and len(password)>=1):
        score = 2
        score += upper*2
        score += lower*2
        score += special*4
        score += digits*3
        score += space*4
    else:
        pass
    return(score)

#--------------------------------------------------------------------------------------------------------------------------------
def console(password12):
    while True:
        pwned = int(pwnedpasswords.check(password12))
        if pwned == 0:
            print("Your password is secure! No leaks detected. If you still doubt this, go and do an advanced security check\n")
        else:
            print("OH NO! The password '{}' has been leaked {} times\n".format(password12,str(pwned)))
        return   

#------------------------------------------------------------------------------------------------------------------------------------

def cracker():
    choice = input("\nEnter choice \nNUMBERS\nCOMBINATION\n:: ")
    if(choice == "numbers" or choice == "number"):
        guess = int(input("Enter the password : "))
        begin = t.time()
        for i in range(1,100000000000):
            if(guess == i):
                end = t.time()
                print("The password is cracked in",end-begin,"seconds")
                break
        return
    elif(choice == "combination" or choice == "combinations"):
        common_passwords = ["123456","password","123456789","12345678","12345","1234567","1234567","qwerty","abc123","admin","letmein","welcome","monkey","password1","sunshine","iloveyou",  "superman",  "123123", "football", "baseball","password123","shadow", "1234", "dragon","michael", "football", "master","jennifer","harley", "hunter", "batman", "trustno1", "starwars", "whatever", "1234567890", "password!", "1234567", "password1", "admin123", "letmein123", "welcome123", "sunshine123", "iloveyou123", "superman123", "123123123", "football123","baseball123","password1234", "shadow123","12341234",]
        driver = webdriver.Firefox()
        driver.get("file:///c://programming/python/python/files/python%20projects/secure%20password%20analyser/loginforcracking.html")
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        submitting = driver.find_element(By.ID, "submmit")
        temp = input('Enter the username: ')
        result = driver.find_element(By.ID, "result")
        input("Press Enter to continue...")
        begin = t.time()
        for i in range(0,len(common_passwords)):
            username.send_keys(temp)
            password.send_keys(common_passwords[i])
            submitting.click()
            username.clear()
            password.clear()
            coming = result.text
            if("AUTHORIZED" in coming):
                 end = t.time()
                 print("Password cracked in", end - begin, "seconds\nThe cracked password is : ",common_passwords[i],"\n")
                 break
            else:
                print("failed !!")
            t.sleep(1)
            continue
        t.sleep(5)
        driver.quit()
        return
    else:
        return

#------------------------------------------------------------------------------------------------------------------------------------

def analysisofpassword():
    data = pd.read_csv("C:\\programming\\python\\python\\files\\python projects\\secure password analyser\\common_passwords.csv")
    sample_size = 1000
    sampled_data = data.sample(sample_size, random_state=42)
    password_lengths = sampled_data['length']
    plt.figure(figsize=(10, 6))
    plt.hist(password_lengths, bins=np.arange(1, 18), edgecolor='black', alpha=0.7, color='skyblue') 
    plt.xlabel('Password Length')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {sample_size} Sampled Passwords')
    plt.grid(axis='y', linestyle='--', alpha=0.5)  
    plt.xticks(np.arange(1, 18))  
    plt.yticks(np.arange(0, 450, 50))  
    plt.tight_layout() 
    plt.show()
    leakedpasswords = pd.read_csv("C:\\programming\\python\\python\\files\\python projects\\secure password analyser\\common_passwords.csv")
    df = pd.DataFrame({"password": leakedpasswords["password"]})
    password_lengths = df["password"].apply(len)
    plt.figure(figsize=(10, 6))
    plt.hist(password_lengths, bins=range(1, 18), edgecolor="black", alpha=0.7, color="salmon")
    plt.xlabel("Password Length")
    plt.ylabel("Frequency")
    plt.title("Distribution of Password Lengths")
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.xticks(range(1, 18))
    plt.tight_layout()
    plt.show()
    leakedpasswords = pd.read_csv("C:\\programming\\python\\python\\files\\python projects\\secure password analyser\\common_passwords.csv")
    df = pd.DataFrame({"password": leakedpasswords["password"]})
    weak_length = 6
    medium_length = 10
    df["strength"] = pd.cut(df["password"].apply(len), bins=[0, weak_length, medium_length, float("inf")], labels=["Weak", "Medium", "Strong"])
    strength_counts = df["strength"].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(strength_counts.index, strength_counts.values, color="purple", edgecolor="black")
    plt.xlabel("Password Strength")
    plt.ylabel("Frequency")
    plt.title("Distribution of Password Strengths")
    plt.tight_layout()
    plt.show()
    return

#------------------------------------------------------------------------------------------------------------------------------------
def generator():
    choice = 0
    passwor = ''
    for i in range(0,17):
        lists = [["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y',"z"],["0",'1','2','3','4','5','6','7','8',"9"],["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',"Z"],["!",'@','#','$','%','^','&','*','(',')','\{','\}','<','>',',','.','?','|',"\\"]]
        choice = r.randint(0,3)
        element = lists[choice]
        passwor += (r.choice(element))
    print("The password is : ",passwor)
    return

#------------------------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------PASSWORD STRENGTH EVALUATOR AND PASSWORD CRACKER------------------------------------------------\n")
while(True):
    choice =input("\nEnter the action ---\n1.Generating Password\n2.Analysing Password\n3.Common Passwords analysis\n4.Crack Password\n:: ")
    if(choice == '1'):
        generator()
    elif(choice == '2'):
        password = input("Enter the password : ")
        score = analysing(password)
        if(score>=0 and score<=13):
            print("\nThe password is VERY WEAK :(\n")
        elif(score>13 and score<=23):
            print("\nThe password is WEAK :(\n")
        elif(score>23 and score<=33):
            print("\nThe password is INTERMEDIATE ^_^\n")
        elif(score>33 and score<=45):
            print("\nThe password is STRONG :)\n")
        elif(score>45):
            print("\nThe password is VERY STRONG :))\n")
        console(password)
    elif(choice == "exit"):
        break
    elif(choice == "3"):
        analysisofpassword()
    elif(choice == "4"):
        cracker()
    else:
        pass
print("------------------------------------------------------------------------------------------------------------------------------------")