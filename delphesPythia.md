### 도커를 이용해서 Delphes, Pythia 사용하기  

  
CCP에 Delphes 최신버전이 안 깔리는 관계로, 최신버전의 Delphes Pythia용 이미지를 만들었습니다.  
```bash
docker images
```  
로 현재 이미지를 확인할수 있구요, delphespythia8 입니다  
  
```bash
docker run -e DISPLAY=$DISPLAY -v 로컬마운트경로:컨테이너마운트경로 -it --name [사용할 컨테이너이름] delphespythia8 /bin/bash
```  
커맨드로 컨테이너 구동이 가능하구요,  
슈퍼 유저로 들어가려면 
```bash
docker exec -u 0 -it [컨테이너ID] bash
```  
로 들어가시면 됩니다.
