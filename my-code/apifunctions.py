#%pip install selenium
#%pip install openpyxl
#%pip install xlrd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    # si True, no aperece la ventana (headless=no visible)
opciones.add_argument('--start-maximized')         # comienza maximizado
#opciones.add_argument('user-data-dir=selenium')    # mantiene las cookies
#opciones.add_extension('driver_folder/adblock.crx')       # adblocker
opciones.add_argument('--incognito')


import warnings
warnings.filterwarnings('ignore')

PATH=ChromeDriverManager().install()


def is_scrapping(ticker):

    '''esta funcion nos descarga y convierte a dataframe el income statement de una empresa y devuelve solo los tres últimos años'''
    
    url1="https://www.morningstar.com/stocks/xnas/"
    url2=ticker+"/financials"
    url=url1+url2

    driver=webdriver.Chrome(PATH, options = opciones)
    driver.get(url)

    #pinchamos en "see details"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > div.sal-component-body > div > sal-components-financials-summary > div > div:nth-child(2) > div > div.sal-component-body > div > div > div.sal-summary-section__header.sal-icon-link > a"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    time.sleep(2)

    ruta="/Users/danigomezlechonbarrachina/Downloads/Income Statement_Annual_As Originally Reported.xls"

    inc_statement=pd.read_excel(ruta)
    
    inc_statement=inc_statement[["AMCX_income-statement_Annual_As_Originally_Reported","2018","2019","2020","2021"]]
    
    for i in range(len(inc_statement["AMCX_income-statement_Annual_As_Originally_Reported"])):

        inc_statement["AMCX_income-statement_Annual_As_Originally_Reported"][i]=inc_statement["AMCX_income-statement_Annual_As_Originally_Reported"][i].strip()

    inc_statement.set_index("AMCX_income-statement_Annual_As_Originally_Reported",inplace=True)

    inc_statement.fillna(0,inplace=True)

    return inc_statement


def bs_scrapping(ticker):

    '''esta funcion nos descarga y convierte a dataframe el balance sheet de una empresa  y devuelve solo los tres últimos años'''
    
    url1="https://www.morningstar.com/stocks/xnas/"
    url2=ticker+"/financials"
    url=url1+url2

    driver=webdriver.Chrome(PATH, options = opciones)
    driver.get(url)

    #pinchamos en "see details"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > div.sal-component-body > div > sal-components-financials-summary > div > div:nth-child(2) > div > div.sal-component-body > div > div > div.sal-summary-section__header.sal-icon-link > a"))).click()

    #pinchamos en "see details"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[3]/main/div[2]/div/div/div[1]/div/div/sal-components/section/div/div/div/sal-components-new-financials/div/div[2]/div/div/sal-components-financials-details/div/div/div/div[1]/div[1]/sal-components-segment-band/div/div/div/button[2]"))).click()
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    time.sleep(2)
    
    ruta="/Users/danigomezlechonbarrachina/Downloads/Balance Sheet_Annual_As Originally Reported.xls"

    balance_sheet=pd.read_excel(ruta)
    
    balance_sheet=balance_sheet[["AMCX_balance-sheet_Annual_As_Originally_Reported","2018","2019","2020","2021"]]
    
    for i in range(len(balance_sheet["AMCX_balance-sheet_Annual_As_Originally_Reported"])):

        balance_sheet["AMCX_balance-sheet_Annual_As_Originally_Reported"][i]=balance_sheet["AMCX_balance-sheet_Annual_As_Originally_Reported"][i].strip()

    
    balance_sheet.set_index("AMCX_balance-sheet_Annual_As_Originally_Reported",inplace=True)

    balance_sheet.fillna(0,inplace=True)
    
    return balance_sheet


def cf_scrapping(ticker):

    '''esta funcion nos descarga y convierte a dataframe el cash flow de una empresa y devuelve solo los tres últimos años y rellena los nulos con 0'''
    
    url1="https://www.morningstar.com/stocks/xnas/"
    url2=ticker+"/financials"
    url=url1+url2

    driver=webdriver.Chrome(PATH, options = opciones)
    driver.get(url)

    #pinchamos en "see details"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > div.sal-component-body > div > sal-components-financials-summary > div > div:nth-child(2) > div > div.sal-component-body > div > div > div.sal-summary-section__header.sal-icon-link > a"))).click()

    #pinchamos en "see details"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div[3]/main/div[2]/div/div/div[1]/div/div/sal-components/section/div/div/div/sal-components-new-financials/div/div[2]/div/div/sal-components-financials-details/div/div/div/div[1]/div[1]/sal-components-segment-band/div/div/div/button[3]"))).click()
    
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__layout > div > div.mdc-page-shell.mds-page-shell.default-layout > div.mdc-page-shell__content.mds-page-shell__content > main > div.stock__content > div > div > div.mdc-column.mds-layout-grid__col.stock__content-sal.mds-layout-grid__col--12.mds-layout-grid__col--auto-at-1092 > div > div > sal-components > section > div > div > div > sal-components-new-financials > div > div:nth-child(2) > div > div > sal-components-financials-details > div > div > div > div.sal-component-header > div.sal-financials-details__exportSection > button"))).click()

    time.sleep(2)
    
    ruta="/Users/danigomezlechonbarrachina/Downloads/Cash Flow_Annual_As Originally Reported.xls"

    cash_flow=pd.read_excel(ruta)
    
    cash_flow=cash_flow[["AMCX_cash-flow_Annual_As_Originally_Reported","2018","2019","2020","2021"]]

    for i in range(len(cash_flow["AMCX_cash-flow_Annual_As_Originally_Reported"])):

        cash_flow["AMCX_cash-flow_Annual_As_Originally_Reported"][i]=cash_flow["AMCX_cash-flow_Annual_As_Originally_Reported"][i].strip()
   
    cash_flow.set_index("AMCX_cash-flow_Annual_As_Originally_Reported",inplace=True)

    cash_flow.fillna(0,inplace=True)
    
    return cash_flow


