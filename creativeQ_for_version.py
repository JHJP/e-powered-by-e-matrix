from functools import reduce

# 오직 자연상수 e만을 갖는 mxn 메트릭스 출력 함수 (풀이과정의 1,2,3을 합침)
eArrayByLambda = lambda m,n :  [(lambda n :[(lambda infinity: (1+1/(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity))**(lambda EulerNumber: reduce(lambda x,y:x+y,(lambda numberOfFib: [(lambda elementOfSequence : int( (1/(5**0.5))*(((1+5**0.5)/2)**(elementOfSequence+1)-((1-5**0.5)/2)**(elementOfSequence+1)) ))(i) for i in range(numberOfFib)])(EulerNumber)))(infinity))(30) for j in range(n)])(n) for i in range(m)]

# 매트릭스의 거듭제곱을 출력하는 함수 (풀이과정의 5,6을 합침)
matrixExponential = lambda matrix, powerNumber: [[1,0],[0,1]] if powerNumber==0 else (lambda matrix1, matrix2 : [(lambda matrix1, matrix2 : [(matrix1[0][0]*matrix2[0][0])+(matrix1[0][1]*matrix2[1][0]), (matrix1[0][0]*matrix2[0][1])+(matrix1[0][1]*matrix2[1][1])])(matrix1, matrix2),(lambda matrix1, matrix2 : [(matrix1[1][0]*matrix2[0][0])+(matrix1[1][1]*matrix2[1][0]), (matrix1[1][0]*matrix2[0][1])+(matrix1[1][1]*matrix2[1][1])])(matrix1,matrix2)])(matrix, matrixExponential(matrix,powerNumber-1))

# 팩토리알을 구하는 함수
factorial = lambda n: 1 if n==0 else n*factorial(n-1)

# 테일러급수 e**eMatrix의 일반항을 구하는 함수(eArrayByLambda()를 이용하여 e로구성된 2x2행렬을 구한다)
generalTermOfTaylorE = lambda call : [(lambda count : [(lambda number11 : matrixExponential(eArrayByLambda(2,2), number11)[0][0]/factorial(number11))(count), (lambda number12 : matrixExponential(eArrayByLambda(2,2), number12)[0][1]/factorial(number12))(count)])(call), (lambda count : [(lambda number21 : matrixExponential(eArrayByLambda(2,2), number21)[1][0]/factorial(number21))(count), (lambda number22 : matrixExponential(eArrayByLambda(2,2), number22)[1][1]/factorial(number22))(count)])(call)]

# e**eMatrix의 일반항에 0부터 infinitese까지대입하여 더한 각 성분을 리스트 형식으로 출력하는 함수
def eRecursions(infinites):
    eRecursionArray=[]
    for i,j in [(0,0), (0,1), (1,0), (1,1)]:
        element=lambda infinites :generalTermOfTaylorE(0)[i][j] if infinites==0 else generalTermOfTaylorE(infinites)[i][j]+a(infinites-1)
        eRecursionArray.append(element(infinites))
    return eRecursionArray
    
# eRecursions에서 구해진 각 항을 2x2매트릭스 형식으로 출력하는 함수
def ePoweredByEmatrix(infinity):
    rowOneOfEPowered=[]
    rowTwoOfEPowered=[]
    for i in range(2):
        rowOneOfEPowered.append(eRecursions(infinity)[i])
    for i in range(2,4):
        rowTwoOfEPowered.append(eRecursions(infinity)[i])
    return [rowOneOfEPowered, rowTwoOfEPowered]

# e**eMatrix가 근사하는 값을 출력
goTo = lambda x : [print(ePoweredByEmatrix(i),"\n") for i in x]
goTo(range(1, 25))