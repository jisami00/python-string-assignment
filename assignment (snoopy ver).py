#################################
# Name: Jessa Mae R. Forrosuelo #
# Code: 2270                    #
#################################


def main():
    print(" ／￣￣ヽ＿＿")
    print(" / /^ヽ ・   ●\"")
    print( "｜# ｜　＿＿ノ ")
    print(" 　`―-)=(    ")
    print("　　／   )_) ")
    print("　c(　   ﾉ ")
    print("   _｣ LL_")
    print(" (＿＿)__)")
    print("🦴" + "=" * 40 + "🦴")

    #Input
    print("🐾 Snoopy says: Type something fun for me to play with! 🐾")
    sentence = input ("🏠 Enter your sentence: ")

    #Main Menu Loop
    while True:
        print("=== SNOOPY'S WORD TRICKS ===")
        print("Choose an operation:")
        print("0. Enter new sentence")
        print("1. Reverse sentence")
        print("2. Count vowels")
        print("3.  Check if Palindrome  ")
        print("4.  Find and replace word ")
        print("5.  Format (title case)")
        print(" 6. Split into words ")
        print(" 7. Word frequency counter")
        print(" 8. Swap case")
        print(" 9. Exit")
        print("🦴" + "=" * 50 + "🦴")

        choice = input("🐕 What trick should Snoopy do? (0-9): ")


        if choice == "0":
            
            sentence = input("Enter a new sentence: ")
            print(f"New sentence saved: '{sentence}'")
            
        elif choice == "1":
            # Reverse the sentence
            result = sentence[::-1]
            print(f"🦴 Snoopy did a backflip! Here's your sentence backwards: '{result}'")
            print("🐕 Woof! That was fun!")
            
        elif choice == "2":
            # Count vowels
            vowels = "aeiouAEIOU"
            count = 0
            for letter in sentence:  # Loop through each letter - Snoopy sniffing each one!
                if letter in vowels:
                    count += 1
            print(f"🎶 Snoopy sniffed around and found {count} vowels!")
            print("🐕 *sniff sniff* Good hunting!")
            
        elif choice == "3":
            # Check if palindrome
            cleaned = sentence.replace(" ", "").lower()
            is_palindrome = cleaned == cleaned[::-1]
            if is_palindrome:
                print("🔍 Snoopy discovered: This sentence IS a palindrome!")
                print("🐕 Woof! It reads the same forwards and backwards!")
            else:
                print("🔍 Snoopy discovered: This sentence is NOT a palindrome.")
                print("🐕 It's different when flipped around!")
                
        elif choice == "4":
            # Find and replace word
            old_word = input("What word should Snoopy find? ")
            new_word = input("What word should replace it? ")
            result = sentence.replace(old_word, new_word)
            print(f" Snoopy fixed it: '{result}'")
            print("🐕 Good as new!")
            
        elif choice == "5":
            # Format (title case)
            result = sentence.title()
            print(f" Snoopy made it fancy: '{result}'")
            print("🐕 Looking good!")
            
        elif choice == "6":
            # Split into words
            words = sentence.split()
            print(f"Snoopy split your sentence into: {words}")
            print(f"That's {len(words)} word treats total!")
            
        elif choice == "7":
            # Word frequency counter
            words = sentence.lower().split()
            frequency = {}
            for word in words:  # Loop through each word - Snoopy counting!
                clean_word = word.strip('.,!?;:"')
                if clean_word in frequency:
                    frequency[clean_word] += 1
                else:
                    frequency[clean_word] = 1
            print("word count report:")
            for word, count in frequency.items():
                print(f"   '{word}': {count} times")
            print("All counted up!")
            
        elif choice == "8":
            # Swap case
            result = sentence.swapcase()
            print(f"Snoopy swapped the cases: '{result}'")
            print(" Upper became lower, lower became upper!")
        elif choice == "9":
            # Exit program with Snoopy 
            print("🐕 Snoopy says: Thanks for playing word tricks with me!")
            print("🦴 It was pawsome fun! 🦴")
            print("Goodbye from Jessa Mae R. Forrosuelo - Code: 2270")
            print("🐾 See you next time for more adventures! 🐾")
            print("         ⠀⢀⡠⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⠤⠀⠀⠀⠀")
            print(" ⠘⠃⠀⠀⣀⡠⠔⠁⠀⠀⠀⠈⢦⠀⠀⠀⠀⢠⡖⠋⠉⠉⠻⡒⠈⠁⠀")
            print(" ⢠⠔⠉⠁⠀⠀⠄⠀⠀⠀⠠⣴⣦⣧⠀⠀⢠⣿⠃⢀⠀⠀⠀⠸⠈⢂⠀⠀")
            print("⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⢳⣿⣿⣿⣄⠄⠉⠁⡔⠞⠢⡀⠀⠀⠀⠀⢄⡀")
            print(" ⣐⣺⡀⠀⠀⠀⠀⠀⠀⠀⠀⡆⣼⣿⣿⡿⠀⠤⠤⠤⠏⠀⠀⠁⠀⠀⢆⠀⠀⡡")
            print("⠈⠋⠈⠒⠦⠤⠤⠒⠒⠒⠒⠧⣻⡿⠟⠳⠤⠤⠤⠤⠤⠤⠔⠑⠒⠊⠀⠁⠂⠁")
            print(" Zzz... Snoopy is taking a nap...")
            break  # This stops the loop - Snoopy goes to sleep
            
        else:
            # invalid choices
            print("🐕 Woof! Snoopy is confused! That's not a trick I know!")
            print("🦴 Invalid choice, try again. Please pick a number between 0-9! 🦴")

main()