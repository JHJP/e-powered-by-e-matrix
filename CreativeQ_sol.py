from functools import reduce
 
#1 피보나치수열을 출력하는 함수를 람다함수를 사용하여 작성
numberOfFib =lambda numberOfFib: [(lambda elementOfSequence : (1/(5**0.5))*( ((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1) ))(i) for i in range(numberOfFib)]

#2 (1)과 피보나치수열의 일반항을 이용하여 자연상수 e를 출력하는 함수를 람다함수를 사용하여 작성(e = lim(n->)(1+1/n)**n)이용
e = lambda infinity: (1+1/(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity))**(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity)

#3  m x n 메트릭스를 출력하는 함수를 람다함수를 사용하여 작성
makeArrayByLambda = lambda m,n :  [(lambda n :[r.randint(0,10) for j in range(n)])(n) for i in range(m)]

#4 (1), (2), (3)를 이용하여 오직 자연상수 e만을 갖는 2x2 메트릭스 구함
eArrayByLambda = lambda m,n :  [(lambda n :[(lambda infinity: (1+1/(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity))**(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity))(30) for j in range(n)])(n) for i in range(m)]
eMatrix = eArrayByLambda(2,2)
piMatirx = [[0, -3.1415], [3.1415, 0]]

#5 행렬의 곱셈함수를 작성
productMatrix = lambda matrix1, matrix2 : [(lambda matrix1, matrix2 : [(matrix1[0][0]*matrix2[0][0])+(matrix1[0][1]*matrix2[1][0]), (matrix1[0][0]*matrix2[0][1])+(matrix1[0][1]*matrix2[1][1])])(matrix1, matrix2),(lambda matrix1, matrix2 : [(matrix1[1][0]*matrix2[0][0])+(matrix1[1][1]*matrix2[1][0]), (matrix1[1][0]*matrix2[0][1])+(matrix1[1][1]*matrix2[1][1])])(matrix1,matrix2)]

#6 (5)를 이용하여 행렬의 거듭제곱 함수를 작성
matrixExponential = lambda matrix, powerNumber: [[1,0],[0,1]] if powerNumber==0 else productMatrix(matrix, matrixExponential(matrix,powerNumber-1))

#7 팩토리알을 구하는 함수를 작성
factorial = lambda n: 1 if n==0 else n*factorial(n-1)

#8 (6), (7)을 이용하여 테일러급수의 일반항을 구하는 함수를 작성
generalTermOfTaylorE = lambda call : [(lambda count : [(lambda number11 : matrixExponential(eMatrix, number11)[0][0]/factorial(number11))(count), (lambda number12 : matrixExponential(eMatrix, number12)[0][1]/factorial(number12))(count)])(call), (lambda count : [(lambda number21 : matrixExponential(eMatrix, number21)[1][0]/factorial(number21))(count), (lambda number22 : matrixExponential(eMatrix, number22)[1][1]/factorial(number22))(count)])(call)]

#9 재귀함수 작성
eRecursion11 = lambda infinite : generalTermOfTaylorE(0)[0][0] if infinite==0 else generalTermOfTaylorE(infinite)[0][0]+eRecursion11(infinite-1)
eRecursion12 = lambda infinite : generalTermOfTaylorE(0)[0][1] if infinite==0 else generalTermOfTaylorE(infinite)[0][1]+eRecursion12(infinite-1)
eRecursion21 = lambda infinite : generalTermOfTaylorE(0)[1][0] if infinite==0 else generalTermOfTaylorE(infinite)[1][0]+eRecursion21(infinite-1)
eRecursion22 = lambda infinite : generalTermOfTaylorE(0)[1][1] if infinite==0 else generalTermOfTaylorE(infinite)[1][1]+eRecursion22(infinite-1)

#10 (8), (9)를 이용하여 테일러급수를 구하는 함수 작성
ePoweredByEmatrix = lambda infinity : [[(lambda infinite11 : generalTermOfTaylorE(0) if infinite11==0 else generalTermOfTaylorE(infinite11)[0][0]+eRecursion11(infinite11-1))(infinity), (lambda infinite12 : generalTermOfTaylorE(0) if infinite12==0 else generalTermOfTaylorE(infinite12)[0][1]+eRecursion12(infinite12-1))(infinity)], [(lambda infinite21 : generalTermOfTaylorE(0) if infinite21==0 else generalTermOfTaylorE(infinite21)[1][0]+eRecursion21(infinite21-1))(infinity), (lambda infinite22 : generalTermOfTaylorE(0) if infinite22==0 else generalTermOfTaylorE(infinite22)[1][1]+eRecursion22(infinite22-1))(infinity)]]

#11 알려져 있는 [[0, -pi], [pi, 0]]을 이용하여 검산 
# generalTermOfTaylorPi = lambda call : [(lambda count : [(lambda number11 : matrixExponential(piMatirx, number11)[0][0]/factorial(number11))(count), (lambda number12 : matrixExponential(piMatirx, number12)[0][1]/factorial(number12))(count)])(call), (lambda count : [(lambda number21 : matrixExponential(piMatirx, number21)[1][0]/factorial(number21))(count), (lambda number22 : matrixExponential(piMatirx, number22)[1][1]/factorial(number22))(count)])(call)]

# piRecursion11 = lambda infinite : generalTermOfTaylorPi(0)[0][0] if infinite==0 else generalTermOfTaylorPi(infinite)[0][0]+piRecursion11(infinite-1)
# piRecursion12 = lambda infinite : generalTermOfTaylorPi(0)[0][1] if infinite==0 else generalTermOfTaylorPi(infinite)[0][1]+piRecursion12(infinite-1)
# piRecursion21 = lambda infinite : generalTermOfTaylorPi(0)[1][0] if infinite==0 else generalTermOfTaylorPi(infinite)[1][0]+piRecursion21(infinite-1)
# piRecursion22 = lambda infinite : generalTermOfTaylorPi(0)[1][1] if infinite==0 else generalTermOfTaylorPi(infinite)[1][1]+piRecursion22(infinite-1)

# ePoweredByPimatrix = lambda infinity : [[(lambda infinite11 : generalTermOfTaylorPi(0) if infinite11==0 else generalTermOfTaylorPi(infinite11)[0][0]+piRecursion11(infinite11-1))(infinity), (lambda infinite12 : generalTermOfTaylorPi(0) if infinite12==0 else generalTermOfTaylorPi(infinite12)[0][1]+piRecursion12(infinite12-1))(infinity)], [(lambda infinite21 : generalTermOfTaylorPi(0) if infinite21==0 else generalTermOfTaylorPi(infinite21)[1][0]+piRecursion21(infinite21-1))(infinity), (lambda infinite22 : generalTermOfTaylorPi(0) if infinite22==0 else generalTermOfTaylorPi(infinite22)[1][1]+piRecursion22(infinite22-1))(infinity)]]

# goTo = lambda x : [print(ePoweredByPimatrix(i),"\n") for i in x]
# goTo(range(1, 20))

#11 e**x의 테일러급수는 e= 1/n!의 무한급수이므로 이것의 일반항 1/n!을 출력하는 함수
# generalTermOfTaylorEOne = lambda number : 1/factorial(number)

#12 e= 1/n!의 무한급수를 출력하는 재귀함수
# ePoweredByOne = lambda infinite: generalTermOfTaylorEOne(0) if infinite==0 else generalTermOfTaylorEOne(infinite)+ePoweredByOne(infinite-1)

# goTo = lambda x : [print(ePoweredByOne(i),"\n") for i in x]
# goTo(range(1, 20))


# (검산) e**1의 테일러급수는 e= 1/n!의 무한급수이므로 이것의 일반항 1/n!을 출력하는 함수
def generalTermOfTaylorEOne(number):
    return 1/factorial(number)

# e= 1/n!의 무한급수를 출력하는 재귀함수
def ePoweredByOne(infinite):
    if infinite==0:
        return generalTermOfTaylorEOne(0)
    else:
        return generalTermOfTaylorEOne(infinite)+ePoweredByOne(infinite-1)
    
# e**1가 근사하는 값을 출력 
goTo = lambda x : [print(ePoweredByOne(i),"\n") for i in x]
print(goTo(range(1, 20)))