- 在按照pip3 install dlib之前需要：
brew cask install xquartz
brew install cmake
brew install boost
brew install boost-python --with-python3
brew install dlib

- pygraphviz安装如果失败，要进行操作：
http://jhartman.pl/2017/06/04/installation-of-pygraphviz-in-macos-10-12-sierra/
brew install graphviz
然后：
pip3 install pygraphviz --install-option="--include-path=/usr/local/Cellar//graphviz/2.40.1/include/" --install-option="--library-path=/usr/local/Cellar//graphviz/2.40.1/lib/"