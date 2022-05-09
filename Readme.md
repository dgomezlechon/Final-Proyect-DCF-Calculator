# ETL Project

## Introduction

In this project we are going to Extract, Transform and Load a series of Data. 
The objective of this project will be to gather trading data of several stocks (Apple, Twitter and Microsoft) and to see how their price is affected when they release their earnings as well as to see the impact that beating or underperforming vs estimates has on them. Finally we want to be able to see for big changes in price what the main news on the stock were as of that date.

## Data Sources

- Yahoo Finance (https://es.finance.yahoo.com/):


    - CSV files:
        - apple_price
        - twitter_price
        - microsoft_price
        
        
- Alpha Query (https://www.alphaquery.com/)


- Google (https://www.google.com/)

## Data extraction and transformation

In order to extract the data we have used two different methods. 

On on hand we have downloaded a series of CVS files from yahoo finance to get the daily trading price for the three companies since the start of 2015. In this CVS files we are getting the open and close price as well as the volume.


In second place we have used scrapping (Selenium) to get the quarterly earnings of these companies since 2015 as well as the estimates these companies had for those quarters.
To these three tables we added a column of "Price_change" to see the daily percentage change in price. 


Finally, we used scrapping to automatize the extraction of the first news link in Google for a certain stock in a certain day. To do this we filtered the results in the tables above by % price change and obtained those days were the % change in price was greater than an x amount (as the amount of results varied depending on the company used, I used different % amounts to have comparable results in terms of number of results shown), and then I created a function called "get_news_link" that searched in google for the company ticker i.e TWTR and the date i.e. 04/04/2022 and then copied the link for the first news on the Dataframe events_companyname.

## Outcomes

- Extracción.ipynb
- Transformation.ipynb
- Load.ipynb
- Analizing_data.ipynb
- apifunctions.py

## Database Schema

Finally I created a Database called etlproject where I uploaded the 9 tables created in the steps above and created a 1-to-1 relationship between them.





![Captura%20de%20Pantalla%202022-04-17%20a%20la%28s%29%209.17.00%20p.%C2%A0m..png](attachment:Captura%20de%20Pantalla%202022-04-17%20a%20la%28s%29%209.17.00%20p.%C2%A0m..png)


```python

```
