## Password Checker

This program was written by Alex Johnson as a part of CS3090 at the University of Utah. 

The program is a rudimentary password checker. It gives two scores based on password length and variety of characters used. 

```python
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
```

```python
 # Check password variety score
 
    score = (((length - repeats)/length)*100 - (2 * doubles))

    print("Character variety score: ", score)
```

### Limitations

While this serves as a baseline for what a good password should have, this program is not comprehensive. For example, it does not take into account the types of characters used and their variety.
ex. "abc" vs "a$3"
This program is for educational purposes and should not be consulted for actual password validity. For more information about what makes a strong password, check [here](https://www.cisa.gov/secure-our-world/use-strong-passwords).

### Ethical Considerations

There are few ethical considerations to be made concerning the program. This tool could not be used or modified to cause harm. The only potential harm comes from users misunderstanding the strength of their own password or putting too much consideration into this program's output. 