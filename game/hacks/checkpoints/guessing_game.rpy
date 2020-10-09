label guessing_game:
    python:
        secret = 4
        guess = 0
        counter = 0

        for i in range(secret):
            guess = int(renpy.input("What is the secret?"))
            if guess == secret:
                break
            counter = counter + 1
            renpy.say("Clara","You guessed: [guess] after [counter] tries")

    "You guessed: [guess] after [counter] tries"

    if guess == secret:
        "You guessed the secret = [secret] correctly"
    elif counter == secret and guess != secret:
        "You ran out of guesses, Goodbye"
    else:
        "CHECK EDGE CASES of counter = [counter] and guess = [guess]"

    return
