# 14 Pandas Data Analysis

## 교육 목차/진도
1. numpy
2. pandas
3. 머신러닝(신경망x)
4. 딥러닝(신경망o)

Gole : 딥러닝의 코드 이해, 적용할 수 있음


### 데이터의 형태
* 차원?
0. 스칼라				: 크기		(a>=0)						양의 실수+0
1. 백터(vector)		: 방향 + 크기	(a, b),(a,b,c),(a,b,c,d)	a,b,c,d는 실수(real number)
3. 매트릭스(matrix,행렬)	: 수나 식의 배열, vector의 모임
4. 볼륨(volume)				: 매트릭스의 모임
* Tensor : 1,2,3 또는 3부터

* array : [1,2] 			: vector
* array : [[1,2], [3,4]]	: matrix
* array : [ [[1,2], [3,4]], [[1,2], [3,4]] ] : 볼륨


# 필수로 알아야하는 것
* 행렬 덧셈, 뺄셈, 곱셈
* 전치행렬
* 방정식 -> 행렬 변경


---
# Jupyter Notebook 기본 사용법
참고 : Jupyter 기본 사용법.ipynb

## introspection
* ?	: 객체 또는 함수일때 정의되어 있는 문서 출력
* ?? : 소스코드도 보여줌
* Shift + Tab : 말풍선으로 객체 또는 함수일때 정의되어 있는 문서 출력
* 예
```
def func_1(a,b):
    return a+b
	
func_1??

Signature: func_1(a, b)
Docstring: <no docstring>
Source:   
def func_1(a,b):
    return a+b
File:      c:\users\apollo\onedrive -\data\data-science-master\datasience\<ipython-input-9-41e494ecc00d>
Type:      function	
```
```
import numpy as np
np.*?
np.*grad*?

from numpy import gradient
gradient??
```

## 매직 명령어
* 파이썬 자체에서는 존재하지 않는 명령어
	- 쥬피터 노트북에서만 지원하는 기능
	- % 기호를 붙여서 사용
	- %magic
	- %time : 시간 측정
		+ `%time [i for i in range(1000000)]`
	- %timeit : 평균 출력
		+ `%timeit [i for i in range(100000)]`
	- %pwd
	- %env
	
## 운영체제 명령어
* ! : 운영체제 명령어 실행할 수 있음
	- !dir
	- !ipconfig
---
# numpy
* 참고 : numpy 기존 사용법.ipynb

* 산술연산을 위한 패키지
	- ndarray(다차원 배월) : 배열 연산 + 브로드캐스팅 기능을 이용해 연산 가능하게 해준다.
		+ 브로드캐스팅 : 연산을 전체에 뿌려준다.
	- 장점 : 브로드캐스팅 덕분에 반복문 작성할 필요가 없다.
	- 선형대수, 난수 생성 가능
* numpy : 산술데이터 처리만 가능한 라이브러리
* pandas : 통계 분석 처리를 위한 리이브러리
* 사용법 예
	- `import numpy as np`
* 리스트와 차이
	- `arr1 = np.arange(1000)'
	- `list1 = [i for i in range(1000)]`
	- `arr2 = np.array(list1)`
	- 리스트 : __개체 저장소__
		+ '함수'도 개체, 리스트로 사용 가능
		+ `list_2 = [print, range]`
	- __ndarray는 리스트 차체에서 산술 연산이 가능함__
		+ 리스트는 문자열처럼 연산함
		
### Numpy ndarray
* 다차원 배열 객체
	- numpy는 ndarray라고 하는 N차원 배열 객체 사용
* 예
```
data = np.random.randn(2,3)
data
array([[ 0.92230624, -1.51439758,  1.58033582],
       [-0.34252766, -1.10818752, -0.57169977]])

data.shape
(2, 3)

