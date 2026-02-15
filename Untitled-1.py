def check_symmetry():
    try:
        # Read dimensions
        m, n = map(int, input().split())
        
        # Condition 1: Must be square
        if m != n:
            # We still need to consume the remaining input lines even if not square
            for _ in range(m):
                input()
            print("Not a Symmetric Matrix")
            return

        # Read the matrix
        matrix = []
        for _ in range(m):
            matrix.append(list(map(int, input().split())))

        # Condition 2: Check symmetry A[i][j] == A[j][i]
        for i in range(m):
            # We only need to check the upper triangle to avoid redundant comparisons
            for j in range(i + 1, n):
                if matrix[i][j] != matrix[j][i]:
                    print("Not a Symmetric Matrix")
                    return

        print("Symmetric Matrix")
        
    except EOFError:
        pass

if __name__ == "__main__":
    check_symmetry()