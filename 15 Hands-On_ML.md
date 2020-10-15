# 15 Hands-On ML(Scikit-Learn, Keras, TensorFlow)
* 참고 ; 핸즈온 머신러닝_*장.ipynb

## 머신러닝을 왜 쓰는가?
* 전통적인 프로그래밍?
    - 문제 발생 -> 문제 해결??? 어떻게? -> 규칙작성
    - 규칙(알고리즘) 작성???? - > 소프트웨어 작성
        + 규칙 확인 -> 문제 발생 -> 문제 해결(알고리즘 수정) -> 확인 (반복)
* 머신 러닝은?
    - 문제 -> 문제 해결?? 어떻게??
    - 모델(알고리즘)을 만듦 -> 문제를 유발하는 데이터들 -> 모델을 학습(fit)시킨다.
        + 모델 확인(예측) -> 문제 발생 -> 문제해결(모델을 다시 학습시킴) -> 확인 (반복)
		
## 대표적인 머신러닝 어플리케이션
* 이미지
    - CNN(Convolutional Neural Network)
        + 합산곱 연산
        + 데이터들의 특징을 추출해 특징들의 패턴을 파악하는 구조
* 자연어 처리, 음성인식
    - RNN(Recurrent Neural Networks)
* 게임
    - 강화 학습
        - 심리학적 요소들
* 예술
    - GAN(Generative Adversarial Network)
        + deepfake 찾아내기
        + 데이터의 차이를 보정
* 분류
    - 군집알고리즘
        + 악성코드 분류/찾기

## 머신러닝의 종류
* 훈련 방법 : 지도(정답이 있음), 비지도(정답 레이블이 없음), 준지도(일부분의 정답만 있음), 강화(보상)
* 훈련 시점
    - 온라인 : 실시간 데이터 업데이트
    - 배치 : 이미 가지고 있는(준비된) 데이터로 학습
* 모델 생성
    - 사례 : 샘플을 기억함
    - 모델 : 샘플을 사용해 모델을 학습시킴

### 지도 학습
* 훈련 데이터에는 '레이블'이라는 원하는 답이 필요함
* 회귀 : 연속된 값(output)을 예측함
    - 선형 회귀
    - 로지스틱 회귀
* 분류
    - SVM
    - DT, 앙상블
* 신경망
    - 만능
    - CNN
    - RNN
    - GAN
    - GPT-3 : 자연어 처리 모델(범용)
	
### 비지도 학습
* 정답은 없음
    - 차이점을 찾아 분류함(군집화 함)
    - 시각화와 차원 축소
    - 연관 규칙 학습

* k - m
* PCA
* 가우시안

## 모델 기반 학습
* 모델을 만들어 예측함
* 간단한 선형 모델
	- 삶의 만족도 = b + a * (1인당_GDP)
	- 2개의 __모델 파라미터__ b와 a를 가짐
	- 모델 파라미터는 '피처'라고도 불림?

* 효용함수 or  적합도 함수 : 모델이 얼마나 좋은지 측정
* 비용함수 : 모델이 얼마나 나쁜지 측정
	- 얼마나 좋은지는 끝없이 값이 늘어나기 때문에, 0에 수렴할 수 있는 '비용함수'를 많이 쓴다.
	
### 선형 데이터
* Linear
    - 선형식
    - 1차 : W1X1 = b , X1 = b / W1
    - 2차 : W1X1 + W2X2 = b , X1 = (b - W2X2) / W1
    - 3차 : W1X1 + W2X2 + W3X3 = b
* 회귀 : 연속되는 값을 예측
* 선을 그리기 위해
    - 기울기 : a
    - 절편 : b
    - 삶의 만족도 = b + a * (GDP)
    - y = ax + b
	
## 정리
* 데이터 선택/분석
* 모델 객체 생성(선택)
* 모델 훈련
* 데이터 예측

---
## 머신러닝의 주요 과제
* 데이터가 충분하지 않음
    - 데이터가 많아야 학습이 잘된다
    - 학습이 잘 되면 성능이 좋은 알고리듬 탄생
