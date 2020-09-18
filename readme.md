## CCP GPU 서버  


1. List

 - Node06
	- Tesla p100-PCIE  x 1  
    - Tensorflow2  

 - Node07  
	- TITAN RTX x 2  
    - Pytorch 1.6.0 

2. Setup Environment  

 - Node06 Tensorflow2 docker server  

  1) Make Tensorflow2 container  
```bash
source /x5/cms/jwkim/TF_GPU/node06_docker/make_container.sh [YOUR WORKING DIRECTORY] [YOUR NAME or ID]   
```  

  2) Access above container  
```bash
source /x5/cms/jwkim/TF_GPU/node06_docker/Access_container.sh [YOUR NAME or ID]  
```  

  3) Please setup basic packages like git,vim,pandas,h5py.... in the container using **apt-get**  
  4) Default working directory in the container is **root/test** and this will be mounter to your real working directory  

  
 - Node07 Pytorch conda environment  

You can use almost all packages for machine learning with pytorch with this commands  

```bash
source /home/jwkim/Anaconda3/setup.sh
conda activate /home/jwkim/anaconda3/envs/Torch_node07/
```  

---






## Docker 사용법 기본  

### 도커권한주기  
도커는 기본적으로 ROOT권한을 필요로 합니다.  
이 문제를 해결하려면 ROOT권한을 가진 사람이 다른 유저에게  
도커 권한을 따로 부여 할 수 있습니다.
```bash
$ usermod -aG docker [유저이름]
```  

### 0. node06 공지  

- 도커를 이용해서 Delphes, Pythia8, ROOT를 돌릴수있는 이미지 파일을 만들었습니다.  

- 현재 도커를 이용해서 gpu용 텐서플로우를 이미지파일로 다운받았고 그 이미지 파일을  
각자 컨테이너화 시키는 방법을 이용해서 독립적인 개발환경을 세팅할 수 있습니다.  
도커에 대한 개념은 아래 참고자료에 나와있습니다.  
참고자료 링크: [Ref](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)  
  
- 현재 가장 최신 이미지는 __tensorflow_gpu_vim_jw_v2__ 와 __tensorflow_cpu_vim_jw__ 으로  
전자는 tensorflow gpu 버전, 후자는 tensorflow cpu버전이고,각각jupyter notebook이 깔려있습니다 /bin/bash를 이용해  
터미널 환경으로 접속하시면 우분투 기반의 툴이 열립니다. git 과 vim이 깔려있어서  
자유롭게 코드를 작성하시고 본인의 github repository와 연동해서 사용하실 수 있습니다  
CNN_test.py 코드가 테스트용으로 깔려있습니다. 파이썬으로 실행하시면 됩니다.  
  
- 컨테이너를 새로 생성하실 때에는 다른 유저와의 컨테이너와 혼동 예방으로,  
이름을 꼭 설정하시기 바랍니다. 혹시 깜빡했을 시 컨테이너 이름을 다음의 명령어로 변경할 수 있습니다.   
```bash
$ docker rename [현재 이름] [새 이름]
```  
  
- 컨테이너는 외부와 차단된 독자적인 환경이자, 컨테이너를 삭제하면 컨테이너 안의 모든 데이터를 손실하는  
휘발성을 가지고있습니다. 따라서 로컬 데이터와 컨테이너안의 파일을 자유롭게 옮기는 데 에는 제약이 있습니다.  
현재 최신 이미지 안에 git 과 vim을 깔아놨습니다. 본인의 github repository 와 연동하거나,  
github 에 옮기기 애매한 큰 용량의 파일들은 아래 __4.Docker 데이터 볼륨: 로컬디렉토리와 컨테이너 내부 디렉토리 연동__ 를 참고하시면 됩니다.  
  
  

- 현재 깔려있는 텐서플로우는 jpyter notebook 이라는 편리한 웹서비스를 연동하는 버전입니다.  
주피터 노트북 웹사이트: [Ref](https://jupyter.org/)  
하지만 지금 포트관련 지식이 부족해서 주피터 노트북을 이용할 수 없습니다.  
혹시나 로컬버전으로 텐서플로우를 실행하시는 중이라면 주피터 노트북을 이용하는것이 편리합니다.  
이 점도 공부해서 개선하겠습니다:)  
  
- 머신러닝 튜토리얼은 저의 github 계정에서 주기적으로 업로드 중입니다.  
__지웅 머신러닝__ [Ref](https://github.com/ico1036/Tensorflow_Anaconda)  
텐서플로우의 설치법 부터 텐서플로우 사용법, 머신러닝 이론등이 올라와있습니다:)   

---
---

### 작동 방법/도커 사용법  
아래 순서대로 
### 1. 설치되어있는 이미지 파일 리스트 확인
```bash
$ docker images
```  
현재 설치되어있는 이미지 리스트를 확인할 수 있습니다.  
도커는 이미지로부터 컨테이너를 실행하여 작업을 합니다.  
이미지는 문제가 있을때마다 업데이트를 할 예정입니다.
  
### 2. 이미지로부터 컨테이너를 생성하기  

