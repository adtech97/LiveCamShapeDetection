1. We need to install 'NOOBS' in the raspberry pi
	i) Download 'NOOBS' And extract contents in SD card
       ii) Begin the installation and wait till setup is complete

2. Now we need to install opencv libraries for python.For installing opencv
   follow the steps

	a)use commands
		1)sudo apt-get install python-opencv
		2)sudo apt-get install python-matplotlib
		3)sudo apt-get install python-scipy
		4)sudo apt-get install ipython
NOTE:- For testing purpose Just type python in Terminal and do import cv2 if it executes perfectly then you are done

	b)Also you can use traditional method
			1. Generic Stuff
						sudo apt-get update
						sudo apt-get upgrade
						sudo rpi-update
						sudo reboot
						sudo apt-get install build-essential git cmake pkg-config
						sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
						sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
						sudo apt-get install libxvidcore-dev libx264-dev
						sudo apt-get install libgtk2.0-dev
						sudo apt-get install libatlas-base-dev gfortran
						cd ~
						git clone https://github.com/Itseez/opencv.git
						cd opencv
						git checkout 3.1.0
						cd ~
						git clone https://github.com/Itseez/opencv_contrib.git
						cd opencv_contrib
						git checkout 3.1.0
			2. For python 2.X
						sudo apt-get install python2.7-dev
						wget https://bootstrap.pypa.io/get-pip.py
						sudo python get-pip.py
						pip install numpy
						cd ~/opencv
						mkdir build
						cd build
						cmake -D CMAKE_BUILD_TYPE=RELEASE \
							-D CMAKE_INSTALL_PREFIX=/usr/local \
							-D INSTALL_C_EXAMPLES=OFF \
							-D INSTALL_PYTHON_EXAMPLES=ON \
							-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
							-D BUILD_EXAMPLES=ON ..
						make -j4
						sudo make install
						sudo ldconfig

			2.1 For python 3:
						sudo apt-get install python3-dev
						wget https://bootstrap.pypa.io/get-pip.py
						sudo python3 get-pip.py
						pip install numpy
						cd ~/opencv
						mkdir build
						cd build
						cmake -D CMAKE_BUILD_TYPE=RELEASE \
						    -D CMAKE_INSTALL_PREFIX=/usr/local \
						    -D INSTALL_C_EXAMPLES=OFF \
						    -D INSTALL_PYTHON_EXAMPLES=ON \
						    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
						    -D BUILD_EXAMPLES=ON ..
						make -j4
						sudo make install
						sudo ldconfig

NOTE :- In The Project we are using python 2.4.13 because there is very Less support for python3.x
#LiveCamShapeDetection