* 데이터에 대표성이 없을 수 있다.
    - 샘플링 잡음 : 작은 샘플로 인한, 우연에 의한 대표성이 없는 데이터
    - 샘플링 편향 : 매우 큰 샘플이라도 추출 방법이 잘못되어 대표성이 없을 수 있음
* 낮은 품질의 데이터, 관련 없는 특성
* 과대 적합
	- 예측이 95%만 넘어도 overfitting일 확률이 높다
    - 훈련 세트에 너무 특화되어 있음 -문제점-> 실제 예측이 낮아진자.
    - Ex) 나는 모의고사만 판다 -> 수능망함
    - 해결방안은???
        + 규제를 사용(참고: p59)
		+ 하이퍼피라미터(규제하기 위해사용하는 값)를 사용 
* 과소 적합
    - 모델이 너무 학습이 안 되어있다.
    - 특징을 못 찾음
    - Ex) 주가 예측 -> 1/2 확률
        + 사람 40%, 침팬치 60%
	- 해결 방법
        + 더 강력한 모델을 선택
        + 훈련 알고리즘에 더 좋은 특성을 주입
        + 모델의 규제를 감소	
		
## 학습이 잘되는 기준?
* lost function OR loss function
* loss function -> 평균 -> cost

## 훈련 셋과 테스트 셋분류
* 테스트 셋을 구하기 힘들기 때문에 분류해서 학습을 시킴
* 데이터를 뽑아 분포를 확인(시각화), 데이터셋이 훈련셋과 같은지 확인(예측을 잘 하는지 확인)
* 학습전 훈련 셋과 테스트 셋으로 구분 한다.
    - 테스트 셋으로 미리 분석하면 안된다.
    - 테스트 셋으로 학습 -> 전체모델의 결과에 영향을 준다. (수능을 봐야 하는데 수능까지 학습함)
    - 테스크 셋의 크기 보통 20%, 
    - 데이터가 많아(5만개 이상). 1만개
* 훈련셋과 테스트셋을 구분할땐 어떻게 추출해야 할까?랜덤
    -  np.random
    - 컴퓨터는 랜덤이 가능할까???? - No
    - np.random.sedd(42) : seed를 지정하면 난수 발생의 초기값을 지정할 수 있다.

### 셋분류할 때, 사용하는 lib
* 넘파이모듈 사용 x
* 식별자 분류 x
* sklearn.model_selection.train_test_split(random_state=42) O

### 계층적 샘플링
* 요소를 고려하고 대상을 선택함
* 데이터 편향을 막음
    - 계층 기준
        + 소득, 나이, 성별
    - 범주를 지정하고 각 범주별로 샘플을 뽑아 낸다.
        + 학습과정의 평향을 막을 수 있음
        + 해당 계층이 제외되는 것을 막을 수 있음
```
Ex) 소득
1억 ~ 8000 : 80:20
8000 ~ 5000 : 80:20
5000 ~ 2000 : 80:20
2000 ~ 0 : 80:20
```

# 선형 모델 정리
* fit
	- 선형 모델에 학습을 시키면, 데이터 셋을 가지고 '기울기'과 '절편'을 자동으로 설정해주는 것
	- 이게 모델을 만들었다는 의미
	
# 모델 만들기 전에하는 과정
1. 문제 정의
	- 비지니스의 목적이 정확히 무엇인가?
	- 모델로 무엇을할려고 하는가?
	- 현재 솔루션(문제 해결 방법)은 무엇인가?
	- 현재의 솔루션보다 모델을 만들어 해결하는가 더 나은가?
	- 모델을 만들기 위해 어떤 방식을 사용할 것인가?
		+ 훈련 방법 : 지도, 비지도, 준지도, 강화
		+ 훈련 시점 : 온라인, 배치
		
2. 성능 지표 선택
	- 회귀 문제
	 	+ 평균 제곱근 오차(RMSE)
	 	+ 평균 절대 오차(MAE) : 이상치가 많으면 고려가능

3. 가정 검사
	- '분류'가 아니라 '회귀'를 사용하는게 맞는지 다시 확인
	
## 파이프 라인 생성 & 머신러닝 알고리즘을 위한 데이터 준비
* 데이터 전처리 : 주어진 데이터 변환
    - 왜? : 효율성을 위해
