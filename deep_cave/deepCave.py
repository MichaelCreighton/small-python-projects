# Deep cave with Al

import random, sys, time

# set constants
width = 70
pause_amount = 0.03

print("deep cave")
print("crtl-c to stop")
time.sleep(2)

leftwidth = 20
gapwith = 10

while True:
    rightwidth = width - gapwith - leftwidth
    print(('.' * leftwidth) + (' ' * gapwith) + ('.' * rightwidth))
     
    try: 
        time.sleep(pause_amount)
    except KeyboardInterrupt:
        sys.exit()

    diceroll = random.randint(1, 6)
    if diceroll == 1 and leftwidth > 1:
        leftwidth = leftwidth -1
    elif diceroll == 2 and leftwidth + gapwith < width - 1:
        leftwidth = leftwidth + 1
    else:
        pass

        diceroll = random.randint(1, 6)
    if diceroll == 1 and gapwith > 2:
        gapwith = gapwith - 1
    elif diceroll == 2 and leftwidth + gapwith < width - 1:
        gapwith = gapwith + 1
    else:
        pass

