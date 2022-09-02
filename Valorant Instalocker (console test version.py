import pyautogui
import os
import keyboard
import time

#Agents Names

Agents = [
    "Jett", "Raze", "Breach", "Omen", "Brimstone", "Phoenix", "Sage", "Sova", "Viper", 
    "Cypher", "Reyna", "Killjoy", "Skye", "Yoru", "Astra", "KAY/O", "Chamber", "Neon", "Fade"
]


askLoop = True
while askLoop:
    resAsk = input("Select your resolution game\n(0) = 1920 x 1080\n(1) = 1440 x 1080\n: ")
    if resAsk == "0":
        notStretched = True
        Stretched = False
        askLoop = False
        os.system("cls")
    elif resAsk == "1":
        notStretched = False
        Stretched = True
        askLoop = False
        os.system("cls")
    else:
        print("\nPlease Enter '0' or '1' to select your resolution, nothing else.\n")   

agentChoose = ""

def NotStretchedAgentPick():
    lockbtn = 930, 810
    
    #Agents coordinates
    astra = 561, 911
    breach = 647, 911
    brimstone = 733, 911
    chamber = 821, 911
    cypher = 898, 911
    fade = 991, 911
    jett = 1073, 911
    kayo = 1167, 911
    killjoy = 1234, 911
    neon = 1319, 911
    omen = 554, 980
    phoenix = 647, 980
    raze = 737, 980
    reyna = 820, 980
    sage = 902, 980
    skye = 982, 980
    sova = 1072, 980
    viper = 1154, 980
    yoru = 1249, 980
    
    if agentChoose == Agents[0]:
        pyautogui.moveTo(jett)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[1]:
        pyautogui.moveTo(raze)
        time.sleep(0.01)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[2]:
        pyautogui.moveTo(breach)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[3]:
        pyautogui.moveTo(omen)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[4]:
        pyautogui.moveTo(brimstone)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[5]:
        pyautogui.moveTo(phoenix)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[6]:
        pyautogui.moveTo(sage)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[7]:
        pyautogui.moveTo(sova)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[8]:
        pyautogui.moveTo(viper)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[9]:
        pyautogui.moveTo(cypher)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[10]:
        pyautogui.moveTo(reyna)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[11]:
        pyautogui.moveTo(killjoy)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[12]:
        pyautogui.moveTo(skye)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[13]:
        pyautogui.moveTo(yoru)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[14]:
        pyautogui.moveTo(astra)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[15]:
        pyautogui.moveTo(kayo)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[16]:
        pyautogui.moveTo(chamber)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[17]:
        pyautogui.moveTo(neon)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[18]:
        pyautogui.moveTo(fade)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    
def StretchedAgentPick():
    lockbtn = 724, 819
    
    #Agents coordinates
    astra = 322, 911
    breach = 411, 911
    brimstone = 507, 911
    chamber = 592, 911
    cypher = 660, 911
    fade = 760, 911
    jett = 842, 911
    kayo = 920, 911
    killjoy = 995, 911
    neon = 1090, 911
    omen = 333, 1000
    phoenix = 418, 1000
    raze = 528, 1000
    reyna = 590, 1000
    sage = 646, 1000
    skye = 750, 1000
    sova = 810, 1000
    viper = 920, 1000
    yoru = 990, 1000
    
    if agentChoose == Agents[0]:
        pyautogui.moveTo(jett)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[1]:
        pyautogui.moveTo(raze)
        time.sleep(0.01)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[2]:
        pyautogui.moveTo(breach)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[3]:
        pyautogui.moveTo(omen)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[4]:
        pyautogui.moveTo(brimstone)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[5]:
        pyautogui.moveTo(phoenix)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[6]:
        pyautogui.moveTo(sage)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[7]:
        pyautogui.moveTo(sova)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[8]:
        pyautogui.moveTo(viper)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[9]:
        pyautogui.moveTo(cypher)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[10]:
        pyautogui.moveTo(reyna)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[11]:
        pyautogui.moveTo(killjoy)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[12]:
        pyautogui.moveTo(skye)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[13]:
        pyautogui.moveTo(yoru)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[14]:
        pyautogui.moveTo(astra)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[15]:
        pyautogui.moveTo(kayo)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[16]:
        pyautogui.moveTo(chamber)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[17]:
        pyautogui.moveTo(neon)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()
    if agentChoose == Agents[18]:
        pyautogui.moveTo(fade)
        pyautogui.click()
        pyautogui.moveTo(lockbtn)
        pyautogui.click()

if notStretched == True:
    askLoop = True
    while askLoop:
        print(*Agents, sep = ', ')
        agentChoose = input("Choose your Agent : ")
        
        if agentChoose in Agents:
            print("\nOk, the script will instalock : {}".format(agentChoose))
            askLoop = False
            keyboardLoop = True
            restartInstalock = True
            print("\nPress/Hold F2 in game to activate the instalock script !")
            print("\nPress F4 to quit the script.\n")
            while keyboardLoop:
                if keyboard.is_pressed('F2'):
                    print("\nInstalock Done !\n")
                    NotStretchedAgentPick()
                    keyboardLoop = False
                if keyboard.is_pressed('F4'):
                    print("\nThanks For using my script, \nGood Bye !")
                    quitLoop = False
                    quit()
                    
            print("Press/Hold F2 again if you want to restart the instalocker with the same agent (=if you start a new game).")
            
            while restartInstalock:
                if keyboard.is_pressed('F2'):
                    print("\nInstalock Done !")
                    print("Press F4 to quit the script.\n")
                    NotStretchedAgentPick()
                if keyboard.is_pressed('F4'):
                    print("\nThanks For using my script, \nGood Bye !")
                    quit()
            
        else:
            print("\nIncorrect Agent name, Please try again.\n")

if Stretched == True:
    askLoop = True
    while askLoop:
        print(*Agents, sep = ', ')
        agentChoose = input("Choose your Agent : ")
        
        if agentChoose in Agents:
            askLoop = False
            keyboardLoop = True
            restartInstalock = True
            print("\nPress/Hold F2 in game to activate the instalock script !")
            print("\nPress F4 to quit the script.\n")
            while keyboardLoop:
                if keyboard.is_pressed('F2'):
                    print("\nInstalock Done !\n")
                    StretchedAgentPick()
                    keyboardLoop = False
                if keyboard.is_pressed('F4'):
                    print("\nThanks For using my script, \nGood Bye !")
                    quitLoop = False
                    quit()
                    
            print("Press/Hold F2 again if you want to restart the instalocker with the same agent (=if you start a new game).")
            
            while restartInstalock:
                if keyboard.is_pressed('F2'):
                    print("\nInstalock Done !")
                    print("Press F4 to quit the script.\n")
                    StretchedAgentPick()
                if keyboard.is_pressed('F4'):
                    print("\nThanks For using my script, \nGood Bye !")
                    quit()
                    
                    
        else:
            print("\nIncorrect Agent name, Please try again.\n")