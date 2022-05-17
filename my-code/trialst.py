#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from apifunctions import *
#import matplotlib.pyplot as plt
import streamlit as st

pd.set_option("display.max_rows", None, "display.max_columns", None)


# In[2]:


wacc=pd.read_csv("data/wacc.csv",index_col = 'ID')
prices=pd.read_csv("data/prices.csv")
sales_growth=pd.read_csv("data/sales_growth.csv", index_col = 'ID')
parameters_new_t=pd.read_csv("data/parameters_new_t.csv")
companies_to_use=pd.read_csv("data/companies_to_use.csv")
market_cap=pd.read_csv("data/market_cap.csv",index_col = 'ID')
shares_outstanding=pd.read_csv("data/shares_outstanding.csv",index_col = 'ID')


# In[3]:


companies_available=companies_to_use['0'].values.tolist()

genre = st.sidebar.radio(
     "What would you like to see?",
     ('DCF_value', 'DCF_evolution', 'Investing Strategy'))

if genre == 'DCF_value':
     st.write('Your selected: DCF_value.')

     #### We add layout to streamlit

     st.title("DCF_Value Calcualtor")
     st.subheader("This app calculates the DCF value of a company")


     #### First we select the year and the list of companies for which we want to calculate the dcf_value and distributions

     # In[4]:
     ## we input the year and companies we want to get the data for

     year_select = st.selectbox(
         'For which year would you like to see the dcf_value?',
         ('2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020','2021'))
     st.write('You selected:', year_select)

     comps_select = st.multiselect(
         'Which companies would you like to select:',
         companies_available)
        
     companies_to_use=comps_select
     year=year_select
     #companies_to_use=['J UN Equity','BR UN Equity']


     # #### We first get the last year revenue of the companies we are interested in:


     # In[5]:


     sales_last_year=last_year_rev(companies_to_use,parameters_new_t,year)


     # #### We rename the columns in the sales_growth dataset for simplicity

     sales_growth.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021']
     # #### We put into a list the growth rate we are going to use for the selected companies

     growth_rate=growth_rate(companies_to_use,sales_growth,year)

     # #### We get the parameters we are going to use for the free cash flow calculations
    
     ebitda_margin,depr_percent,nwc_percent,capex_percent,tax_rate=parameters(companies_to_use,parameters_new_t,year)

 
     # #### We calculate the free cash flows for the list of companies we have

     # In[9]:
 

     free_cash_flows=[]
     for i in range(len(ebitda_margin)):
        
         free_cash_flows.append(free_cash_flow(growth_rate[i],ebitda_margin[i],depr_percent[i],nwc_percent[i],capex_percent[i],tax_rate[i],sales_last_year[i],year))



     # #### We calculate the dcf_value for each of the companies:

     # In[10]:


     wacc.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021']


     # #### We calculate the terminal value for each of the companies

     dcf_values=[]
     for i in range(len(ebitda_margin)):
        
         dcf_values.append(terminal_value(wacc[year][i],free_cash_flows[i],growth_rate[i]))


     # #### We iterate 10,000 times the values of sales_growth, ebitda_margin and nwc_percent  using a monte_carlo simulation to get the distribution of the price for each company

     # In[12]:


     output_distribution=[]

     for j in range(len(companies_to_use)):

        
         growth_rate_f=growth_rate[j]
         ebitda_margin_f=ebitda_margin[j]
         depr_percent_f=depr_percent[j]
         nwc_percent_f=nwc_percent[j]
         capex_percent_f=capex_percent[j]
         tax_rate_f=tax_rate[j]
         sales_last_year_f=sales_last_year[j]
         wacc_f=wacc[year][companies_to_use[j]]
         free_cash_flows_f=free_cash_flows[j]

         output_distribution.append(run_mcs(growth_rate_f,ebitda_margin_f,depr_percent_f,nwc_percent_f,capex_percent_f,tax_rate_f,sales_last_year_f,wacc_f,free_cash_flows_f))
        


     # In[13]:


     mode=[]

     for i in output_distribution:
        
         mode.append(max(set(i), key=i.count))
         #plt.hist(i, bins = 20)
         #plt.show()

     #### we get a bar chart with the free cash flows for the selected companies

     for i in range(len(free_cash_flows)):
        
         data=pd.DataFrame(free_cash_flows[i])
         data.rename(columns={0: "Free Cash Flow"}, inplace=True)
        
         st.subheader(companies_to_use[i])
         # we print the values of the variables being used:
         col1, col2, col3,col4 = st.columns(4)
         col1.metric("Growth Rate", "{}%".format(round(growth_rate[i]*100,2)))
         col2.metric("Perpetuity Growth Rate", "{}%".format(round((growth_rate[i]/5)*100,2)))
         col4.metric("DCF_Value", "{}M".format(f'{round(mode[i]/1000000):,}'))
         col3.metric("WACC","{}%".format(round(wacc[year][companies_to_use[i]]*100,2)))

         #we print the chart
         #st.write(data)
         st.bar_chart(data)



#### We add the different tab selection:

elif genre == 'DCF_evolution':
     st.sidebar.write('Your selected: DCF_evolution.')

     #### We add layout to streamlit

     st.title("DCF Historical Evolution")
     st.subheader("This tab allows you to see the historical evolution of the dcf_value for a selected company")

     company = st.selectbox('Which company would you like to select:',
         companies_available)
     companies_to_use=company

     # añadimos slider para seleccionar los años para los que queremos el gráfico:
     from  datetime import time

     time_frame = st.slider(
     "Select time period:",
     2010,2021,(2010,2021))
     st.write("Selected years:", time_frame)
     
     years=[]
     a=time_frame[0]
     while time_frame[1] not in years:
        years.append(a)
        a=a+1

        #### we transform the years into strings:
     for i in years:
            years[years.index(i)]=str(i)

        ####we do a function to get the yearly parameters of selected company
     sales_growth.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021']  
     wacc.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021'] 
     
     yearly_sales_growth,yearly_sales,yearly_ebitda,yearly_depr_prct,yearly_nwc_percent,yearly_capex_percent,yearly_tax_rate=yearly_parameters(years,company,sales_growth,parameters_new_t)

     fcf_list=[]
     for i in range(len(years)):

         fcf_list.append(free_cash_flow(yearly_sales_growth[i],yearly_ebitda[i],yearly_depr_prct[i],yearly_nwc_percent[i],yearly_capex_percent[i],yearly_tax_rate[i],yearly_sales[i],years[i]))

     terminal_values=[]
     for i in range(len(years)):
        
         terminal_values.append(terminal_value(wacc[years[i]][company],fcf_list[i],yearly_sales_growth[i]))

     #from scipy import stats
     output_distributions=[]
     for i in range(len(years)):

         output_distributions.append(run_mcs(yearly_sales_growth[i],yearly_ebitda[i],yearly_depr_prct[i],yearly_nwc_percent[i],yearly_capex_percent[i],yearly_tax_rate[i],yearly_sales[i],wacc[years[i]][company],fcf_list[i]))

     mode=[]

     st.subheader(company)
     for i in output_distributions:
        
         mode.append(float(max(set(i), key=i.count)))

     to_draw=market_cap[market_cap.index==company].transpose()
     to_draw=to_draw[company].astype(dtype="float64")*1000000

     st.bar_chart(mode)
     st.bar_chart(to_draw)

     to_draw["DCF_Value"]=mode
     
     st.bar_chart(to_draw)

     








elif genre == 'Investing Strategy':
     st.sidebar.write('Your selected:Investing Strategy')
    

