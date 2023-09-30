import os
from pyexpat import model
try:
	color_table = "#00FF00"
except FileNotFoundError:
	color_table = "#00FF00"
#--(Dark@Colours)---#
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
s="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;92m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[38;5;208m"
#--(rare-colors)--#
holaa="38;5"
ro=(f"\033[{holaa};208")
rb=(f"\033[{holaa};32")
rc=(f"\033[{holaa};122m")
rg= (f"\033[{holaa};112m")
rp=(f"\033[{holaa};147m") 
os.system("clear")
logo = ("""
\033[1;91m                            ─━㋱ASSALAMUALAIKUM㋱━─ 
  \033[1;90m                         
  \033[1;91m
  \033[1;91m   ##     ##  ##  ##         ## ###### ##      
  \033[1;92m   ##     ##  ##  ####     #### ##     ##       
  \033[1;95m   ##     ##  ##  ##  ##  ## ## ##     ##      
  \033[1;96m   #########  ##  ##    ##   ## ###### ##      
  \033[1;97m   ##     ##  ##  ##         ## ##     ##     
  \033[1;98m   ##     ##  ##  ##         ## ##     ##      
  \033[1;92m   ##     ##  ##  ##         ## ###### #########
  \033[1;99m
   \033[1;91m          Hard Woark kye to sucees(KING-HIMEL32)
  \033[1;92;1m                      
                                    ## HIMEL-HACKER##
  
  [∆]\033[1;96;1m Author   :KING-HIMEL32
  [∆]\033[1;93;1m Facebook :mdnx.himel32
  [∆]\033[1;94;1m Whatsapp : 01601161609
  [∆]\033[1;91;1m GitHub   : Kinghimel-32
  [∆]\033[1;92;1m Virson   : KH32.0.20""")
 



def linex():
	print('\033[1;32m==========================================')
def lines():
	print('\033[1;32m==========================================')
os.system("clear")
print(logo)
def generate_samsung_user_agent():
    samsung_models = [
        "Galaxy S21",
        "Galaxy S20",
        "Galaxy Note 20",
        "Galaxy Note 10",
        "Galaxy A71",
        "Galaxy A51",
        "Galaxy Tab S7",
        "Galaxy Tab S6",
        "Galaxy Watch 4",
        "Galaxy Watch Active 2",
    ]
    
    android_versions = [
        "10.0; Android",
        "11.0; Android",
        "12.0; Android",
    ]
    
    samsung_browsers = [
        "Chrome/90.0.4430.93",
        "Chrome/91.0.4472.164",
        "Firefox/89.0",
        "Firefox/90.0",
        "SamsungBrowser/14.0",
        "SamsungBrowser/15.0",
    ]
    
    model = os.choice(samsung_models)
    android_version = os.choice(android_versions)
    browser = os.choice(samsung_browsers)
    
    user_agent = f"Mozilla/5.0 ({model}; {android_version}; SM-G977B) AppleWebKit/537.36 (KHTML, like Gecko) {browser} Safari/537.36"
    
    return user_agent
 
 
def generate_user_agents(num_agents):
    user_agents = []
    
    for _ in range(num_agents):
        user_agent = generate_samsung_user_agent()
        user_agents.append(user_agent)
    
    return user_agents
 
 
# Option 1: Generate a specific number of user agents
num_agents = int(input("Enter LIMIT: "))
user_agents = generate_user_agents(num_agents)
 
print("Generated User Agents:")
for ua in user_agents:
    print(ua)
 
 
# Option 2: Generate unlimited user agents
unlimited_option = input("Do you want to create unlimited user agents? (yes/no): ")
 
if unlimited_option.lower() == "yes":
    while True:
        user_agent = generate_samsung_user_agent()
        print(user_agent)
        next_option = input("Generate another user agent? (yes/no): ")
        
        if next_option.lower() != "yes":
            break
else:
    print("Script execution completed.")
    user_agent = f"{logo}\nMozilla/5.0 ({model};"
