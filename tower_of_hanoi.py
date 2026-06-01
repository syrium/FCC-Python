def hanoi_solver(num_disks:int):
    pole1 = []
    pole2 = []
    pole3 = []

    for disk in range(num_disks, 0, -1):
        pole1.append(disk)
    
    result = f'{pole1} {pole2} {pole3}'

    def move_pile(num_disks, mv_from, mv_to):
        poles = [pole1, pole2, pole3]

        if num_disks == 1:
             move_disks(mv_from,mv_to)

        else:
            mv_medium = [p for p in poles if id(p) not in map(id, [mv_from, mv_to])][0]
            move_pile(num_disks-1, mv_from, mv_medium)
            move_disks(mv_from, mv_to)
            move_pile(num_disks-1, mv_medium, mv_to)

    def move_disks(mv_from, mv_to) :
        nonlocal result

        if len(mv_to) > 0:
            if mv_from[-1] > mv_to[0]:
                mv_to.insert(0,mv_from[-1])
            else:
                mv_to.append(mv_from[-1])
        else:
            mv_to.insert(0,mv_from[-1])
        mv_from.pop()
        result += f'\n{pole1} {pole2} {pole3}'
    
    move_pile(num_disks, pole1, pole3)
    
    return result

print(hanoi_solver(5))
