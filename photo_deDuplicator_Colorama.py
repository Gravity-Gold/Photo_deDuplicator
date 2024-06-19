from tkinter import filedialog
from PIL import Image
import imagehash
import os
from colorama import Fore, Back, Style
from export_Report import exportCSV, exportHTML
images = {}
dupImages = {}
path = "C:\\IMAGES" #location of the image folder on my computer, for testing purposes

## If you want a version without colorama, I can put a version of the code without it on my github ##

def reportOpt():
    global images,dupImages,path
 
    print(f"||=================================||")    
    print(f"    [0] {Fore.YELLOW} What does it do? {Fore.RESET}")
    print(f"||=================================||")
    print(f"    [1] {Fore.YELLOW} CSV export{Fore.RESET}")
    print(f"    [2] {Fore.YELLOW} HTML export{Fore.RESET}")
    print(f"    [3] {Fore.YELLOW} placeholder{Fore.RESET}")
    print(f"||=================================||")
    print(f"    [4] {Fore.YELLOW} Return\n{Fore.RESET}\n")
    
    choice = input("    ")
    print("\n\n")
    port = 8000

    if choice == '0':
        print("[Press ENTER to move dialogue forward]\n")
        input()
        print(Fore.YELLOW + "There are options to export in both CSV, and HTML format.\n")
        input()
        print("A CSV file is a simplified version of the file format used by Excel, which stores Comma Seperate Values")
        print("It can be used to contain simple strings of data, such as this. The program will create a new file in\nthe same directory it is stored in.")
        print("You can choose the files name, it is recommended that you make the names unique and meaningful.")
        input()
        print("To export to HTML, it saves the data in a .json file and accesses a html index which then reads the file, and displays it to you.")
        print("Currently, it runs the server indefinitely until it is manually closed. This prevents the program from being used in the same instance,")
        print("so it's best to export it in another format as well if that's something you want to do.")
        print(Fore.RESET) ### If other bluesky options get completed, then a description of them may be added here for the user's clarity. If you're unsure how to format it, look at the other information page
        print("[Press ENTER to return to main menu]")
        input()
    elif choice == '1':
        exportCSV(images,dupImages)
    elif choice == '2':
        print("Note. Currently accessing a HTML report will make it impossible to use the program again in a continuous instance.")
        choice = input("Continue?\n[Y/N]\n")
        if choice.lower() == 'y':
            exportHTML(images,dupImages,port,path)
    elif choice.lower() == 'port':
        port = int(input("Please inpu the value you'd prefer for your port. The default is 8000"))
    elif choice == '4':
        return
    reportOpt()

def deDuplicate(path): 
    global images, dupImages
    for FILE in os.listdir(path):
        imgPath = os.path.join(path,FILE)
        HASH = str(imagehash.average_hash(Image.open(imgPath)))
        #print(FILE)
        #print(HASH)
        if HASH in images:
            #print(f"Duplicate: {FILE}, {HASH}")
            dupImages[FILE] = HASH
        else:
            #print(f"Unique image: {FILE}, {HASH}")
            images[HASH] = FILE
    print("Unique Images:")
    for key in images:
        print(f"{images[key]}: {key}")
    print("\n\nDuplicate Images:")
    for key in dupImages:
        print(f"{key}: {dupImages[key]}")
        
    print("Would you like to delete duplicate images?")
    CHOICE = input("YES or NO?   ")
    if CHOICE.lower() == 'yes':
        print("\nAre you sure you would like to delete duplicate images?\nWhether or not they are recoverable will be based on your computer settings.")
        CHOICE = input("YES or NO?   ")
        if CHOICE.lower() == 'yes':
            for key in dupImages:
                imgPath = os.path.join(path,key)
                print(f"Deleting: {imgPath}")
                try: 
                    os.remove(imgPath) #this is the code to remove a file
                except:
                    print("Failed to remove one or more images.")
            print("Successfully deleted all duplicate images.")
            



