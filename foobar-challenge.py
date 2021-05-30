import math


def fuel_injection_perfection(num_pellets):
    print("Initial amount of pellets: ", num_pellets)
    curr_pellets = int(num_pellets)
    num_steps = 0
    curr_least = 0

    #loop​ ​for​ ​still​ ​checking​ ​if​ ​we​ ​can​ ​get​ ​min​ ​from​ ​dividing​ ​by​ ​2​ ​throughout
    while (not (math.log(curr_pellets)).is_integer()):
        minStepsBetweenFloorCeil = num_steps + int(closerToTwoRaisedToNDiff(curr_pellets))
        if curr_least > minStepsBetweenFloorCeil or curr_least == 0:
            curr_least = minStepsBetweenFloorCeil
        
        #minimize steps in case NEXT number of pellets is ODD
        if curr_pellets % 2 != 0:
            if ((curr_pellets - 1)/2) % 2 == 0:
                curr_pellets -= 1
            else:
                curr_pellets += 1
            num_steps += 1

        curr_pellets /= 2
        num_steps += 1
    
    #since we only check if number of pellets is a power of 2, check for
    #necessary additional "divide by 2" steps to reach 1
    if curr_pellets > 1:
        num_steps += math.log(curr_pellets, 2)

    return min(curr_least, num_steps)

#get min number of add/remove pellets to reach nearer 2^n + from division by two from 2^n to 1
def closerToTwoRaisedToNDiff(curr_pellets):
    logbtwo = math.log(curr_pellets, 2)

    n_ceil = int(math.ceil(logbtwo))
    twoToCeilPellets = 2 ** n_ceil
    diff_with_ceil = twoToCeilPellets - curr_pellets

    n_floor = int(math.floor(logbtwo))
    twoToFloorPellets = 2 ** n_floor
    diff_with_floor = curr_pellets - twoToFloorPellets

    return min(n_ceil + diff_with_ceil, n_floor + diff_with_floor)

if __name__ == "__main__":
    print(fuel_injection_perfection('15'))
    print('---------------------------')
    print(fuel_injection_perfection('4'))
    print('---------------------------')
    print(fuel_injection_perfection('300'))    
    

            