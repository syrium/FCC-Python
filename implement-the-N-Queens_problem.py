def dfs_n_queens(n):
    solutions = []
    current = [] #to track the current path

    cols = set()
    pos_diag = set() # have same row + col
    neg_diag = set() # have same row - col

    if n < 1:
        return []
    
    def dfs(row):
        if row==n:
            solutions.append(current[:])
        
        for col in range(n):
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue
            
            current.append(col)
            cols.add(col)
            pos_diag.add(row+col)
            neg_diag.add(row-col)

            dfs(row+1)

            current.pop()
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    dfs(0)
    return solutions

print(dfs_n_queens(4))