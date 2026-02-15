def check_identity_matrix():
    try:
        # Get the size of the square matrix
        n = int(input().strip())
        
        is_identity = True
        
        for i in range(n):
            # Read each row and convert to a list of integers
            row = list(map(int, input().split()))
            
            for j in range(n):
                # Check diagonal elements
                if i == j:
                    if row[j] != 1:
                        is_identity = False
                # Check non-diagonal elements
                else:
                    if row[j] != 0:
                        is_identity = False
            
            # Optimization: if we already found a mismatch, no need to check further rows
            if not is_identity:
                break
                
        if is_identity:
            print("Identity Matrix")
        else:
            print("Not an Identity Matrix")
            
    except ValueError:
        print("Invalid input. Please enter integers.")

# Run the function
check_identity_matrix()