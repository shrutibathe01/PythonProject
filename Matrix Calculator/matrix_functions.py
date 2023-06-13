def input_matrix():
    matrix=[]
    col=[]
    no_of_row=int(input('Enter no of Rows: '))
    no_of_col=int(input('Enter no. of Columns: '))
    
    for ir in range (1,no_of_row+1):
        for ic in range(1,no_of_col+1):
            print("Enter value of a",ir,ic)
            val=int(input())
            col.append(val)
        matrix.append(col)
        col=[]
    return no_of_row,no_of_col,matrix

def addition_of_matrix(matrixA,matrixB):
    addition_matrix=[]
    addition_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range(no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] + matrixB[r][c]
                addition_col.append(val)
            addition_matrix.append(addition_col)
            addition_col=[]
    return addition_matrix  

def subtraction_of_matrix(matrixA,matrixB):
    subtraction_matrix=[]
    subtraction_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for r in range(no_of_rowA):
            for c in range(no_of_colA):
                val=matrixA[r][c] - matrixB[r][c]
                subtraction_col.append(val)
            subtraction_matrix.append(subtraction_col)
            subtraction_col=[]
    return subtraction_matrix        

def product_of_matrix(matrixA,matrixB):
    product_matrix=[]
    product_col=[]
    no_of_rowA=len(matrixA)
    no_of_colA=len(matrixA[0])
    no_of_rowB=len(matrixB)
    no_of_colB=len(matrixB[0])
    val=0
    if no_of_rowA == no_of_rowB and no_of_colA == no_of_colB:
        for i in range(no_of_rowA):
            for j in range(no_of_colB):
                for k in range(no_of_colA):
                    val=val+(matrixA[i][k] * matrixB[k][j])
                product_col.append(val)
                val=0
            product_matrix.append(product_col)
            product_col=[]
    return product_matrix 

def transpose(matrix):
    row_len=len(matrix)
    col_len=len(matrix[0])
    row_tr=[]
    transpose_matrix=[]
    for z in range (row_len):
        for e in range(col_len):
            row_tr.append(matrix[e][z])
        transpose_matrix.append(row_tr)
        row_tr=[]
    return transpose_matrix        