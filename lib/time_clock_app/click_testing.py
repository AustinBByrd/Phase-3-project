import datetime
import time
import os



def display_clock():
    last_time = None  # Variable to store the last displayed time

    while True:
        now = datetime.datetime.now()

        # Check if the time has changed since the last display
        if now != last_time:
            # Print the current time
            print(f"Current Time: {now.strftime('%I:%M:%S %p')}")

            # Print a message indicating that the time has changed
            print("Time has changed!")

            # Update the last displayed time
            last_time = now

        # Wait for a short interval before checking again
        time.sleep(1)  # Adjust the interval as needed

print("hello world")
display_clock()


def animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10      /   2 \\\\")
    print(";;         /       ::")
    print("|| 9  ----O      3 ||")
    print("::                 ;;")
    print(" \\\\ 8           4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10          2 \\\\")
    print(";;                 ::")
    print("|| 9  ----O------3 ||")
    print("::                 ;;")
    print(" \\\\ 8           4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10          2 \\\\")
    print(";;                 ::")
    print("|| 9  ----O      3 ||")
    print("::          \      ;;")
    print(" \\\\ 8        \  4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10          2 \\\\")
    print(";;                 ::")
    print("|| 9  ----O      3 ||")
    print("::       /         ;;")
    print(" \\\\ 8   /       4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10          2 \\\\")
    print(";;                 ::")
    print("|| 9------O      3 ||")
    print("::                 ;;")
    print(" \\\\ 8           4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("        _____")
    print("     _.'_____`._")
    print("   .'.-'  12 `-.`.")
    print("  /,' 11      1 `.\\")
    print(" // 10  \       2 \\\\")
    print(";;       \         ::")
    print("|| 9  ----O      3 ||")
    print("::                 ;;")
    print(" \\\\ 8           4 //")
    print("  \`. 7       5 ,'/")
    print("   '.`-.__6__.-'.'")
    print("      -._____.-")
    
    time.sleep(1)
# while True:
#     animation()
