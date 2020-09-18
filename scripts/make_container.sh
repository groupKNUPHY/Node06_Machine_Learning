MOUNT_PATH=$1
YOUR_ID=$2


## Only for admin
#docker run --runtime=nvidia -it -p 8888:8888  -v /x5/cms/jwkim/TF_GPU:/root/test: --name jw_test_TF2_gpu f0b0261fec71 bash


# Run this
docker run --runtime=nvidia -it -p 8888:8888  -v $MOUNT_PATH:/root/test: --name $YOUR_ID\_TF2_gpu f0b0261fec71 bash
echo " ####################################################################### " 
echo "Container  $YOUR_ID\_TF2_gpu is created and mounted the path: $MOUNT_PATH "