* 수치형 데이터 전처리
    - 데이터 정제 : 필요없는것 빼기
    - 조합 특성 추가
    - 특성 스케일링
        - 표준화(표준편차)
        - 정규화(min-max) : 최소, 최대를 0~1로 바꿈
* 범주형 데이터
    - 원-핫 인코딩 -> 확률
    - 숫자 True -> 1, False -> 0
        + 데이터 -> 1 or 0 -> 딥러닝 : 0.8 확률로 계산되어 나옴(예: 0.8퍼센트로 True이다)
        + 숫자 2 -> [0,0,1,0,0,0,0,0,0,0]
		
## Sklearn API 활용
* API를 이용하면 데이터 전처리에 관한 과정을 간편하게 구성할 수 있음
* API : 일관되게 설계해야 한다. -> 클래스 남용 금지(numpy array로 통일)
* API 종류
    - 추정기
        + 모델의 파라미터 추정, fit()를 사용
    - 변환기
        + 데이터셋 변환, transform()을 사용
            * 보통 fit(), transform() 동시에 사용
    - 예측기
        + 데이터 예측, predict()을 사용
            * fit(), predict()
			
## 모델 선택과 훈련

### 모델 선택
* 평균제곱근 오차(RMSE)
* MSE
* DecisionTreeRegressor
* RandomForestRegressor : 가장 좋음
* SVM(support vector machine, 서포트 벡터 머신) : 경계로 나눔
======================= 학습 완료

### 교차 검증
* k-겹 교차 검증
* 훈련세트를 '폴드'라 불리는 10개의 서브셋로 무작위로 분할
    - 10개를 각각 훈련시켜보고, 좋은 것을 선택
	- 9개는 폴드는 훈련에 사용, 1개는 평가(검증)에 사용
* 모델이 일관되게 동작하는지 확인 가능
    - 좋은 모델일수록 -> 표준편차가 작음(일관되게 학습됨)
	
## 모델 튜닝
* RandomForestRegressor 가장 성능이 좋다.
* 성능이 좋은 모델을 호출 후 튜닝한다.
    - 그리드 탐색
        + 수동으로 하이퍼 파라미터 조합을 찾는다.
        + 리스트로 하이퍼 파라미터를 지정 후 넣어준다.
    - 랜덤 탐색
        + 랜덤으로 조합을 찾아준다.(자동)
        + 하이퍼파라미터의 값의 횟수를 지정해주고 횟수만큼 반복한다. (low값과, high값을 결정해주고 횟수를 결정)
		+ `from sklearn.model_selection import RandomizedSearchCV`
    - 앙상블
        + 한개의 모델을 사용하는 것보다. 좋은 성능을 보이는 여러개의 모델을 조합하여 더 좋은 성능을 나타나게 만든다.
		
### 최상의 모델과 오차 분석
참고 : p118

### 테스트 세트로 시스템 평가하기
참고 : pp119-120

---
# CHAPTER 3 분류

## MNIST
* 미국조사국 직원들이 손으로 쓴 70,000개의 작은 숫자 이미지

## 이진 분류기
* 맞냐 틀리냐? 두개로 나눈다.
    - 이진분류를 반복하면 다중분류가 가능해 진다.

* 모델을 선태하여 훈련시킨다.
    - '__확률적 경사하강법__'을 통해 아래 3가지로 변함
        + 퍼셉트론
        + LogisticRegression : 분류 모델
        + SVM(support vector machine, 서포트 벡터 머신) : 경계로 나눔
* 확률적 경사하강법
    - 학습데이터의 단위를 배치라 하고, 배치 사이즈가 1인 분류기
    - 한번에 하나씩 훈련샘플을 처리해서 학습

```
from sklearn.linear_model import SGDClassifier

SGDClassifier(loss='perceptron')
SGDClassifier(loss='log')
SGDClassifier(loss='hinge')  # 기본값 SVM
```
* SGD : Stochastic(확률적) Gradient(기울기) Descent(하강)

