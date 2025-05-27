n=int(input())

def modify_matrix(n):
    i=n//2
    j=n//2
    val=1
    matrix[i][j]=val
    val+=1

    for ring in range(1,n//2+1):
        j+=1
        matrix[i][j]=val
        val+=1

        for _ in range(2*ring-1):
            i+=1
            matrix[i][j]=val
            val+=1

        for _ in range(2*ring):
            j-=1
            matrix[i][j]=val
            val+=1

        for _ in range(2*ring):
            i-=1
            matrix[i][j]=val
            val+=1

        for _ in range(2*ring):
            j+=1
            matrix[i][j]=val
            val+=1
        
def print_matrix(matrix):
    for row in matrix:
        print(row)

if n%2==1:
    matrix=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append('*')
        matrix.append(row)

    modify_matrix(n)
    
    print_matrix(matrix)
        
