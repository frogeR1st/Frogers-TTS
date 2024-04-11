#imports
#   custom
import FrogersToolkitV1

import pytchat
from gtts import gTTS
import os

#vars
#   imports
ft = FrogersToolkitV1.FT

#   settings
points = False
all_messages = False
URL = "zH7eNxmVAhA"

#   live stream
chat = pytchat.create(video_id=URL)


#   people
banned = open(ft.to_file("permisions\\banned.py"))
mods = open(ft.to_file("permisions\\mod.py"))
owner = open(ft.to_file("permisions\\owner.py"))

bannedR = banned.read()
modsR = mods.read()
ownerR = owner.read()

#   commands
cm_text_to_speach = "!"

#   points
points_to_tts = 10
points_to_sfx = 20
starting_points = 100

file_name = "message.mp3"

#def
def add_points(username, add_points):
    try:
        user_file = ft.to_file(f"other save files\\points\\{username}.txt")
        user_file_opened = open(user_file)
        user_file_set = int(user_file_opened.read()) + add_points



        with open(user_file, "w") as file:
            file.write(str(user_file_set))

    except FileNotFoundError:
        if add_points <= 1:
            with open(user_file, "w") as file:
                file.write(str(starting_points))
        else:
            with open(user_file, "w") as file:
                file.write(str(starting_points + add_points))

    except FileExistsError:
        print("file existance error")

def get_points(username):
    try:
        user_file = open(ft.to_file(f"other save files\\points\\{username}.txt"))
    
        return(user_file.read())
    except FileNotFoundError:
        print("cant do that")


def playtts(mess : str, lang : str, slow : bool):
    global file_name

    tts = gTTS(mess, lang=lang, slow=slow)

#   Save the speech to an audio file
    tts.save(file_name)

#   Play the audio file
    os.system("start message.mp3")

#class

#main
print(banned.read())
print(mods.read())
print(owner.read())

while chat.is_alive:
    for comment in chat.get().sync_items():

        print(f"Delta Time: {comment.datetime}, Name: {comment.author.name}, Message: {comment.message}")

#       points
        add_points(comment.author.name, 1)


#       chechs for permisions
        if comment.author.name in ownerR:

            if "//owner" in comment.message:
                user = comment.message[8:]
                with open(ft.to_file("permisions\\owner.py"), "w") as file:
                    ownerR = ownerR[:-1] + f"{user}, ]"
                    file.write(ownerR)
            elif "//addSP" in comment.message:
                user = comment.message[8:]
                print(user)
                add_points(user, 100)

            elif "//subSP" in comment.message:
                user = comment.message[8:]
                add_points(user, -100)



        if comment.author.name in modsR:

            if "/ban" in comment.message:
                user = comment.message[5:]
                with open(ft.to_file("permisions\\banned.py"), "w") as file:
                    bannedR = bannedR[:-1] + f"{user}, ]"
                    file.write(bannedR)

            elif "/mod" in comment.message:
                user = comment.message[5:]
                with open(ft.to_file("permisions\\mod.py"), "w") as file:
                    modsR = modsR[:-1] + f"{user}, ]"
                    file.write(modsR)

            elif "/addP" in comment.message:
                user = comment.message[6:]
                print(user)
                add_points(user, 10)

            elif "/subP" in comment.message:
                user = comment.message[6:]
                add_points(user, -10)

        if not comment.author.name in bannedR:
#           SFX
            if "@sadtrombone" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\sad.mp3")

            if "@fail" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))
                os.system(f"start files\SFX\Fail.mp3")

            if "@tf2fail" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))
                os.system(f"start files\SFX\TF2_Fail.mp3")

            if "@gta" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))
                os.system(f"start files\SFX\GTA_Wasted.mp3")

            if "@metal" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))
                os.system(f"start files\SFX\MetalPip.mp3")

            if "@sadviolin" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\sad2.mp3")

            if "@spongesad" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\SpongeSad.mp3")

            if "@stink" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\Stinks.mp3")

            if "@nuthing" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\\SFX\\nuthing.mp3")

            if "@squash" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\squash.mp3")

            if "@zorbeez" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\Zorbeez.mp3")

            if "@shoot" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\Sniper.mp3")

            if "@celebration" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\celebration.mp3")
                
            if "@standing" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\Standing.mp3")

            if "@dougdougzorbeez" in str(comment.message).lower():
                if points is True:
                    add_points(comment.author.name, (-points_to_sfx - 1))

                os.system(f"start files\SFX\ZorbeezDoug.mp3")

#           TTS
            if all_messages is True:
                add_points(comment.author.name, (-points_to_tts - 1))
                playtts(f"From {comment.author.name}, {comment.message}", "en", False)

            elif points is False:
                if ft.has(cm_text_to_speach, comment.message)[0] is True:
                    if ft.has(cm_text_to_speach, comment.message)[1] == 0:
                        playtts(f"From {comment.author.name}, {comment.message}", "en", False)

            elif points is True:
                if int(get_points(comment.author.name)) >= points_to_tts:
                    if ft.has(cm_text_to_speach, comment.message)[0] is True:
                        if ft.has(cm_text_to_speach, comment.message)[1] == 0:
                            add_points(comment.author.name, (-points_to_tts - 1))
                            playtts(f"From {comment.author.name}, {comment.message}", "en", False)



banned.close()
mods.close()
owner.close()
