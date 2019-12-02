def commands(number):

    commands = []
    code = bin(number)[2:]

    gestures = \
        {
            1: "wink",
            10: "double blink",
            100: "close your eyes",
            1000: "jump"
        }

    gesture_number = 1
    for i in range(len(code)-1, -1, -1):
        if code[i] == str(1) and gesture_number <= 1000:
            commands.append(gestures[gesture_number])
        elif gesture_number > 1000:
            commands.reverse()
        gesture_number *= 10

    return commands

def secret_code(actions):
    all_actions_bin = 0
    gestures = \
        {
            "wink": 1,
            "double blink": 10,
            "close your eyes": 100,
            "jump": 1000
        }

    all_actions = [gestures[gesture] for gesture in actions]
    for i in range(0, len(all_actions)):
        try:
            if all_actions[i] > all_actions[i + 1]:
                all_actions.append(10000)
                return int("0b"+str(sum(all_actions)), 2)
        except:
            continue

    return int("0b"+str(sum(all_actions)), 2)
