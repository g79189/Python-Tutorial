length=int (input("Enter the length: "))
width=int (input("Enter the width: "))
print(length)
print(width)

def area(l,w):
  # area=l*w
  # print (area)
  return l*w

def perimeter(l,w):
  # perimeter=2*l+2*w
  # print(perimeter)
  return (2*l)+(2*w)


area= area(length,width)
print("Area is : ",area)
perimeter=perimeter(length,width)
print("Perimeter is : ",perimeter)
#perimeter("Perimeter is: ",int(perimeter(length,width)))    
