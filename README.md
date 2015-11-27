# Python Introduction
  
  
Richard Wen (init.r.w@gmail.com)  
  
A quick introduction to [Python](https://www.python.org/doc/essays/comparisons/) in Windows, which includes setting up python, using an IDE, and basic examples. The advantages to using Python include:  
* Easy-to-learn, short, and readable code  
* Packages and frameworks for a wide variety of applications  
* Increased productivity and reusable code  
  
**Requirements**  
* [Python 2.7](https://www.python.org/downloads/)  
* [Wing IDE](https://wingware.com/downloads/wingide-101) (Recommended)  
  
## 1.0 Quick Start  
1. Download and install [Python 2.7](https://www.python.org/downloads/) and [Wing IDE](https://wingware.com/downloads/wingide-101) (see the install guide in section 2.0)  
2. Download and unzip [this repository](https://github.com/rwenite/py-examples/archive/examples/intro.zip)  
3. Run cmd.bat  
4. Execute a simple Python file via the command line: `python sample\helloworld.py`  
5. Try the [basic examples](https://github.com/rwenite/py-examples/tree/examples/intro/sample) with Wing IDE 101 and refer to the [python docs](https://docs.python.org/2.7/)  
  
For more examples, switch branches  
  
**Package Installation**  
  
[pip](https://pip.pypa.io/en/stable/) is Python's package management system for packages found in the [package index](https://pypi.python.org/pypi). Run pip through the command line with your path variable set correctly `set PATH=%PATH%;C:\Python27\;C:\Python27\Scripts\`.  
    
* To get a list of available commands: `pip help`
* To get a list of installed packages: `pip list`  
* To install a package: `pip install package`  
* To uninstall a package: `pip uninstall package`  
* To upgrade a package: `pip install package --upgrade`  
* To upgrade pip on windows: `python -m pip install --upgrade pip`  
  
## 2.0 Install Guide  
  
**Python 2.7**  
  
Python is an open source and free programming language that is suitable for a wide variety of purposes.
  
1. Download and install [Python 2.7](https://www.python.org/downloads/) with default settings  
2. In a command prompt, type in `set PATH=%PATH%;C:\Python27\;C:\Python27\Scripts\`  
3. Then, type in `python` and you should be in the Python shell  
<img src="https://raw.githubusercontent.com/rwenite/py-examples/examples/intro/img/install4.jpg"  width="600;"/>  
  
**Wing IDE 101**  
  
Wing IDE 101 is an integrated development environment (IDE) complete with an editor, debugger, and console to make writing Python code easier.  
  
1. Download and install [Wing IDE 101](https://wingware.com/downloads/wingide-101) with default settings
2. Open Wing IDE 101 and go to: _Tools -> Python Shell_ and check that Python is running correctly; if not proceed to steps 3 and 4  
<img src="https://raw.githubusercontent.com/rwenite/ex-py-intro/master/img/wing2.jpg" width="600;"/>  
3.  Go to: _Edit -> Configure Python..._  
<img src="https://raw.githubusercontent.com/rwenite/py-examples/examples/intro/img/checkwing1.jpg"  width="400;"/>  
4. Select custom, browse to the directory of your installed Python, and select _python.exe_  
<img src="https://raw.githubusercontent.com/rwenite/py-examples/examples/intro/img/checkwing2.jpg" width="400;"/>  