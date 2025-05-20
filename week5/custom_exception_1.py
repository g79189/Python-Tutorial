class Negative_NumberEx(Exception):
    pass

def is_value_Negative(value):
    if value < 0:
        raise Negative_NumberEx("Value less than zero.")
        print("Value is not negative")
    return True
    
try:
    value = is_value_Negative(-5)
    print(value)
except Negative_NumberEx as e:
        print(e)
  
finally:
    print("End of program")
