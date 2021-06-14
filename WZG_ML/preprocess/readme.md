### Pre-Process ###

# dataframe make code
[Uproot to dataframe](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/preprocess/binary_make.py)

# 1. 데이터 로드 및 정리
- 각 채널들의 npy 파일을 로드 (eee, eem, emm, mmm)
- 채널, 프로세스에 따라서 데이터들을 dict로 정리
- Weight를 위한 lumi, genevt, xsec를 dict로 정리
- (for문을 이용하여 원하는 column의 데이터들만 뽑아서 정렬)
- def 를 통해 프로세스별로 특정 번호 부여 및 각 프로세스의 genevt, xsec를 넣고, 데이터를 순차적으로 읽어서 dataframe 만들기
- pandas 형태로 데이터 제작 및 df.to_hdf를 통해 hdf5 형식으로 저장


# 2. column 변경
- [Control Columns](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/preprocess/coladd.py)
- 위에서 저장한 hdf5 형식의 파일 읽기
- df.drop으로 필요없는 column 삭제 (lepton mass 등...)
- 새로 만들어줄 column의 variable 정의
- df['column_name']으로 데이터에 column 추가
- df.to_hdf로 새로운 데이터 hdf5 형식으로 저장
 
