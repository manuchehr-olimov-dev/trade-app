Google Colab:
https://colab.research.google.com

Commands:

➡️!sudo apt update

!sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

!pip3 install --user --upgrade Cython==0.29.33 virtualenv


➡️!git clone https://github.com/kivy/buildozer
%cd buildozer

!python setup.py build

!pip install -e .
%cd ..

Now before running the next command upload your Python file

➡️ !buildozer init

Next, scroll down to the requirements and change them as follows:

requirements = python3, kivy==2.3.0, docutils, Kivy-Garden, pygments, pypiwin32

➡️!buildozer -v android debug