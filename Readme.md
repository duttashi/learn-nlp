Tutorial: Natural Language Processing in Python
=====

This repo contains material for a `1-semester course` on Natural Language Processing with Python.

### Audience
-----

The target audience are students, researchers, developers, hobbyists and anyone interested in knowing more about Natural Language Processing and Text Analytics.

Some very basic knowledge of Python is assumed (e.g. if you have seen some Python script before, you're good to go), but no previous NLP knowledge is required.

### Environment Set up
-----
The code has been tested with Python 2.7 only on Windows 7 64-bit OS. 

**Step 1** - Navigate to desktop and clone this repo

- Open PowerShell by pressing and releasing the keys `Windows` and `R` together on the keyboard and release these two keys together. If you have done it right, then a `Run` dialog box will open up. Type “powershell” in Run dialog box and click the `OK` button.
     
- In PowerShell type the command `cd c:\users\yourusername\desktop` (*ensure to subsitute yourusername*) and press the enter key on the keyboard.

- Now type the command `git clone https://github.com/duttashi/learn-nlp`
    
**Step 2**- Install Anaconda and iPython Notebook

- Downloads and install Anaconda from [here](https://www.anaconda.com/download/). **Choose Python 2.7 version**. Select the default options when prompted during the installation of Anaconda.

- Launch IPython notebook by typing `jupyter notebook` in PowerShell

**Step 3**- Check installed libraries versions

- Click the `new` button on the notebook.

    ##### scipy
    import scipy
    print('scipy: %s' % scipy.__version__)
    ##### numpy
    import numpy
    print('numpy: %s' % numpy.__version__)
    ##### matplotlib
    import matplotlib
    print('matplotlib: %s' % matplotlib.__version__)
    ##### pandas
    import pandas
    print('pandas: %s' % pandas.__version__)
    ##### statsmodels
    import statsmodels
    print('statsmodels: %s' % statsmodels.__version__)
    ##### scikit-learn
    import sklearn
    print('sklearn: %s' % sklearn.__version__)

You should see output like the following:

    scipy: 0.19.0
    numpy: 1.12.1
    matplotlib: 2.0.2
    pandas: 0.20.1
    statsmodels: 0.8.0
    sklearn: 0.18.1

**Step 4**- Install Deep Learning Libraries

In this step, we will install Python libraries used for deep learning, specifically: Theano, TensorFlow, and Keras.

NOTE: While installing the deep learning libraries, if you encounter any error, check out the `Issues` tab or else search for possible answers on `www.stackoverflow.com` website.

- Install the Theano deep learning library by typing: `conda install theano`
- Install Keras by typing: `pip install keras`

Confirm your deep learning environment is installed and working correctly by executing the following commands in the `ipython notebook`

    # theano
    import theano
    print('theano: %s' % theano.__version__)
    
You should see an output like;

theano: 0.9.0.dev-c697eeab84e5b8a74908da654b66ec9eca4f1291

	# keras
    import keras
    print('keras: %s' % keras.__version__)

Note: keras requires tensorflow which will work with python3. Will leave this as a future work. This work involves removing anaconda ipython 2.x and installing version 3.x by following Step 2.

### Summary

Congratulations, you now have a working Python development environment for machine learning.

You can now learn and practice machine learning and deep learning on your workstation.

### Where to go from here?

Please see the folder scripts where you will find `ipython notebooks` for further learning.

Here are some interesting questions and answers on StackOverflow. I recommend these should be read in the order, `On Statistical knowledge`- [1](https://stackoverflow.com/questions/2039904/what-statistics-should-a-programmer-or-computer-scientist-know), `On data mining`- [2](https://stackoverflow.com/questions/5064928/difference-between-classification-and-clustering-in-data-mining), [3](https://stackoverflow.com/questions/10059594/a-simple-explanation-of-naive-bayes-classification).  

Enjoy and Keep Calm!



  
