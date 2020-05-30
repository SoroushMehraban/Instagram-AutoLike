# Instagram-AutoLike
Autolike script for instagram
#### Prerequisites:
1. You should install selenium with this following command in terminal:
```
pip install selenium
```
2. You should download ChromeDriver ([Click here](https://chromedriver.chromium.org/downloads)) and place .exe file (in case if you are in using windows) in project folder.
#### How does this script work:
For running this script, you should open terminal, go to your project folder and type this command:
```
python AutoLike.py username password
```
and instead of username and password, give it yours. this script simply open a chrome browser with helps of selenium, login, scroll down and like every post which it sees.</br>
this script scrolls down for 100 times and then refresh the page. if you want to change this feature, you can easily change the value of  SCROLL_TIMES.