# Set
* Test(수능) vs Training(사설모의고사) vs Validation(평가원 모의고사)
    - 모델을 검증하는 과정에서 Test Set을 사용한다. Test Set = Validation
    - 문제점
        + Test Set을 이용해 모델의 성능을 확인하고 -> 파라미터 수정 -> Test에서만 잘 동작하는 모델이 생성된다.
        + Trainnig -> Validation 보정 -> Test으로 평가
        + Test(1) : Training(8) : Validation(1)
  
* Validation Set을 사용했을 때 장점
    - 과적합 문제를 해결할 수 있다.

* 검증세트를 통해 모델 선정 과정
    1. Trainig Set으로 Model 학습
    2. 학습괸 모델을 Validation Set으로 평가
    3. Validation Set에 대한 결과로 모델 파라미터 조작
    4. 가장 우수한 모델 선택
    5. 그 모델로 Test Set 평가
	
### 교차 검즘
* 단순교차 검증
    - 예) k=3인 경우
    - trainig 데이터를 3구간으로 나누고, 3구간으로 또 나눔(9개 구간)
    - 그리고 3구간은 Validation Set으로 사용하고, 6구간은 training
    ```
    from sklearn.model_selection import cross_val_score
    cross_val_score(모델객체, 훈련데이터, 타겟, cv=폴드수)
    ```
* 계층별 K-겹 교차검증
    - 편향된 데이터의 경우 단순교차 검즘으로는 문제가 발생할 수 있다.
    - 계층을 나누고 분할해서 뽑는다.(자동)
    ```
    from sklearn.model_selection import StratifiedKFold
    skf = StratifiedKFold(n_splits=3, random_state=42, shuffle=True)
    cross_val_score(sgd_clf, X_train, y_train_5, cv=skf)
    ```   
* 임의분할 교차검증
    - Train_size와 test_size를 데이터 개수(정수) 또는 비율(실수)로 정할 수 있다.
    - 4번 반복 분할 25%가 검증세트가 된다.
    - 10%를 검증세트로 4번 반복분할하여 학습시킬 수 있다.
    ```
    from sklearn.model_selection import ShuffleSplit
    ss = ShuffleSplit(n_splits=8, random_state=42, test_size=0.5, train_size=0.5)
    cross_val_score(sgd_clf, X_train, y_train_5, cv=ss)
    ```
* 나오는 값은 '정확도'를 의미   
 
## 오차 행렬(Confusion Matrix)
```
from sklearn.metrics import confusion_matrix
```
* 행 : 실제 Class(target)
* 열 : 예측 Class(predict)
* TP(True Positive), FP(False Positive), FN(False Negative), TN(True Negative)

* 정밀도(Precision)
    - 모델이 True라고 예측한 것 중에서 실제 True인 것에 대한 비율
    - TP(True Positive) / TP + FP(False Positive)
    - 예) 맑다고 예측했는데 실제 맑은날 비율

* 재현율(Recall)
    - 실제 T 모델이 T라고 예측하것의 비율
    - TP / TP + FN(False Negative)
    - 예) 실제 맑은날 중에 맑다고 예측한 비율
    
* 두 얼굴 중 한 사람 얼굴 찾음
    - Precision: 100%
    - Recall: 50%
    
* 정밀도 VS 재현율
    - 실제 Positive인 데이터를 Negative로 잘못 판단하면 안되는 경우 '__재현율__'을 사용
        - 인증, 악성코드, 병진단
        - 실제로 양성인데 음성으로 판단하면 -> 병을 키울수 있다.
    - 실제로 Negative인데 Positive로 잘못 판단하면 안되는 경우 '__정밀도__'를 사용
        - 스팸메일
        - 스팸메일이 아닌데 스펨메일로 판단하면 -> 중요 메일을 못받음
        
* 정밀도는 낮아지고 재현율이 높아진다 -> 예측을 많이 함(골결이 낮다. 호난사)
* 정밀도가 높아지고 재현율이 낮다 -> 신중하게 예측을 함. (찬스는 낮지만, 골결이 높다. 손날두)

* confidence Threshold 값에 따라 정밀도와 재현율의 수치가 조정되고(서로 상보적), trad-off가 발생한다.
    - trad-off : 한쪽이 올라가면 다른쪽이 내려가는 모순적 관계를 이르는 말

