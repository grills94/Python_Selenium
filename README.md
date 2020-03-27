# Python Selenium Framework
The aim of this project began with a group of individuals, of different skill levels within Python, to get together and walk through setting up a Python Selenium framework.

# Day 1 - Project Setup

First day we made the simple steps to create a project in PyCharm, add the necessary packages and set up our `setup.py` and `requirements.txt` files.

We threw together a quick `hack_file.py` to get a basics up and running and to ensure everyone's machines where functioning as expected.

## What is the setup.py Vs requirements.txt?
We have setup two files in the `setup.py` file and the `requirements.txt` and both are involved in setting up your Python environment. They do have some subtle differences in their uses though.

### setup.py
The `setup.py` is mainly used to document and setup your python packages for distribution purposes. It is mainly used to set up details for an end users system - in short deploying a final 'product' as a package.

```python
from setuptools import setup

setup(
    name='python_selenium_example',
    version='0.1',
    packages=['pytest'],
    url='',
    license='MIT license',
    author='Kieran Cornwall',
    author_email='kcornwall@spartaglobal.com',
    description='Hackathon effort at Selenium framework',
)
```

As you can see in our setup above we're stating a package of `pytest` which should form part of any dependency/package installation when being deployed.

### requirements.txt
The `requirements.txt` file relates more to development environment setup, in one fail swoop you can run `pip install -r requirements.txt` and have all dependencies for a development environment installed.

### So, why bother with both?!?!?!?
your development requirements maybe very different from your 'production/packaged' product. If you have built a website using Python Django (Python's MVC framework) and you're using selenium to test the front end... the truth is you don't need to deploy selenium to the production environment you only run it in development.

So, to reduce deployment time it makes sense to only install packages needed to run on the production service :-).

## Additional points
* A `web_drivers` folder has been added and the chromedriver (version 80.0.3987.106) has been added into the folder and already referenced in the `hack_file.py` to assist in ease of use:

```python
from selenium import webdriver

driver = webdriver.Chrome("../web_drivers/chromedriver")

driver.get("https://www.bbc.co.uk/")
```

The line `driver = webdriver.Chrome("../web_drivers/chromedriver")` is already referencing the chromedriver held within the `web_drivers` folder so should run out of the box all things being well and that the version of chrome being used aligns with the chromedriver.

# Day 2 - Some basic usage

On day 2 we have covered setting up a basic file that will run Selenium objects.

running the `hack_file.py` should produce a basic Selenium run.

***Important note***

If using Windows ensure the driver instantiation is as below:

`driver = webdriver.Chrome("../web_drivers/chromedriver.exe")`

and for mac/Lnux:

`driver = webdriver.Chrome("../web_drivers/chromedriver")`

More details to follow
