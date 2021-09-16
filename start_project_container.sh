#!bin/bash

sudo chmod 777 ./job_in_docker
sudo xhost +local:root

sudo docker run --entrypoint ./runapp.sh --gpus all -e "ACCEPT_EULA=Y" --network=host \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v /etc/localtime:/etc/localtime:rw \
        -v $PWD/job_in_docker:/root/job_in_docker\
	-e QT_X11_NO_MITSHM=1\
	-e NVIDIA_VISIBLE_DEVICES=all\
	-e NVIDIA_DRIVER_CAPABILITIES=all\
	-e XAUTHORITY=/tmp/.docker.xauth \
        -e DISPLAY=unix${DISPLAY} lottoworld777/project:0.91
# job_in_docker is a sharing folder for sharing local files, fodlers, etc..
