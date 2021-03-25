def main():
    c="Y"
    while(c=="Y"):
        print("What number are you thinking")
        try:
            number=int(input())
            if(number%2!=0):
                print("That's an odd number! Have another?")
                c=input()
            else:
                print("That's an even number! Have another?")
                c=input()
        except: 
            print("Please enter a number\n")
    
main()