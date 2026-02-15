def spiral_order():
    # Read dimensions
    try:
        line1 = input().split()
        if not line1: return
        r, c = map(int, line1)
        
        # Read matrix
        matrix = []
        for _ in range(r):
            matrix.append(list(map(int, input().split())))
            
        top, bottom = 0, r - 1
        left, right = 0, c - 1
        result = []
        
        while top <= bottom and left <= right:
            # 1. Traverse Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 2. Traverse Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 3. Traverse Left (Check if row still exists)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                
            # 4. Traverse Up (Check if column still exists)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        print(*(result))
        
    except EOFError:
        pass

if __name__ == "__main__":
    spiral_order()