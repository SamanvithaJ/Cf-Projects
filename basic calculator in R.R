# Basic calculator in R

num1 <- 3
num2 <- 5
choice <-3
result <- switch(choice, 
          "addition" = (num1+num2), 
          "subtraction" = (num1-num2), 
          "multiplication"=(num1*num2), 
          "div" =(num1/num2))
result

