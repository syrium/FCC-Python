def square_root_bisection(number, tolerance=0.01, max_iteration=20):
    iteration = 0
    root = 0
    track_mid = []

    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    if number < 1:
        lower = number
        upper = 1
        while iteration < max_iteration:
            iteration += 1
            mid = (upper + lower) / 2
            track_mid.append(mid)
            
            if upper - lower <= tolerance:
                root = mid
                print(f'The square root of {number} is approximately {root}')
                print(track_mid)
                return root
            elif mid**2 > number:
                upper = mid
            #elif mid**2 < number:
            #    lower = mid
            else:
                lower = mid
            #else:
                #root = lower
            #    return
        print(f'Failed to converge within {max_iteration} iterations')
        print(track_mid)
        return
    else:
        upper = number
        lower = 0
        while iteration < max_iteration:
            iteration += 1
            mid = (upper + lower) / 2
            track_mid.append(mid)
            if  upper - lower <= tolerance:
                root = mid
                print(f'The square root of {number} is approximately {root}')
                print(track_mid)
                return root
            elif mid**2 > number:
                upper = mid
            else:
                lower = mid
        print(f'Failed to converge within {max_iteration} iterations')
        print(track_mid)
        return

    

square_root_bisection(255, 1e-7, 10)