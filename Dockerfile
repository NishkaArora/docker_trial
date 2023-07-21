#FROM continuumio/miniconda3

# This is an auto generated Dockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ros:noetic-robot

# install bootstrap tools
RUN apt-get -y update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
#RUN rosdep init && \
RUN rosdep update --rosdistro $ROS_DISTRO

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-base=1.5.0-1* \
    && rm -rf /var/lib/apt/lists/*


# ###### Installing miniconda3
# RUN apt-get update 
# #RUN apt-get install apt-transport-https
# RUN sudo apt-get install -y wget

# RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

# RUN bash Miniconda3-latest-Linux-x86_64.sh -b

# ENV PATH=/root/miniconda3/bin:${PATH} 

# RUN conda update -y conda

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app

#RUN conda env create --name nuplan -f /app/environment.yml
#SHELL ["conda", "run", "-n", "nuplan", "/bin/bash", "-c"]
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN sudo apt-get install -y python3.9
RUN sudo apt-get install -y curl

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.9 get-pip.py
# give 3.9 priority over python 3
RUN sudo ln -sf /usr/bin/python3.9 /usr/bin/python3

RUN sudo pip install -e .
RUN sudo pip install -r requirements_torch.txt
RUN sudo pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/your/custom/path"


#RUN conda env create -f environment.yml --name nuplan

# Run hello.py when the container launches
#CMD ["python", "tutorials/inference.py"]

#ENTRYPOINT ["conda", "run", "-n", "nuplan", "python", "tutorials/inference.py"]
