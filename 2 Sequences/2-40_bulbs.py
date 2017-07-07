# N light bulbs are connected by a wire. Each bulb has a switch associated with it,
# however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb.
# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.
# You can press the same switch multiple times.
#
# Note : 0 represents the bulb is off and 1 represents the bulb is on.

def num_switch(switches):
    switch_count = 0
    current_on = 1

    for i in range(len(switches)):
        if switches[i] != current_on:
            switches[i] = 1
            switch_count += 1
            current_on = 0 if current_on == 1 else 1

    return switch_count
    

if __name__ == '__main__':
    switches = [0, 1, 0, 1]
    print(num_switch(switches))