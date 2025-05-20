def divide(a,b):
    try:
        num=int(b)
        return a/num

    except ZeroDivisionError as e:
        print("Divide by zero error")
        return None
    except ValueError:
        print("Not an integer")
        return None
        
print (divide(10,"Hello"))
