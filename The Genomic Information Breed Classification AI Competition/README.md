###
label encoding, one-hot encoding 시 test 데이터 셋 활용하여 encoder를 fit하는 경우
data scaling 적용 시 test 데이터 셋 활용하여 scaler를 fit하는 경우
pandas의 get_dummies() 함수를 test 데이터셋에 적용하는 경우
test 데이터 셋의 결측치 처리 시 test 데이터 셋의 통계 값 활용
test 데이터 셋을 EDA하여 얻은 인사이트를 통해 학습에 활용하는 경우
test 데이터 셋을 학습 과정에 사용하는 모든 행위 (test 데이터셋은 추론에만 활용되어야 합니다)
test 데이터 셋의 데이터 개수 정보를 활용하는 경우 (실제 test 데이터셋은 몇개가 입력으로 들어올 지 모르기 때문)
위 예시 외에도 test 데이터 셋이 모델 학습에 활용되는 경우에 Data leakage에 해당됨.

['id', 'father', 'mother', 'gender', 'trait', 'SNP_01', 'SNP_02',
       'SNP_03', 'SNP_04', 'SNP_05', 'SNP_06', 'SNP_07', 'SNP_08', 'SNP_09',
       'SNP_10', 'SNP_11', 'SNP_12', 'SNP_13', 'SNP_14', 'SNP_15', 'class']

1. 파일 설명
    - 1. 전처리
    - 2. 모델 
    - 3. 저장한 모델 로드

2. 12월 13일
    - 전처리 : 원핫-trait, SNP-라벨인코딩, drop-father,mother,gender
    - 모델 : catboost 사용