## 다중 분류
* OvR/OvA
    - 0 vs all/{0}
    - 1 vs all/{1}
    - 2 vs all/{2}
* OvO
    - 각 Class마다 2진 분류실행 N(N-1)/2 = n_C_2
    - combination 연산을 함
    - 5 vs 0
    - 5 vs 1
    - 5 vs 2
    - ...
    
* 보통은 OvR을 선호
    - 훈련셋이 많으면 OvR

---
# CHAPTER 4 모델 훈련
* Data -> 변수 1개, x -> y
* 연속형 데이터
    - 값을 예측

* 분류형(범주) 데이터
    - class를 분류

## 선형회귀 모델
* 선에서 벗어난 오차를 '입십론($\epsilon$)'이라 부름
    - f(Xn) + 입실론 = Yn
    - 에측            실제값
* 각각의 '입실론'을 최소화시키는게 선형 회귀 모델임
    - $ f(X) = \beta0 + \beta1X + \epsilon(범위) $
        + predict=$\beta0+\beta1X$
    - 오차 : 우리가 인정할 수 있어야 한다.
        + \epsilon_i$의 분포가 정규분포 안쪽 -> 인정 가능
    - 정규 분포는 : E(입실론i) = 0
    
### Cost function
* $\displaystyle \sum_{i=1}^n (Y_i-\widehat{Y_i})^2$
* Cost function이 최소화 되는 값을 찾는게 목표!
* root 금지 - 미분이 어렵게 됨
* 거리의 방향을 제거한
* 예)
    - 범위 : 1 ~ 6
    - predict function : 2
    - cost : (1-2)^2 + (6-1)^2 = 17
    - predict function : 3
    - cost : (1-3)^2 + (6-3)^2 = 13
    - predict function : 4
    - cost : (1-4)^2 + (6-4)^2 = 13
    - 그래프는 곡선($\cup$)일 것이다.
        + 그래프의 최하단이 cost값을 최소화 한다.
        
* $f(\beta_{0},\beta_{1})$
    + 변수 $\beta_{0}, \beta_{1}$

* $\beta$가 2개면 그래프가 입체적으로 변함 곡선뿔(아래로 볼록?)같은 형태

### 미분
* 기울기 0을 찾을 때 사용 가능
    - __기울기가 0이 cost값이 최소__
    
* $\beta$가 1개
    - 그냥 '미분'함
    - $\beta_0$에 대해 미분

* $\beta$가 2개
    - 다변량 '미분'함
    - $\beta_{0}, ..., \beta_{1}$에 대해 미분

#### 미분
* __접하는 선(line)의 기울기__
    - 순간 속력(순간 변화량)
* 이동거리 : 2km -> 3시간
* 평균속력 : 2/3 -> km/시간
    - 평균속력 : 거리의 변화량 / 시간의 변화량 = __기울기__

$\displaystyle \lim_{\vartriangle t \to 0}  {f(t) - f(t+\vartriangle t) \over \vartriangle{t}}$ : 순간 속력

* __기울기 = 0 => 미분 = 0__

## Cost function의 미분
### 1) $\beta$가 1개
* $cost'(\beta_{0})$, ${d \over d\beta_{0}} cost(\beta_{0})$
* ${d \over d\beta_{0}} cost(\beta_{0})$ = $0 -2Y_i +2\beta_0$
    - $\beta_0$ = $\sum Y_i$
    
### 2) $\beta$가 2개 (편미분, 다변수 미분)
* 이미지 참조 : 1.pdf

* $\partial$(파셜)
    - $\partial cost(\beta_{0},\beta_{1}) \over \partial \beta_{0} = 0$
    - $\partial cost(\beta_{0},\beta_{1}) \over \partial \beta_{1} = 0$
    
* 변수 2개 식 2개 => 연립 방정식
    - 이미지 참조 : 1.pdf
    
* 변수 3개, 미분 3번, $\beta_0, \beta_1, \beta_2$ => 연립방정식
    - $\beta_0 + \beta_1 X_1 + \beta_2 X_2$
    
