# <<This tool is used for educational purpose Only>>
# <<This tools has been made by xXLonelyAlienXx>>


import json
import requests
import time
import os
#------------------------------------------------------------------------------------------------------Clear
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')
#------------------------------------------------------------------------------------------------------Tools
def serverinfo_server():
    clear()
    print("Server Only")
    invite = input("Enter the Discord Server Link : ")
    invite_code = invite.split("/")[-1]

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    data = json.loads(response.text)
    time.sleep(1)
    def organization():
        print("-----------------------------------")
        print(f"Guild >>")
        print("-----------------------------------")
        print(f"id                         :", data["guild"]["id"])
        print(f"name                       :", data["guild"]["name"])
        print(f"splash                     :", data["guild"]["splash"])
        print(f"banner                     :", data["guild"]["banner"])
        print(f"description                :", data["guild"]["description"])
        print(f"icon                       :", data["guild"]["icon"])
        print(f"verification_level         :", data["guild"]["verification_level"])
        print(f"vanity_url_code            :", data["guild"]["vanity_url_code"])
        print(f"nsfw_level                 :", data["guild"]["nsfw_level"])
        print(f"nsfw                       :", data["guild"]["nsfw"])
        print(f"premium_subscription_count :", data["guild"]["premium_subscription_count"])
        print(f"premium_tier               :", data["guild"]["premium_tier"])
        print(f"features                   :", data["guild"]["features"])
        print("-----------------------------------")
        print(f"Channel >>")
        print("-----------------------------------")
        print(f"id                         :", data["channel"]["id"])
        print(f"type                       :", data["channel"]["type"])
        print(f"name                       :", data["channel"]["name"])
        print("-----------------------------------")
        print(f"Server >>")
        print("-----------------------------------")
        print(f"id                         :", data["profile"]["id"])
        print(f"name                       :", data["profile"]["name"])
        print(f"icon_hash                  :", data["profile"]["icon_hash"])
        print(f"member_count               :", data["profile"]["member_count"])
        print(f"online_count               :", data["profile"]["online_count"])
        print(f"description                :", data["profile"]["description"])
        print(f"banner_hash                :", data["profile"]["banner_hash"])
        print(f"game_application_ids       :", data["profile"]["game_application_ids"])
        print(f"game_activity              :", data["profile"]["game_activity"])
        print(f"tag                        :", data["profile"]["tag"])
        print(f"badge                      :", data["profile"]["badge"])
        print(f"badge_color_primary        :", data["profile"]["badge_color_primary"])
        print(f"badge_color_secondary      :", data["profile"]["badge_color_secondary"])
        print(f"badge_hash                 :", data["profile"]["badge_hash"])
        print(f"traits                     :", data["profile"]["traits"])
        print(f"visibility                 :", data["profile"]["visibility"])
        print(f"custom_banner_hash         :", data["profile"]["custom_banner_hash"])
        print(f"premium_subscription_count :", data["profile"]["premium_subscription_count"])
        print(f"premium_tier               :", data["profile"]["premium_tier"])
        print("-----------------------------------")

    organization()
    exit = input("Enter >E< to exit> ")
    if exit in ["e","E"]:
        menu()
    else:
        serverinfo_server()

def serverinfo_sender():
    clear()
    print("Inviter Only")
    invite = input("Enter the Discord Server Link : ")
    invite_code = invite.split("/")[-1]

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    data = json.loads(response.text)
    time.sleep(1)
    def organization():
        print(f"type                   :", data["type"])
        print(f"code                   :", data["code"])
        print(f"expires_at :", data["expires_at"])
        print(f"id :", data["id"])
        print("-----------------------------------")
        print(f"Inviter >>")
        print("-----------------------------------")
        print(f"id                         :", data["inviter"]["id"])
        print(f"username                   :", data["inviter"]["username"])
        print(f"avatar                     :", data["inviter"]["avatar"])
        print(f"discriminator              :", data["inviter"]["discriminator"])
        print(f"public_flags               :", data["inviter"]["public_flags"])
        print(f"flags                      :", data["inviter"]["flags"])
        print(f"banner                     :", data["inviter"]["banner"])
        print(f"accent_color               :", data["inviter"]["accent_color"])
        print(f"global_name                :", data["inviter"]["global_name"])
        print(f"avatar_decoration_data     :", data["inviter"]["avatar_decoration_data"])
        print(f"collectibles               :", data["inviter"]["collectibles"])
        print(f"display_name_styles        :", data["inviter"]["display_name_styles"])
        print(f"vad_colors                 :", data["inviter"]["vad_colors"])
        print(f"banner_color               :", data["inviter"]["banner_color"])
        print(f"clan                       :", data["inviter"]["clan"])
        print(f"primary_guild              :", data["inviter"]["primary_guild"])
        print("-----------------------------------")

    organization()
    exit = input("Enter >E< to exit> ")
    if exit in ["e","E"]:
        menu()
    else:
        serverinfo_sender()


