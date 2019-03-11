# Securities_Visualization_in_Python
A Command Line Interface (CLI) Python program to visualize stock market data over a given time frame. 

This is a program myself and two others wrote for our final project in my object-oriented Python programming class. The other two authers
are Jake Susskind (@jakesusskind) and Jeremy Westerwiller. The program uses the Macrotrends API to pull real time stock data in CSV format.
The program graphs the data using the Matplotlib, Pandas, and NumPy libraries. If the user makes a mistake in their input such as formatting the date
wrong or puting days when the market was closed they will see this error:

'Enter a new stock symbol and/or check that you have five dates in YYYY-MM-DD format, and are days the market was open'

Other errors include entering a stock before it was publicly traded, for example a user could not request data for Tesla in 1995.

A screenshot of the SPDR S&P500's (SPY) performance over 5 days in November, 2018.
![stock_vis_ss1](https://user-images.githubusercontent.com/22042867/54096391-07f7ca80-4382-11e9-87f3-9265679c1197.PNG)

A screenshot of GE's (General Electric) stock performance over 5 days in January in 2001.
![stock_vis_ss4_GE_jan](https://user-images.githubusercontent.com/22042867/54096587-e814d680-4382-11e9-8e59-3401691e4831.PNG)

I wanted to see how Amazon (AMZN) in 1997 when it IPO'd.
![stock_vis_ss3](https://user-images.githubusercontent.com/22042867/54096395-0e864200-4382-11e9-92f9-8de381f2c485.PNG)

Instructions:
  1) Navigate in your command line to where the file exists. 
  2) Enter the name of the .py file and the symbol of the stock you want along with 5 dates in the format YYYY-MM-DD with no commas separating
     them.
  3) DISCLAIMER: The Macrotrends API supports up to 50 free data requests through it, so after they it will generate an error. However, a different
     API could be substituted in it's place.
  4) Enter and watch it graph the performance of the security. 
  5) Errors: the program will return this error if you type your instructions incorrectly, so pay attention to your input!
  
  'Enter a new stock symbol and/or check that you have five dates in YYYY-MM-DD format, and are days the market was open'
  
  6) Happy trading!
  
