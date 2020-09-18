
## Only for admin
#docker exec -it jw_test_TF2_gpu bash


ID=$1


echo " Access to the container: $ID\_TF2_gpu..... "
echo " Please use the [ctrl] + p + q command to exit " 
## Run this
docker exec -it $ID\_TF2_gpu bash



