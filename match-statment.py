X = int(input("Enter the value x: "))

match  X :
    
    case 0 :
         print("x: is zero")
    case 10 :
        print("case is 10 ")
    case _ if X != 30 :
        print("x is not equal to 30")
    case 40 :
          
          print("X is 40 ")