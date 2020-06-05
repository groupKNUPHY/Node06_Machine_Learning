## node06 DelphesPythia8 docker 사용법

### 1) node06 입장  
```bash  
$ ssh node06
```  

### 2) 이미지  확인  
```bash  
$ docker images
```  


### 3) 컨테이너 생성(이미 생성시 필요없음)  
```bash  
$ docker run -itd -v 마운트할 로컬 경로:/도커안에경로:ro --name [생성할 컨테이너이름] [이미지ID]
```  

### 4) 컨테이너 확인 
```bash  
$ docker ps
```  

### 5) 컨테이너 입장  
```bash
$ docker exec -it -u 0 [container ID] bash
```  

## DelphesPythia8  

1. Intro  
DelphesPythia는 config.cmnd 라는 파일을 먼저 만들어야 실행할 수 있습니다.  
LHE 파일을 바로 읽어드려서 Pythia8 Delphes6를 통과한 결과가 나옵니다.
실행법:  
```bash  
./DelphesPythia8 [card경로] [config.cmd경로] [output.root]
```  

  
2. Config.cmnd  
```bash
! 1) Settings used in the main program.

Main:numberOfEvents = 이벤트개수         ! number of events to generate
Main:timesAllowErrors = 3          ! how many aborts before run stops

! 2) Settings related to output in init(), next() and stat().

Init:showChangedSettings = on      ! list changed settings
Init:showChangedParticleData = off ! list changed particle data
Next:numberCount = 100             ! print message every n events
Next:numberShowInfo = 1            ! print event information n times
Next:numberShowProcess = 1         ! print process record n times
Next:numberShowEvent = 0           ! print event record n times

! 3) Set the input LHE file

Beams:frameType = 4
Beams:LHEF = LHE파일 경로
```  
