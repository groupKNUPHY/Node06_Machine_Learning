## Project: Application of DNN to WZgamma signal classification  

### Prerequisite
 - 사용가능한 노드: Node06, Node07 (GPU기반으로 작동하게 코딩해놨습니다, CPU도 가능하지만 테스트 안 해봤고 느립니다)  
 - 프로젝트에 필요한 모든 python library를 셋팅합니다 ( 가상환경 )
```bash
source /home/jwkim/Anaconda3/setup.sh  # JiWoong 가상환경 불러오기
conda env list # 가상환경 리스트확인
conda activate Torch_node07 # pytorch 가상환경으로 설정
```


### 1. Preprocessing step
 - [여기서 확인해주세요](https://github.com/groupKNUPHY/Node06_Machine_Learning/tree/master/WZG_ML/preprocess)


### 2. Traing step
 - Training python script: [run/train.py](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/run/train.py)  
    - Data loader로 데이터를 불러온뒤, traing validation test dataset 으로 6:2:2 로 나눕니다. Training 데이터는 랜덤 셔플링 합니다.   
    - DNN model class를 불러와서 Model 을 학습시킵니다. 동시에 Validation 셋으로 검증을해서 Loss와 Acc 정보를 저장합니다.
    - Validation data를 기반으로, Loss 가 가장 낮은 epoch의 weight 만 model업데이트에 사용합니다. (overfitting 된 weight는 모델업데이트에 반영되지않습니다)  

    
 - Data loader class: [python/DataLoader.py](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/python/DataLoader.py)
    - Data 를 불러오고 Minmax scale 등의 전처리를 하는 클래스입니다
    - 여기서 Input data path 를 정의합니다 (/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/WZG_ML/data/binary.h5 
)
    
 - DNN architecture class: [python/Model.py](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/python/Model.py)
    - DNN 구조가 담겨있는 클래스입니다


### 3. Training monitoring step
 - Learning curve: [util/epoch_vs_loss.py](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/util/epoch_vs_loss.py)  
    - epoch vs Loss 그리고 epoch vs accuracy 를 plotting 합니다
    - usage:
```python
python train.py --h # Show argument list
python train.py --epoch EPOCH  --batch BATCH --lr LEARNING_RATE
```

### 4. Evaluation step  
 - Evaluation using test dataset: [run/Eval.py](https://github.com/groupKNUPHY/Node06_Machine_Learning/blob/master/WZG_ML/run/Eval.py)  
    - 학습된 모델 (weightFile.pth) 을 읽어오고, test dataset 을 넣어서 evaluation 
    - Evaluation 결과가 저장된 prediction.csv 파일이 만들어지고, 이 파일을 읽어서 ROC, DNN score 가 그려집니다. 
    - usage
```python
python Eval.py --h # Show argument list
python Eval.py --epoch EPOCH  --batch BATCH --lr LEARNING_RATE
```