def main():
    global path, images, dupImages
    print(rf"||===============================================================||") ###ASCII art subject to change if anyone wants to do a better job
    print(rf"||     {Fore.RED}     _====_   /\   /\  //===\\  ======  //===\\   {Fore.RESET}        ||")
    print(rf"||     {Fore.RED}     ||   ||  ||   ||  ||   ||    ||    ||   ||   {Fore.RESET}        ||")
    print(rf"||     {Fore.RED}     ||==//   ||===||  ||   ||    ||    ||   ||   {Fore.RESET}        ||")
    print(rf"||     {Fore.RED}     ||       ||   ||  ||   ||    ||    ||   ||   {Fore.RESET}        ||")
    print(rf"||     {Fore.RED}     ||       ||   ||  \\===//    ||    \\===//   {Fore.RESET}        ||")
    print(rf"||===============================================================||")
    print(rf"||{Fore.BLUE} |-\ |-- |-\ |   | |-\ |    -----  /--   /\   -----  /-\  |-\ {Fore.RESET} ||")
    print(rf"||{Fore.BLUE} | | |-- | | |   | |-/ |      |   |     /--\    |   |   | |-/ {Fore.RESET} ||")
    print(rf"||{Fore.BLUE} |-/ |-- |-/  \_/  |   |___ __|__  \-- /    \   |    \-/  | \ {Fore.RESET} ||")
    print(rf"||===============================================================||","\n\n\n")


    print(f"||=================================||")    
    print(f" {Fore.YELLOW}Current selected path is: {path} {Fore.RESET}   ")
    print(f"||=================================||")    
    print(f"    [0] {Fore.YELLOW} What does it do? {Fore.RESET}")
    print(f"||=================================||")
    print(f"    [1] {Fore.YELLOW} Set folder destination{Fore.RESET}")
    print(f"    [2] {Fore.YELLOW} Run Photo deDuplicator{Fore.RESET}")
    print(f"    [3] {Fore.YELLOW} Clear history{Fore.RESET}")
    print(f"||=================================||")
    print(f"    [4] {Fore.YELLOW} Export report {Fore.RESET}(WIP)")
    print(f"||=================================||")
    print(f"    [5] {Fore.YELLOW} Exit deDuplicator\n{Fore.RESET}\n")

    ###after running program, print the report then have an option to export it as something. CSV, html, etc.

    
    choice = input("    ")
    print("\n\n")
    

    if choice == '0':
        print("[Press ENTER to move dialogue forward]\n")
        input()
        print(Fore.YELLOW + "The Photo deDuplicator is built to find duplicate images in a specific folder. It has not been known to work on subfolders.\n")
        print("It does this by converting an image's data into a unique hash value, which is then compared by every other image stored.\n")
        input()
        print("If you wish to check multiple folders in one instance of the program, it is best to do them one at a time.\n")
        print("Between folders, you should clear the stored history. This is to protect against similar images stored in different folders,")
        print("which you may not wish to be deleted. If you want to make sure there are no duplicates at all, in every folder checked,")
        print("then you simply do not delete the history.")
        input()
        print("The program is currently able to export into a .csv file.\n\n" + Fore.RESET)
        print("[Press ENTER to return to main menu]")
        input()
        
    elif choice == '1':
        path = filedialog.askdirectory()    
        print(path)  
    elif choice == '2':
        deDuplicate(path) #runs the deDuplicate function, using the path as an input to carry information between functions
    elif choice == '3':
        print("Are you certain you wish to clear the system's history? Doing so will also clear the report, unless it's already been exported.\n\n")
        CHOICE = input("[yes/no]\n\n")
        if CHOICE.lower() == 'yes':
            images = {} #sets images and dupImages to empty dictionaries, effectively clearing them
            dupImages = {}
    elif choice == '4':
        reportOpt()
    elif choice == '5':
        CHOICE = input("Are you sure? Leaving will delete report if not exported\n[yes/no]\n\n")  ### make it check whether you've already exported the report or not
        if CHOICE.lower() == 'yes' or CHOICE == '':
            os._exit(0)
    main() #reset once done


#exportCSV(images,dupImages)
main()    