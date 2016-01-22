'''
Author:     Arthur J. Miller
Date:       01-20-2016

Overview:
        # Must make objective row negative for X1,X2,Etc
        # RowSize = (ActualRowSize -1)
        # ColSize = (ActualColSize -1)
        # Must change vales to float to handle normalization step

        # TODO Exeption handling for 2Di
        # TODO 2Dii Need a way to check for negative values in ratio array... algorithm doesnt use negative values
        # TODO how many times do we loop the whole algorithm? Are there other checks for NO MAX VALUE

Paramaters:
'''

#!/usr/bin/python

# import modules used here -- sys is a very standard one
#nonpy

# Gather our code in a main() function
def main():
    #### 1. Prompt User
    #       a. Size 2,3, or 4 variable objective function
    #ObjFunctSize = 2
    RowSize = 4         # 0 to 4
    ColSize = 2         # 0 to 2
    #           i. Enter obj funt values -> insert into array
    ObjFunctArray =  [float(-40),float(-50),float(0),float(0),float(0)]
    #       b. Number of constraints
    #           i. Enter constraint values (in inequality form) -> insert into ixj 2d array
    Const1Array = [float(1),float(2),float(1),float(0),float(40)] #40
    Const2Array = [float(4),float(3),float(0),float(1),float(120)] #120
    #### 2. Start Algorithm
    #       a. Convert inequality constraints to equation using slack variables
    #       b. Create initial Augmented array using constraint equations and objective equation
    SimplexArray = [Const1Array,Const2Array,ObjFunctArray]
    print(SimplexArray)
    #       c. Scan bottom row for smallest value -> use that column as entering column
    PivotColVal = min(SimplexArray[ColSize])
    print("PivotColVal: ", PivotColVal)
    PivotCol = SimplexArray[ColSize].index(PivotColVal)
    print("PivotCol: ", PivotCol)
    #       d. Find minimum value of ratios of {last column value : enter column value} -> this is pivot
    RatioArray = []
    for i in range(ColSize): #Dont do ratio for Objective Fucntion Row
        RatioArray.append(SimplexArray[i][RowSize]/SimplexArray[i][PivotCol])
        print("Ratio Array: ", RatioArray)
    #           i. if all entries in columns are 0 or negative -> no max solution
    NoMaxSol = all(v == 0 for v in RatioArray)
    print("NoMaxSol: ", NoMaxSol)
    if NoMaxSol == 1:
        print("No Max Solution... All ratio values are zero")
        return 1
    #           ii. Unimplmented. if tie at minimum ratio -> choose either
    PivotRowVal = min(RatioArray)
    print("PivotRowVal: ", PivotRowVal)
    PivotRow = RatioArray.index(PivotRowVal)
    print("PivotRow: ",PivotRow)
    #       e. Normalize pivot value by checking if 1, then dividing each row value by itself
    print(SimplexArray[PivotRow])
    PivotVal = float(SimplexArray[PivotRow][PivotCol])
    if SimplexArray[PivotRow][PivotCol] != 1:
        for i in range(RowSize+1):
            SimplexArray[PivotRow][i] = SimplexArray[PivotRow][i]/PivotVal
        print(SimplexArray[PivotRow])

    #       f. Make every other value in pivot column == 0 by, elementary row operations
    #           i. R_i' <= R_i - PivotVal*R(Pivot)
    print("SimplexArray Before Row Ops: ", SimplexArray)
    for i in range(ColSize+1):
        TempRowOpVal = SimplexArray[i][PivotCol]        #The value SimplexArray[i][PivotCol] will become zero before operation done
        for j in range(RowSize+1):
            if(i == PivotRow):
                break
            SimplexArray[i][j] = SimplexArray[i][j] - TempRowOpVal*SimplexArray[PivotRow][j]
    print("SimplexArray After Row Ops: ",SimplexArray)
    #       g. Check bottom row, if no values are negative DONE! bottom right value is Z maximum
    for i in range(RowSize+1):
        if(SimplexArray[RowSize][i] < 0):
            break
        else:
            print("Bottom Row Shows Maximum Solution: ",SimplexArray)
            return 0

    #       h. print Table
    print(SimplexArray)
    # Function to print table
'''    def printMatrix(testMatrix):
            print ' ',
            for i in range(len(testMatrix[1])):  # Make it work with non square matrices.
                  print i,
            print
            for i, element in enumerate(testMatrix):
                  print i, ' '.join(element)
SimplexAlgorithm().main()
'''

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()