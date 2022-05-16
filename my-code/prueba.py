#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('store', '-r wacc')
get_ipython().run_line_magic('store', '-r prices')
get_ipython().run_line_magic('store', '-r sales_growth')
get_ipython().run_line_magic('store', '-r parameters_new_t')
get_ipython().run_line_magic('store', '-r companies_to_use')


# In[2]:


import pandas as pd
import numpy as np
from apifunctions import *
import datetime
import matplotlib.pyplot as plt
from scipy import stats

pd.set_option("display.max_rows", None, "display.max_columns", None)


# #### First we select the year and the list of companies for which we want to calculate the dcf_value and distributions

# In[3]:


year="2021"
companies_to_use=companies_to_use


# #### We first get the last year revenue of the companies we are interested in:
# 

# In[4]:


sales_last_year=last_year_rev(companies_to_use,parameters_new_t,year)


# #### We rename the columns in the sales_growth dataset for simplicity

# In[5]:


sales_growth.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021']


# #### We put into a list the growth rate we are going to use for the selected companies

# In[6]:


growth_rate=growth_rate(companies_to_use,sales_growth,year)


# #### We get the parameters we are going to use for the free cash flow calculations
# 

# In[7]:


ebitda_margin,depr_percent,nwc_percent,capex_percent,tax_rate=parameters(companies_to_use,parameters_new_t,year)


# #### We calculate the free cash flows for the list of companies we have

# In[8]:


free_cash_flows=[]
for i in range(len(ebitda_margin)):
    
    free_cash_flows.append(free_cash_flow(growth_rate[i],ebitda_margin[i],depr_percent[i],nwc_percent[i],capex_percent[i],tax_rate[i],sales_last_year[i]))


# #### We calculate the dcf_value for each of the companies:

# In[9]:


wacc.columns = ['2010', '2011', '2012', '2013','2014', '2015', '2016', '2017','2018', '2019', '2020', '2021']


# #### We calculate the terminal value for each of the companies

# In[10]:


dcf_values=[]
for i in range(len(ebitda_margin)):
    
    dcf_values.append(terminal_value(wacc["2021"][i],free_cash_flows[i],growth_rate[i]))


# #### We iterate 10,000 times the values of sales_growth, ebitda_margin and nwc_percent  using a monte_carlo simulation to get the distribution of the price for each company

# In[11]:


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
    


# In[ ]:


mode=[]

for i in output_distribution:
    
    mode.append(max(set(i), key=i.count))
    plt.hist(i, bins = 20)
    plt.show()


# In[ ]:


mode

