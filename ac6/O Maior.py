def main():
    a, b, c = input().split()
    a= int(a)
    b= int(b)
    c= int(c)
           
    maiorAB= (a+b+abs(a-b))/2
    MaiorABC = (maiorAB + c + abs(maiorAB-c))/2

    print(f'{MaiorABC:.0f} eh o maior')

main()

