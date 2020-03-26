# Python Selenium Framework
The aim of this project began with a group of individuals, of different skill levels within Python, to get together and walk through setting up a Python Selenium framework.

# Day 1 

First day we made the simple steps to create a project in PyCharm, add the necessary packages and set up our `setup.py` and `requirements.txt` files.

We threw together a quick `hack_file.py` to get a basics up and running and to ensure everyone's machines where functioning as expected.

## Additional points
* A `web_drivers` folder has been added and the chromedriver (version 80.0.3987.106) has been added into the folder and already referenced in the `hack_file.py` to assist in ease of use:

```python
from selenium import webdriver

driver = webdriver.Chrome("../web_drivers/chromedriver")

driver.get("https://www.bbc.co.uk/")
```

The line `driver = webdriver.Chrome("../web_drivers/chromedriver")` is already referencing the chromedriver held within the `web_drivers` folder so should run out of the box all things being well and that the version of chrome being used aligns with the chromedriver.

