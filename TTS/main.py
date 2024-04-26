#custom
from FrogersToolkitV1 import FT
#imports
from gtts import gTTS
import pytchat
import os
import time

#vars
running = True
URL = "YNvAxdTxNF8"
file_name = "message.mp3"

verified_players = []

#settings
play_all_messages = False

owner = True
mods = True
verified = True
normal = True


#inits
chat = pytchat.create(video_id=URL)
ft = FT

#def
def playtts(mess : str, lang : str, slow : bool):
    global file_name

    tts = gTTS(mess, lang=lang, slow=slow)

#   Save the speech to an audio file
    tts.save(file_name)

#   Play the audio file
    os.system(f"start {file_name}")

def playsfx(reletive_file : str):
    os.system(f"start {ft.to_file(reletive_file)}")

#main
while running:
            while chat.is_alive():
                    for comment in chat.get().sync_items():
                        allowed = False
    #                  prints message info
                        print(">--comment print--<")
                        print(f"message: {comment.message}, name: {comment.author.name}")
                        print(f"owner: {comment.author.isChatOwner}, verified: {comment.author.isVerified}, mod: {comment.author.isChatModerator}")
                        print(f"type of message: {comment.type}")
                        #print()
                        #print(f"json: {comment.json()}")
                        #print()
                        print(">--end--<")

                        if comment.author.isChatOwner and owner is True:
                            allowed = True
                            print("owner")

                        elif comment.author.isVerified and verified is True:
                            allowed = True

                        elif comment.author.isChatModerator and mods is True:
                            allowed = True
                            print("mod")

                        else:
                            if normal is True:
                                allowed = True
                            else:
                                allowed = False

                        print(allowed)
                        if allowed == True:
    #                  tts
                            if play_all_messages is False:
                                if comment.message[slice(0,1)] == "!":
                                    playtts(f"name {comment.author.name}   {comment.message}", "en", False)
                            else:
                                playtts(f"name {comment.author.name}   {comment.message}", "en", False)

    #                  sfx
    #                      Fail
                            if "#fail" in str(comment.message).lower():
                                playsfx("SFX\\fail\\TF2_Fail.mp3")
                            elif "#gta" in str(comment.message).lower():
                                playsfx("SFX\\fail\\GTA_Wasted.mp3")

    #                      Celebration
                            elif "#yay" in str(comment.message).lower():
                                playsfx("SFX\\Celebration\\Celebration.mp3")

    #                      popular
                            elif "#nuthing" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Nuthing.mp3")
                            elif "#squash" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Squashing_Time.mp3")
                            elif "#standing" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Standing.mp3")
                            elif "#stinks" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Stinks.mp3")
                            elif "#fnaf" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\FNAF.mp3")
                            elif "#sonic.exe" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Sonic.exe.mp3")
                            elif "#or_is_it" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Vsauce_Song.mp3")
                            elif "#hey" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Hey.mp3")
                            elif "#strike" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Wiii_bowling.mp3")
                            elif "#sonic_drown" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Drowning.mp3")
                            elif "#papyrus" in str(comment.message).lower():
                                playsfx("SFX\\Popular\\Papyrus.mp3")

    #                      sad
                            elif "#sadtrombone" in str(comment.message).lower():
                                playsfx("SFX\\Sad\\SadTrombone.mp3")
                            elif str(comment.message).lower() == "#sadviolin":
                                playsfx("SFX\\Sad\\Sadviolin.mp3")

    #                      sfx
                            elif "#shoot" in str(comment.message).lower():
                                playsfx("SFX\\SFX\\SniperShot.mp3")
                            elif "#car" in str(comment.message).lower():
                                playsfx("SFX\\SFX\\Car.mp3")
                            elif "#microwave" in str(comment.message).lower():
                                playsfx("SFX\\SFX\\Microwave.mp3")
                            elif "#cricket" in str(comment.message).lower():
                                playsfx("SFX\\SFX\\Cricket.mp3")

    #                    WHY!!!
                            elif "#metal" in str(comment.message).lower():
                                playsfx("SFX\\WHY!!!!!!\\MetalPip.mp3")
                            
    #                       mod/owner only
                            if comment.author.isChatOwner is True or comment.author.isChatModerator is True:
                                if "#zorbeez" in str(comment.message).lower():
                                    playsfx("SFX\\Long\\Zorb.mp3")
                                elif "#sans_undertale" in str(comment.message).lower():
                                    playsfx("SFX\Long\Mega.mp3")
                                elif "#prowler" in str(comment.message).lower():
                                    playsfx("SFX\Long\Prowler.mp3")
                                elif "#papyrus_undertale" in str(comment.message).lower():
                                    playsfx("SFX\\Popular\\bonetrousle.mp3")
                                elif "#undyne" in str(comment.message).lower():
                                    playsfx("SFX\\Popular\\undyne.mp3")

            print("tts stoped")
            playsfx("SFX\\fail\\Fail.mp3")
            time.sleep(5)
            