def serverinfo_full():
    clear()
    print("Full")
    invite = input("Enter the Discord Server Link : ")
    invite_code = invite.split("/")[-1]

    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    data = json.loads(response.text)
    time.sleep(1)
    
    def organization():
        print(f"type                   :", data["type"])
        print(f"code                   :", data["code"])
        print(f"expires_at :", data["expires_at"])
        print(f"id :", data["id"])
        print("-----------------------------------")
        print(f"Inviter >>")
        print("-----------------------------------")
        print(f"id                         :", data["inviter"]["id"])
        print(f"username                   :", data["inviter"]["username"])
        print(f"avatar                     :", data["inviter"]["avatar"])
        print(f"discriminator              :", data["inviter"]["discriminator"])
        print(f"public_flags               :", data["inviter"]["public_flags"])
        print(f"flags                      :", data["inviter"]["flags"])
        print(f"banner                     :", data["inviter"]["banner"])
        print(f"accent_color               :", data["inviter"]["accent_color"])
        print(f"global_name                :", data["inviter"]["global_name"])
        print(f"avatar_decoration_data     :", data["inviter"]["avatar_decoration_data"])
        print(f"collectibles               :", data["inviter"]["collectibles"])
        print(f"display_name_styles        :", data["inviter"]["display_name_styles"])
        print(f"vad_colors                 :", data["inviter"]["vad_colors"])
        print(f"banner_color               :", data["inviter"]["banner_color"])
        print(f"clan                       :", data["inviter"]["clan"])
        print(f"primary_guild              :", data["inviter"]["primary_guild"])
        print("-----------------------------------")
        print(f"Guild >>")
        print("-----------------------------------")
        print(f"id                         :", data["guild"]["id"])
        print(f"name                       :", data["guild"]["name"])
        print(f"splash                     :", data["guild"]["splash"])
        print(f"banner                     :", data["guild"]["banner"])
        print(f"description                :", data["guild"]["description"])
        print(f"icon                       :", data["guild"]["icon"])
        print(f"verification_level         :", data["guild"]["verification_level"])
        print(f"vanity_url_code            :", data["guild"]["vanity_url_code"])
        print(f"nsfw_level                 :", data["guild"]["nsfw_level"])
        print(f"nsfw                       :", data["guild"]["nsfw"])
        print(f"premium_subscription_count :", data["guild"]["premium_subscription_count"])
        print(f"premium_tier               :", data["guild"]["premium_tier"])
        print(f"features                   :", data["guild"]["features"])
        print("-----------------------------------")
        print(f"Channel >>")
        print("-----------------------------------")
        print(f"id                         :", data["channel"]["id"])
        print(f"type                       :", data["channel"]["type"])
        print(f"name                       :", data["channel"]["name"])
        print("-----------------------------------")
        print(f"Server >>")
        print("-----------------------------------")
        print(f"id                         :", data["profile"]["id"])
        print(f"name                       :", data["profile"]["name"])
        print(f"icon_hash                  :", data["profile"]["icon_hash"])
        print(f"member_count               :", data["profile"]["member_count"])
        print(f"online_count               :", data["profile"]["online_count"])
        print(f"description                :", data["profile"]["description"])
        print(f"banner_hash                :", data["profile"]["banner_hash"])
        print(f"game_application_ids       :", data["profile"]["game_application_ids"])
        print(f"game_activity              :", data["profile"]["game_activity"])
        print(f"tag                        :", data["profile"]["tag"])
        print(f"badge                      :", data["profile"]["badge"])
        print(f"badge_color_primary        :", data["profile"]["badge_color_primary"])
        print(f"badge_color_secondary      :", data["profile"]["badge_color_secondary"])
        print(f"badge_hash                 :", data["profile"]["badge_hash"])
        print(f"traits                     :", data["profile"]["traits"])
        print(f"visibility                 :", data["profile"]["visibility"])
        print(f"custom_banner_hash         :", data["profile"]["custom_banner_hash"])
        print(f"premium_subscription_count :", data["profile"]["premium_subscription_count"])
        print(f"premium_tier               :", data["profile"]["premium_tier"])
        print("-----------------------------------")


    organization()
    exit = input("Enter >E< to exit> ")
    if exit in ["e","E"]:
        menu()
    else:
        serverinfo_full()
#------------------------------------------------------------------------------------------------------Menu
def menu():
    clear()
    print("""
╔═══════════════════════════════════════════════════════════════════════════════╗
║██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗     ██████╗ ██████╗ ██████╗ ██████╗ ║
║██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗║
║██║██╔██╗ ██║██║   ██║██║   ██║   █████╗█████╗██║     ██║   ██║██████╔╝██║  ██║║
║╚═╝██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝╚════╝██║     ██║   ██║██╔══██╗██║  ██║║
║██╗██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ╚██████╗╚██████╔╝██║  ██║██████╔╝║
║╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ║
╚═══════════════════════════════════════════════════════════════════════════════╝

-Made by xXLonelyAlienXx

[1] -Full 
[2] -Inviter only
[3] -Server Only 

[0] --exit
""")
    print(f'<What is this guild?>')
    choice = input(f'└───➤')
    if choice == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Goodbye!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()  
    elif choice == "1":
        serverinfo_full()
    elif choice == "2":
        serverinfo_sender()
    elif choice == "3":
        serverinfo_server()


    else:
        clear()
        print("Option Invalid")
        time.sleep(1)
        print("Reset Menu")
        clear()
        menu()


#------------------------------------------------------------------------------------------------------Run
if __name__ == "__main__":
    menu()

#------------------------------------------------------------------------------------------------------Run
if __name__ == "__main__":
    menu()
