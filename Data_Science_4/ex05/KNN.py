import pandas as pd
import sys

def main():
    if len(sys.argv) != 3:
        print ("Two arguments required : python KNN.py 'Train_knight.csv' 'Test_knight.csv'")

    dir_Train = sys.argv[1]
    dir_Test = sys.argv[2]

    
    return 0

if __name__ == "__main__":
    main()