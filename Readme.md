# DCF Calculator

## Introduction

In this project we are going to create a Discounted Cash Flow calculator. For this we are going to get fundamental data for the mebers of the SPX Index from the Bloomberg API and use it to create discounted cash flow models for the members of the index since 2010.

## Data Sources

- Bloomberg API:


    - CSV files:
        - wacc.xlsx
        - prices.xlsx
        - sales_growth.xlsx
        - market_cap.xlsx
        - shares_outstanding.xlsx
        
        
- Morningstar (https://www.morningstar.com/)




## Data extraction and transformation

In order to extract the data we have used two different methods. 

On first hand we extract the data from the API of Bloomberg and BQL (Bloomberg query language). We also use selenium to extract information from the financial statements for the selected companies.

## Outcomes

- trialst.py
- apifunctions.py
- Data cleaning.ipynb

## App Creation

***Link to app: https://share.streamlit.io/dgomezlechon/final-proyect-dcf-calculator/main/my-code/trialst.py***

Finally I created an app using Streamlit in order to see the data obtained. This app is divided into three sections:

- DCF_value: Here we can filter by the year and select as many companies as we want, in order to see their proyected cash flows as of that year and the DCF value of the company in that moment of time (all yearly data is as of the last working day of the year in the U.S.)

- DCF_evolution: Here we can select an individual company and see how its valuation according to this model has evolved over time. Also we can see the companies market cap evolution and compare both to see whether the company was over or undervalued.

- Investing strategy: 
    
    - Don't rebalance: For this strategy we can select the year (as of last working day) when we decide to invest according to this model, the year when we want to sell our positions and both the quantity invested and the number of companies to be bought. 

The model calcualtes the discounted cash flow value of each company, applies a margin of safety of 30% percent and compares it with the market cap in that point in time. It then invests equally the amount between the x companies which are undervalued the most.

   - Rebalance: For this strategy we can select the same parameters as in the "DOnt rebalance" one. However in this case it assumes all our positions are sold at the end of each year. Then calculates the new companies to buy and buys them reinvesting profits (subtracting taxes of 20%).