data *10
data + data 
```
* arr.shape
	- 객체의 행렬 크기를 알 수 있음
* arr.ndim
	- 객체의 차원을 알 수 있음
	
## ndarray 생성하기
* np.zeros(10): 메모리를 초기화하고, 0으로 값을 채워 넣는다.
* np.empty(10): zeros 비슷하지만, 메모리를 초기화하지 않고 메모리값을 반환한다.
* np.ones((3,4)): 메모리를 초기화하고 1로 채워 넣는다.
* np.full((3,4),10) : 임의의 값(10)으로 채움

* np.ndarray((3,)) : ndarray는 권장사항 아님

### indx, slice
* 리스트와 동일
* Sequential(순차) 데이터이기 때문에 인덱싱과 슬라이싱이 가능하다.
* 예
```
arr2d_2 = np.array([
    [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
    [[13,14,15,16],[17,18,19,20],[21,22,23,24]]
])

arr2d_2.shape
(2, 3, 4)

arr2d_2[:,[1],[2]]
array([[ 7],
       [19]])
```

### 블리언 값
* names = np.array(["오민엽", "조상우", "오정석", "정세영"])
* names[Ture]이면 값을 출력
```
names == '오민엽'
array([ True, False, False, False])
```
```
names[names != '오민엽']
array(['조상우', '오정석', '정세영'], dtype='<U3')
```
```
data = np.random.randn(7,4)
data<0
data[data<0]
data[data>0]
```
```
data[data<0] = -1
data
array([[-1.        , -1.        ,  0.4677455 , -1.        ],
       [-1.        , -1.        ,  0.12119663, -1.        ],
       [ 0.24661762,  0.75266912,  0.41781214,  0.57523455],
       [ 1.01347698,  1.20123116,  0.27038419, -1.        ],
       [-1.        , -1.        ,  0.2872791 ,  0.40947229],
       [ 0.60802533,  0.24272869, -1.        ,  0.53159843],
       [-1.        ,  1.61764345,  2.38541021, -1.        ]])
```

### 팬시(fnacy) 색인
* fancy(고급진?)
* 정수 배열 색인
	- 정수만 사용가능, ':'은 사용 불가
	- 특정한 행(row)을 출력 가능
* arr[[4,3,0]]
	- 4번째, 3번째, 0번째 행 출력
* arr2d_1[[0,1,2],[1,2,2]]
	- 0번째행의 1번 인덱스, 1번째행의 2번 인덱스, 2번째행의 2번 인덱스 출력
* arr2 = np.arange(32).reshape((8,4))
	- 8행, 4열에 0~31 원소를 넣음
```
arr2[[1,0],[0,2]]
	1행의 0번열, 0행의 2번열
array([4, 2])
```


## 백터화 연산
* 배열에 함수를 적용하고 싶다.
* 함수를 백터화 시킨다. -> 적용시킨다. (for문을 구현한 것이라 성능이 안 좋다)
* 브로드캐스팅을 이용해 연산한다. (성능이 좋아짐)
```
mat_1 = np.array(range(1,10)).reshape(3,3)
mat_1
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
	   
add_20  = lambda i: i + 20
vec_add_20 = np.vectorize(add_20)
vec_add_20(mat_1)
array([[21, 22, 23],
       [24, 25, 26],
       [27, 28, 29]])
	   
mat_1 + 10
array([[11, 12, 13],
       [14, 15, 16],
       [17, 18, 19]])
```

## 전치
* 행렬의 행과 열을 변경해 준다.
* `arr.T`
* `arr.transpose()`


## 유니버설 함수
* 데이터 원소별로 연산을 수행
	- 단항 유니버설 : __exp__, sqrt(제곱근)
	- 이항 : maximum, minimum, add(+)
	- e^x = exp(x)
		+ exp([1 ,4 ,9, 16]) = [e, e^4, e^9, e^16]
	- np.maximum(x,y,z)
		+ 개체들 중 최대값을 뽑아줌, shape과 type(float64, int32)이 같아야함
* arr = np.random.rand(10)
	- 랜덤의 숫자로 백터를 생성

## 메서드
* 합, 평균, 표준편차
	- sum
	- mean : 평균
	- std,var
	- min, max
	- arr.sort()
		+ np.sort(arr)
* arr.sum(axis=0)
	- 각각의 열의 합산
* arr.sum(axis=1)
	- 각각의 행의 합산
	
	
## 선형대수 연산
* 선형대수 : Linear한 함수를 풀기위해 사용
* np.dot(x,y)
	- x @ y
	- 행렬의 곱
* linalg 모듈
	- 선형대수에 필요한 역행렬과 행렬식에 관한 함수를 포함하고 있음
		+ det : 행렬식을 계산
		+ inv : 역행렬(정사각 행렬만 가능)

		+ eig : 고유값 고유벡터 계산
		+ qr : qr분해 계산
		+ svd : 특이값 분해 계산
		+ slove : 연립방정식 해 계산
		+ matrix_rank : 행렬의 rank를 반환한다.
* np.linalg.matrix_rank(w) # 독립차원의 차수
	- 독립차워느이 차수 참고 : https://rfriend.tistory.com/164
* np.ndim(w) #실제 차원은 아니다. tensor기준의 차원

---
# pandas
* 참고 : day2-1 

# part1 판다스 입문

## dict 2 series
* `import pandas as pd'
* 시리즈 만들기
```
dic_1 = {'a':1, 'b':2 ,'c':3}
ser_1 = pd.Series(dic_1)
ser_1
	a    1
	b    2
	c    3
	dtype: int64
```
```
list_1 = ['hello world', 231, 111.1111, True]
ser_2 = pd.Series(list_1)
ser_2
	0    hello world
	1            231
	2        111.111
	3           True
	dtype: object
```
```

tup_1 = ('hello world', 231, 111.1111, True)
ser_3 = pd.Series(tup_1)
ser_3
	0    hello world
	1            231
	2        111.111
	3           True
	dtype: object
```

* 인덱스 구조
```
ser_1.index
ser_1.values
```


* 원소 선택
```
ser_4 = pd.Series(tup_1, index=('헬로','월드','집에','가고싶다'))
ser_4
	헬로      hello world
	월드              231
	집에          111.111
	가고싶다           True
	dtype: object
```

## 2차원 배열(데이터프레임)
* 데이터프레임 만들기
```
dic_2 = {'a': [1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
df_1 = pd.DataFrame(dic_2)
df_1
		a	b	c
	0	1	4	7
	1	2	5	8
	2	3	6	9
```

* 행 인덱스/열 이름 설정
```
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], 
                   index=['준서', '예은'],
                   columns=['나이', '성별', '학교'])
```

* 행 인덱스 변경
`df.index=['학생1', '학생2']`
`df.rename(index={'준서':학생1, '예은':'학생2]}, inplace=True)`

* 열 이름 변경
`df.columns=['연령', '남녀', '소속']`
`df.rename(columns={'나이'='연령', '성별':'남녀', '학교':'소속'}, inplace=True)`

* 행/열 삭제
```
df.drop(['서준'],inplace=True)
df.drop(['수학'], axis=1, inplace=True)
```

* Data Frame 선택
	- 축 이름을 선택할때는(인덱스 이름) : loc
	- 정수형 위치 인덱스 : iloc

* 범위 슬라이싱
	- DataFrame 객체.iloc[ 시작 인덱스: 끝 인덱스: 슬라이싱 간격 ]
```
df.iloc[ : : 2]
df.iloc[0:3:2]
df.iloc[ : :-1]
```

* 열 추가
```
df_6['과학'] = [10,20,30]
```

* 행 추가
```
df_6.loc[4] = ['민엽',90,30,80,100,20,90]
```

* 원소 값 변경
```
df_6.loc['민엽'][['체육','음악']] = 50, 60
```

* 행, 열의 위치 바꾸기
	- 치환
```
df_7 = df_6.transpose()
df_7 = df_7.T
```

### 인덱스 활용
* 인덱스 지정 및 초기화
	- header에서 인덱스를 지정한다.
	- 멀티인덱스(MultiIndex)도 가능
```
df_6.set_index('이름', inplace=True)
df_6.set_index(['영어','과학'],inplace=True)
```
```
df_6.reset_index(inplace=True)
```

* 행 인덱스 재배열
	- 행 인덱스가 추가되며, NaN값이 입력됨(기본값)
	- Not a Number(NaN)
```
new_index =[{'r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
```

#### 정렬
```
df_7.sort_index()		# index 정렬은 잘 사용 안함
df_7.sort_values('수학') #오름차순
df_7.sort_values('수학',ascending=False) #내림차순
```

### 사칙 연산(산술연산)
* `stud_1 = pd.Series({'수학':10, "영어":20, "음악":30})`
* 시리즈 vs 숫자
```
stud_1 + 1
	수학    11
	영어    21
	음악    31
	dtype: int64
```

* 시리즈 VS 시리즈
* `stud_2 = pd.Series({'수학':20, "영어":50, "음악":20})`
```
stud_2 - stud_1
	수학    10
	영어    30
	음악   -10
	dtype: int64
```

#### 계산시 주의
* 값이 nan인 인덱스__와__ 값이 있는 인덱스와 연산시 = Nan
* 인덱스가 없는 값(값이 없는 인덱스)__와__ 값이 있는 인덱스와 연산시 = Nan
* __연산 메소드__를 사용해 값을 채운다.
	- add
	- sub
	- mul
	- div
```
stud_1.add(stud_2, fill_value=10)
```

### 데이터프레임 연산
* 데이터프레임 VS 숫자
	- `DataFrame 객체 + 연산자 + 숫자`

* 데이터프레임 VS 데이터프레임
	- `DataFrame1 + 연산자 + DataFrame2`
	- 동일한 위치의 원소끼리 계산
	- 원소가 존재하지 않거나, NaN이면 = NaN
	
---
# Part2 데이터 입출력
File Format|Reader|Writer
---|---|---
CSV|read_csv|tcsv
JSON|read_json|to_json
HTML|read_html|to|html
...|...|...
MS Excel| read_excel| to_excel

* 예
```
df_2 = pd.read_csv(file_1, header=None)
df_3 =pd.read_csv(file_1, index_col='c1') # header에서 인덱스 지정
csv 옵션 : p61-p62 참고
	- sep(delimiter) : 텍스트 데이터를 필드별로 구분하는 문자 - 쉽표(,), 탭(\t), 공백(" ")

df_5 = pd.read_html('./part2/sample.html')
	pandas.read_html("웹주소(URL)" 또는 'HTML 파일 경로(이름)')
```

### 여러 개의 데이터브레임의 하나의 Excel 파일로 저장
* `pandas.ExcelWriter('파일 이름(경로)')`
```
data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
        }
data2 = {'c0':[1,2,3], 
         'c1':[4,5,6], 
         'c2':[7,8,9], 
         'c3':[10,11,12], 
         'c4':[13,14,15]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

writer = pd.ExcelWriter("./df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name='sheet1')
df2.to_excel(writer, sheet_name='sheet2')
writer.save()
```


---
# Part3 데이터 살펴보기

### 대표값
* 데이터 수집 -> 대표하는 값 -> 평균(전체합/n)
* 중간값 -> 전체 데이터 n/2번재 있는 데이터
	- 평균의 오류
		+ 이상값(너무 크거나 작은값)이 있어 정확한 대표값이 아닐수 있음
* 최대값
* 최소값

### 데이터의 비교
* *__나눗셈__은 측량의 기준을 바꿔주는 행위*
* 편차 = (데이터값) - (데이터들의 평균값)
* 분산 = (편차 제곱 합) / (데이터 수)
	- 평균에서 각 값이 얼마나 떨어져있는지
	- 자료와 평균과의 거리(⇒편차)제곱에 대한 중간값. 또는 __거리들의 중간값__(직관적)
	- 변량들이 퍼져있는 정도, 분산이 크면 들죽날죽 불안정하다는 의미
	
* 표준편차
	- 정규화 : 데이터의 분포를 비교하기 위해 측정 단위로 통일, 데이터를 0 ~ 1 사이의 값으로 바꿈
		+ Xi - Xmin / Xmax - Xmin
	- 표준화 : 평균의 기준으로 거리를 재고, 그 값을 평균으로 만듦
		+ x - (x의 평균) / 평균과의 거리
	- => 표준편차, 분산 => 데이터의 분포 => 데이터를 비교 가능 => __상관계수__
* 상관계수


## 데이터 확인
* DataFrame 객체.head(n)
* DataFrame 객체.tail(n)
	- 기본값 5개
```
df_1= pd.read_csv('./part3/auto-mpg.csv', header=None)
df_1.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df_1.head()

mpg	cylinders	displacement	horsepower	weight	acceleration	model year	origin	name
0	18.0	8	307.0	130.0	3504.0	12.0	70	1	chevrolet chevelle malibu
1	15.0	8	350.0	165.0	3693.0	11.5	70	1	buick skylark 320
2	18.0	8	318.0	150.0	3436.0	11.0	70	1	plymouth satellite
3	16.0	8	304.0	150.0	3433.0	12.0	70	1	amc rebel sst
4	17.0	8	302.0	140.0	3449.0	10.5	70	1	ford torino
```

## 데이터 요약 정보 확인하기
* 데이터프레임의 크기(행,열)
```
df_1.shape # 행과 열의 개수를 튜플로 나타냄
```

* __데이터프레임 기본 정보__.info()
	- 자료형 출력
		+ `df_1.dtypes`
		+ `df_1.mpg.dtypes`
```
df_1.info()
	<class 'pandas.core.frame.DataFrame'>
	RangeIndex: 398 entries, 0 to 397
	Data columns (total 9 columns):
	 #   Column        Non-Null Count  Dtype  
	---  ------        --------------  -----  
	 0   mpg           398 non-null    float64
	 1   cylinders     398 non-null    int64  
	 2   displacement  398 non-null    float64
	 3   horsepower    398 non-null    object 
	 4   weight        398 non-null    float64
	 5   acceleration  398 non-null    float64
	 6   model year    398 non-null    int64  
	 7   origin        398 non-null    int64  
	 8   name          398 non-null    object 
	dtypes: float64(4), int64(3), object(2)
	memory usage: 28.1+ KB
```



* 데이터프레임 기술 통계 정보 요약
```
df_1.describe()
	mpg	cylinders	displacement	weight	acceleration	model year	origin
	count	398.000000	398.000000	398.000000	398.000000	398.000000	398.000000	398.000000
	mean	23.514573	5.454774	193.425879	2970.424623	15.568090	76.010050	1.572864
	std	7.815984	1.701004	104.269838	846.841774	2.757689	3.697627	0.802055
	min	9.000000	3.000000	68.000000	1613.000000	8.000000	70.000000	1.000000
	25%	17.500000	4.000000	104.250000	2223.750000	13.825000	73.000000	1.000000
	50%	23.000000	4.000000	148.500000	2803.500000	15.500000	76.000000	1.000000
	75%	29.000000	8.000000	262.000000	3608.000000	17.175000	79.000000	2.000000
	max	46.600000	8.000000	455.000000	5140.000000	24.800000	82.000000	3.000000
```

## 데이터 개수 확인
* 각 열의 데이터 개수
* `DataFrame 객체.count()`
	- 데이터프레임의 각 열이 가지고 있는 데이터 개수를 __시리즈 객체__로 반환
	- 단, 유효한 값의 개수만을 계산함

* 각 열의 고유값 개수
* `DataFrame 객체["열의 이름"].value_counts()`
	- 고유값이 행 인덱스가 되고, 고유값의 개수가 데이터 값이 되는 __시리즈 객체__ 반환
	- "dropna=True" 옵션 설정하면, NaN은 제외하고 개수 계산(기본값:False)

## 통계함수 적용
* 평균값
	- `DataFrame 객체.mean()`
	- `DataFrame 객체['열 이름'].mean()`
	
* 중간값
	- `DataFrame 객체.median()`
	- `DataFrame 객체['열 이름'].median()`
	
* 최대값
	- 문자열은 ASCII 숫자로 변환하여 크고 작음을 비교
	- 문자열과 숫자가 섞이면, 숫자도 문자열로 인식
	- `DataFrame 객체.max()`
	- `DataFrame 객체['열 이름'].max()`
	
* 최소값
	- 문자열은 ASCII 숫자로 변환하여 크고 작음을 비교
	- 문자열과 숫자가 섞이면, 숫자도 문자열로 인식
	- `DataFrame 객체.min()`
	- `DataFrame 객체['열 이름'].min()`

* 표준편차
	- `DataFrame 객체.std()`
	- `DataFrame 객체['열 이름'].std()`

* 상관계수
	- `DataFrame 객체.corr()`
	- `DataFrame 객체['열 이름의 리스트'].corr()`
	- `df[['mpg','weight']].corr()`

	
## 판다스 내장 그래프 도구
* `DataFrame 객체.plot()`
```
df_2 = pd.read_excel('./part2/남북한발전전력량.xlsx')
df_3 = df_2.iloc[[0,5], 3:]					# 필요없는 열 제거
df_3.index=['south','north']
df_3.columns = df_3.columns.map(int)		# header의 자료형을 int로 바꿈
df_3.T.plot()								# 기본값: 'line'
```


* 산점도 : 상관계수를 시각적으로 확인 가능
```
df = pd.read_csv('./part3/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.plot(kind='scatter', x='mpg', y='weight')
```

* 박스 플릇
	- 데이터의 분포와 분산 정도에 대한 정보 제공
	- 데이터의 범위/중앙값을 확인
	- 이상치의 존재 여부 확인 가능
	```
	df[['mpg', 'cylinders']].plot(kind='box')
	```

