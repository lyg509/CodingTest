#백준 9946 - 단어 퍼즐

i =1

while True:
    a = input().strip()
    b = input().strip()

    if a == "END" and b == "END":
        break
    
    if sorted(list(a)) == sorted(list(b)):
        print(f"Case {i}: same")
    else:
        print(f"Case {i}: different")


# 'f'  f-strings(Formatted string literals)의 약자
#  간단하게 문자열 내에 변수를 삽입하여 포매팅할 수 있는 기능을 제공한다.



        
        