def cleaning_is(income_statement):
    
    '''This function eliminates the extra lines in the income statement so that we are only left with those relevant to the calculations'''
    
    unwanted_index=['Total Revenue', 'Gross Profit','Cost of Revenue', 'Operating Income/Expenses','Depreciation, Amortization and Depletion', 'Total Operating Profit/Loss','Non-Operating Income/Expenses, Total','Total Net Finance Income/Expense', 'Net Interest Income/Expense','Irregular Income/Expenses', 'Pretax Income', 'Net Income from Continuing Operations',
       'Net Income after Extraordinary Items and Discontinued Operations','Net Income after Non-Controlling/Minority Interests',
       'Net Income Available to Common Stockholders',
       'Diluted Net Income Available to Common Stockholders',
       'Income Statement Supplemental Section',
       'Reported Normalized and Operating Income/Expense Supplemental Section',
       'Total Revenue as Reported, Supplemental',
       'Operating Expense as Reported, Supplemental',
       'Total Operating Profit/Loss as Reported, Supplemental',
       'Reported Normalized Income', 'Reported Effective Tax Rate',
       'Reported Normalized Operating Profit', 'Discontinued Operations',
       'Basic EPS', 'Basic EPS from Continuing Operations',
       'Basic EPS from Discontinued Operations', 'Diluted EPS',
       'Diluted EPS from Continuing Operations',
       'Diluted EPS from Discontinued Operations',
       'Basic Weighted Average Shares Outstanding',
       'Diluted Weighted Average Shares Outstanding',
       'Reported Normalized Diluted EPS', 'Basic EPS', 'Diluted EPS',
       'Basic WASO', 'Diluted WASO', 'Fiscal year ends in Dec 31 | USD']
    
    for i in unwanted_index:
        
        if i in income_statement.index:
    
            income_statement=income_statement.drop(i,axis=0)
        
    return income_statement


def cleaning_bs(balance_sheet):
    
    '''This function eliminates the extra lines in the balance sheet so that we are only left with those relevant to the calculations'''
        
    unwanted_index=["Total Current Assets","Cash and Cash Equivalents","Trade/Accounts Receivable, Current","Gross Trade/Accounts Receivable, Current",
    "Allowance/Adjustments for Trade/Accounts Receivable, Current","Amount Due From Related Parties, Current","Deferred Tax Assets, Current","Total Non-Current Assets","Net Property, Plant and Equipment","Properties",
    "Leasehold and Improvements","Machinery, Furniture and Equipment","Furniture, Fixtures and Office Equipment","Leased Property, Plant and Equipment","Other Property, Plant and Equipment","Accumulated Depreciation",
    "Net Intangible Assets","Trademarks and Patents","Licenses and Rights","Customer Relationships","Other Intangible Assets","Gross Goodwill and Other Intangible Assets","Accumulated Amortization of Intangible Assets","Accumulated Amortization of Intangibles other than Goodwill"
    ,"Accumulated Amortization of Trademarks and Patents","Accumulated Amortization of Customer Relationships","Accumulated Amortization of Other Intangible Assets","Trade and Other Receivables, Non-Current","Amount Due from Related Parties, Non-Current","Total Liabilities"
    ,"Total Current Liabilities","Trade/Accounts Payable, Current","Interest Payable, Current","Taxes Payable, Current","Trade Notes Payable, Current"
    ,"Amount Due to Related Parties/Shareholders, Current","Payables and Accrued Expenses, Current","Accrued Expenses, Current","Financial Liabilities, Current"
    ,"Current Debt and Capital Lease Obligation","Current Portion of Long Term Debt and Capital Lease","Provision for Employee Entitlements, Current"
    ,"Deferred Income/Customer Advances/Billings in Excess of Cost, Current","Other Deferred Liabilities, Current","Financial Liabilities, Non-Current"
    ,"Long Term Debt","Notes Payables, Non-Current","Bank/Institutional Loans, Non-Current","Other Loans, Non-Current","Capital Lease Obligations, Non-Current"
    ,"Deferred Tax Liabilities, Non-Current","Total Equity","Equity Attributable to Parent Stockholders","Paid in Capital","Common Stock"
    ,"Preferred Stock","Additional Paid in Capital/Share Premium","Total Non-Current Liabilities"]
            
    for i in unwanted_index:
        
        if i in balance_sheet.index:
    
            balance_sheet=balance_sheet.drop(i,axis=0)
        
    return balance_sheet


def cambio_a_float(dataframe):
    
    '''This function converts the dataframe to float'''
    
    for i in dataframe.columns:
        
        dataframe[i]=dataframe[i].astype(dtype="float64")


def add_columns(dataframes,new_years):

    '''This function adds the new year columns to the dataframes'''
    
    for i in dataframes:
       
        for j in new_years:
            
            i[j]=0
    