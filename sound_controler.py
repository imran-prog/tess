from datetime import date
from sound import Sound


def sound_control():
    while True:
        '''
        print("Choose an option:")
        print("1] Mute / Unmute volume")
        print("2] Increase volume")
        print("3] Decrease volume")
        print("4] Set volume to 0")
        print("5] Set volume to 100")
        print("6] Set volume to ...")
        print("7] Print sound settings")
        print("8] Quit")
        print("")
        '''

        option = input("> ")
        '''
        if option == "1":
            Sound.mute()
            continue

        elif option == "2":
            Sound.volume_up()
            continue

        elif option == "3":
            Sound.volume_down()
            continue

        elif option == "4":
            Sound.volume_min()
            continue

        elif option == "5":
            Sound.volume_max()
            continue
        '''
        # elif option == "6":
        volume = int(input("Volume (0 - 100): "))
        Sound.volume_set(volume)
        continue

sound_control()