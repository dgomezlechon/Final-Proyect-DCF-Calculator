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
    
    inc_statement=inc_statement[["AMCX_income-statement_Annual_As_Originally_Reported","2019","2020","2021"]]
    
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
    
    balance_sheet=balance_sheet[["AMCX_balance-sheet_Annual_As_Originally_Reported","2019","2020","2021"]]
    
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
    
    cash_flow=cash_flow[["AMCX_cash-flow_Annual_As_Originally_Reported","2019","2020","2021"]]
    
    cash_flow.set_index("AMCX_cash-flow_Annual_As_Originally_Reported",inplace=True)

    cash_flow.fillna(0,inplace=True)
    
    return cash_flow