### 다변량 '미분'이 '일반화'되면?
* __정규방정식__이 나타난다.
* 정규방정식의 표기법?
    - 이미지 참조

### cost function
* 정규방적식 사용은 컴퓨터에게 부담이 된다.
    - => $ \sum_{i=1}^n (XB-y)^2$ '미분'하면 => 0
    - $0 - 2X^T(XB-y)$
    - ...
    - $B = (X^TX)^{-1} X^Ty$ : 정규 방정식

## 경사 하강법
* 선형회귀 풀이 2번째
* Cost functinon => cost($\beta$)
    - 목적 : $cost'(\beta) = 0 인 \beta을 찾는것$
    - 방법 1 : $\beta \in R^n$에 대해 무차별 대입
    - 방법 2 : 적당한 규칙을 적용 => 순차적으로 업데이트 => 결과
        + 적당한 규칙 : 이미지 참조(1.pdf)
        + 기울기가 0이 될 때까지 반복 => B = B - n*0 = B
        
* 정규방적식 풀이는 컴퓨터에게 엄청난 부담을 준다.
* 에타($\eta$) : 학습률(Learning rate), 사용자가 정하는 값, 하이퍼파라미터
* 베타($\beta$) : 구할려는값(기울기, 절편)

## 배치 경사 하강법의 종류
* BATCH(배치) 사이즈를 기준으로 종류를 나눔
1. 많은 피처(Feature, 특성)를 몽땅 학습시키면
    - 문제 : 오래거림, 메모리 부족
2. 데이터를 나눠서 여러번의 학습 과정

1. epoch, step, batch size
    - epoch : 전체 샘플(Sample) 한 바퀴 돌면, 1 epoch
    - step : 기울기(가중치, Weight),  편향(절편, Bias) 1회 업데이트, 1 setp
    - batch size : 1 step에서 사용한 데이터의 수
        + 몇 개를 학습 시킬지 정함

**식 4-6: 비용 함수의 그레이디언트 벡터**

$
\dfrac{\partial}{\partial \boldsymbol{\theta}} \text{MSE}(\boldsymbol{\theta})
 = \dfrac{2}{m} \mathbf{X}^T (\mathbf{X} \boldsymbol{\theta} - \mathbf{y})
$

**식 4-7: 경사 하강법의 스텝**

$
\boldsymbol{\theta}^{(\text{next step})} = \boldsymbol{\theta} - \eta \dfrac{\partial}{\partial \boldsymbol{\theta}} \text{MSE}(\boldsymbol{\theta})
$

## GD(Gradient descent,경사 하강법)
* Full Batch GD
* Batch size = m = 전체 데이터
* matrix 연산
    - m번 계산후 업데이트

## SGD(Stochastic Gradient Descent, 확률적 경사 하강법)
* batch size = m = 1 (랜덤으로 추출된 1개의 데이터를 사용하여 업데이트)
* 벡터단위 연산
    - 장점 : 업데이트가 빠르다. (1번 계산으로 업데이트)
    - 단점 : 행렬 연산의 장점이 사라진다.
    
## Mini Batch GD
* batch size = m = 사용자가 지정 $2^n$로 지정
    - 장점 : matrix 연산 사용
    - 단점 : SGD보다 느리다.



## Cost function
* 입력한 Training Set에 대하여 가장 적합한 직선을 우리가 가질 수 있게 해줌 = 목표
* Cost = (h - y)^2
    - Cost = 예측된 결과 값(h) - 실제 결과 값(y)
    - 음수로 값이 없어지면 안되기 때문에 제곱함

# 개인 정리
1. 선형 회귀에서 미분을 사용하는 이유?
  - __Cost function__의 최소값을 구하기 위해서
  - 미분을 사용하면 기울기 0을 구할 수 있어서, 기울기 0이 최소값
2. 미분이 순간속력을 구하는 거고, 미분은 방향(-/+)을 가지고 있는게 맞나요?
  - 미분 : 순간적인 변화
  - yes
3. 구하는 $\beta$는 '기울기'와 '절편'을 뜻하는가?
  - yes
4. cost function이 MSE와 같다고 할수 있나요?
  - MSE 는 Cost Function의 한 종류 입니다
