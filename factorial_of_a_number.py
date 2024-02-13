This Python program uses a recursive function to calculate the factorial of a given number. The factorial is computed by multiplying the number with the factorial of its preceding number.

# Python program to find
# factorial of given number
def factorial(n):

    #single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))
Output:
    120

    Iterative approach
    # Python program to find
    #factorial of a given number
    def factorial(n):
        if n < 0:
            return 0
        elif n ==0 or n== 1:
            return 1
        else:
            fact = 1
            while(n >1):
                fact *= n
                n -= 1
                return fact
            #Driver Code
            num = 5
            print("Factorial of",num,"is",factorial(num))
            Output:
                120

        Example 2:
            # Python program to find
            #factorial of given number

            #Function tofind factorial of given number
            def factorial(n):

                res = 1
                for i in range(2, n+1):
                    res *= i
                    return res
                # Driver Code
                num = 5
                print("Factorial of", num, "is",factorial(num))
                factorial(num))
                Output:
                    120

        Ternary operator(One line Solution)
        # Python 3 program to find
        # factorial of given number
         
         def factorial(n):
              
                 # single line to find factorial
                     return 1 if (n==1 or n==0) else n * factorial(n - 1) 
                  
                  
                 # Driver Code
                 num = 5
                 print ("Factorial of",num,"is",
                               factorial(num))

                Output:120

                using In-built function 
                # Python 3 program to find
                # factorial of given number
                import math
                 
                 def factorial(n):
                         return(math.factorial(n))
                      
                      
                     # Driver Code
                     num = 5
                     print("Factorial of", num, "is",
                                   factorial(num))

                     Using numpy.prod 
                     import numpy
                     n=5
                     x=numpy.prod([i for i in range(1,n+1)])
                     print(x)This Python program uses a recursive function to calculate the factorial of a given number. The factorial is computed by multiplying the number with the factorial of its preceding number.

                     # Python program to find
                     # factorial of given number
                     def factorial(n):

                         #single line to find factorial
                         return 1 if (n==1 or n==0) else n * factorial(n - 1)
                     # Driver Code
                     num = 5
                     print("Factorial of",num,"is",factorial(num))
                     Output:
                         120

                         Iterative approach
                         # Python program to find
                         #factorial of a given number
                         def factorial(n):
                             if n < 0:
                                 return 0
                             elif n ==0 or n== 1:
                                 return 1
                             else:
                                 fact = 1
                                 while(n >1):
                                     fact *= n
                                     n -= 1
                                     return fact
                                 #Driver Code
                                 num = 5
                                 print("Factorial of",num,"is",factorial(num))
                                 Output:
                                     120

                                Example 2:
                                    # Python program to find
                                    #factorial of given number

                                    #Function tofind factorial of given number
                                    def factorial(n):

                                        res = 1
                                        for i in range(2, n+1):
                                            res *= i
                                            return res
                                        # Driver Code
                                        num = 5
                                        print("Factorial of", num, "is",factorial(num))
                                        factorial(num))
                                        Output:
                                            120

                                Ternary operator
                    (One line Solution)
                    # Python 3 program to find
                    # factorial of given number
                     
                     def factorial(n):
                          
                             # single line to find factorial
                                 return 1 if (n==1 or n==0) else n * factorial(n - 1) 
                              
                              
                             # Driver Code
                             num = 5
                             print ("Factorial of",num,"is",
                                           factorial(num))




                Output:120

                using In-built function 
                # Python 3 program to find
                # factorial of given number
                import math
                 
                 def factorial(n):
                         return(math.factorial(n))
                      
                      
                     # Driver Code
                     num = 5
                     print("Factorial of", num, "is",
                                   factorial(num))

                     Using numpy.prod 
                     import numpy
                     n=5
                     x=numpy.prod([i for i in range(1,n+1)])
                     print(x)
