s = input()

state = pstate = ''

for c in s:

    if c == '1': #(--)

        if pstate == '':
            print(1, 1)
            state = 'h'

        if pstate == 'h':
            print(1,3)
            state = ''

        if pstate == 'v':
            print(1,1)
            state = 'hv'

        if pstate == 'hv':
            print(1, 3)
            state = 'v'


    else: # c = 0 (|)
        if pstate == '':
            print(3, 4)
            state = 'v'

        if pstate == 'h':
            print(3, 4)
            state = 'hv'

        if pstate == 'v':
            print(1, 4)
            state = ''

        if pstate == 'hv':
            print(1, 4)
            state = 'h'


    pstate = state

