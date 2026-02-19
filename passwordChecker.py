def main():
    password = input("Enter password: ")

    # Check password length score
    length = len(password)

    if length < 7:
        length_score = "Poor"
    elif length < 10:
        length_score = "Decent"
    elif length < 15:
        length_score = "Good"
    else:
        length_score = "Excellent"

    print("Length score:", length_score)

    prevChar = ''
    doubles = 0
    repeats = 0

    charMap = {}
    for char in password:
        if char not in charMap:
            charMap[char] = 1
            prevChar = char
        else:
            if prevChar == char:
                doubles += 1
            prevChar = char
            repeats += 1

    score = (((length - repeats)/length)*100 - (2 * doubles))

    print("Character variety score: ", score)







if __name__ == "__main__":
    main()