```bash
$ docker run --runtime=nvidia -it -p [요청포트]:[포워딩포트] --name [생성할 컨테이너이름] [이미지ID] /bin/bash
```  
#### 1) p 옵션은 웹 이용을 안 할시에는 필요없습니다. [이미지ID] 뒤에는 명령옵션입니다 처음에 컨테이너를 실행할 때에는 입력을 안 하셔도 상관없습니다.  
#### 2) runtime 옵션은 gpu버전을 가동 할 때에만 필요합니다. cpu버전 이용시 빼주세요. 그 외 옵션은 아래에 정리했습니다.   
 - runtime=nvidia 엔비디아 gpu를 이용하는 텐서플로우 컨테이너를 생성합니다  
 - it 입력을 가능하게 합니다
 - p 8080:80 외부에서 Docker host의 8080포트로 요청이 들어오면 컨테이너의 80포트로 해당요청을 Forwarding 합니다
다른유저와 겹치지 않게 주의해주세요
 - /bin/bash bash쉘로 열어서 컨테이너 안으로 들어갑니다  
 - 컨테이너 안에서 [ctrl]+[p]+[q] 를 입력하면 밖으로 나갑니다
 - 컨테이너 이름을 설정하지 않으면 랜덤생성됩니다.
 - 컨테이너 생성 참고자료:  [Ref](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html)

### 3. 컨테이너 컨트롤 하는 명령어들

 - 현재 실행중인 컨테이너 확인
```bash
$ docker ps
# a 옵션: 정지된 컨테이너까지 포함
$ docker ps -a
```    
 - 정지된 컨테이너 실행
```bash
$ docker start [컨테이너 ID]
```  
 - 백그라운드 실행중인 컨테이너에 명령  
exec 를 이용해서 백그라운드 실행중인 컨테이너에 명령을 내릴 수 있습니다.  
아래 코드는 백그라운드 실행중인 컨테이너 안을 bash 환경으로 들어가는 예시입니다.
```bash
$ docker exec -it [컨테이너ID] /bin/bash
```  
 - 실행중인 컨테이너 정지하기
```bash
$ docker stop [컨테이너ID]
```  
 -정지된 컨테이너 삭제하기
```bash
$ docker rm [컨테이너ID]
```
컨테이너 이름을 보고 삭제해주세요!  
다른 유저 컨테이너 삭제하면 안됩니다ㅠㅠ  
 - 컨테이너 명령어 참고자료:  [Ref](https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html#%EB%8F%84%EC%BB%A4-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4)


### 4. Docker 데이터 볼륨: 로컬디렉토리와 컨테이너 내부 디렉토리 연동  
Doker 데이터 볼륨은 데이터를 컨테이너가 아닌 로컬 호스트에 저장하는 방식입니다. 데이터 볼륨을 사용하는 방법은  
여러가지가 있지만, root권한 문제등등 의 이유로 가장 직관적이고 할 수 있는 간편한 방법을 적어봤습니다.  
나머지 방식과 볼륨에대한 더욱 구체적인 설명은 링크를 참조하시기 바랍니다: [링크](http://pyrasis.com/book/DockerForTheReallyImpatient/Chapter06/04)  

  #### 1. 컨테이너와 공유할 디렉토리 생성하기  
볼륨을 이용하여 로컬호스의 특정 디렉토리와 컨테이너의 특정디렉토리를 마운트 한다고 가정해봅시다.  
그러면 서로 공유하는 디렉토리는 완전히 같은 디렉토리가 됩니다.  
즉 컨테이너 안에서 로컬디렉토리 안의 파일을 삭제/생성 할 수 있고 그 반대도 가능합니다.  
따라서 실수로 중요한 파일을 삭제하지 않기 위해, 먼저 로컬에서 컨테이너와 공유할 특정 디렉토리를 생성하고 따로 관리할 것을 부탁드립니다.  

  #### 2. 컨테이너의 디렉토리와 로컬호스트 디렉토리 마운트하기  
이미지로 부터 컨테이너를 생성 할 시에 마운트를 할 수 있습니다.  
```bash
$ docker run -itd -v /home/jwkim/test_dir:/root/test:ro --name jwkim [컨테이너ID] 
```  
위 명령은 로컬에 있는 test_dir 와 컨테이너 안의 test 디렉토리를 read only로 마운트하면서 컨테이너를 생성한 예시입니다.  
__-v__ 옵션을 이용해서 볼륨을 이용하여 마운트를 한다는 것을 선언하고, 순서대로 로컬에서 마운트할 디렉토리의 절대경로:  
컨테이너에서 마운트할 디렉토리의 절대경로:옵션이 됩니다.  
__ro__ 옵션을 주면 컨테이너안에서는 로컬에서 공유하는 디렉토리를 읽기만 할 수 있어, 원치않는 데이터 훼손을 방지할 수 있습니다.  
또한 컨테이너안에서 test라는 디렉토리가 없더라도, 로컬에 test_dir가 존재한다면 자동으로 생성되고 마운트가 됩니다.  
주의 할 점은 위 명령어를 치는 순간부터 마운트가 된다는 점 입니다. 컨테이너를 삭제해도 로컬에 마운트된 정보들은 남지만,  
다시 컨테이너를 생성할 때 -v 옵션부터 시작되는 위 명령어를 치지 않으면 마운트가 되지 않습니다.    

 #### 3. 마운트한 디렉토리 삭제하기  
로컬에서 1)번에서 만든 디렉토리를 삭제하면 컨테이너 안에서 마운트된 디렉토리에 들어가려는 순간  
Stale file handle 에러가 뜨면서 진입이 안 됩니다. 즉 마운트가 끊어집니다



