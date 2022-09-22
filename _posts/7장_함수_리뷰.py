#값 반환하기
def calculate_area(radius):
    area = 3.14 * radius**2
    return area

r = calculate_area(5)
print("원의 넓이는  = ",r)

#함수에 여러 개의 입력 전달하기
def get_sum(n1,n2):
    sum = 0
    for i in range(n1, n2+1):
        sum += i
    return sum

print(get_sum(1,10))

#정사각형 그리기
import turtle
t = turtle.Turtle()

def rectangular(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
rectangular(100)

#n각형 그리기
def polygon(n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        
for i in range(10):
    t.lt(20)
    polygon(6, 100)

    

    

