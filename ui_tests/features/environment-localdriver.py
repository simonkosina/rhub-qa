from selenium import webdriver
#import requests
#import wget
#import zipfile
#import os


#def before_all():
   #reserved for test preparation

def before_scenario(context, scenario):


  if 'web' in context.tags:
        
 #__________________Chromedriver automated lattest version aquisition_________________
 #WIP
    # get the latest chrome driver version number
    # url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    # response = requests.get(url)
    # version_number = response.text

    # # build the donwload url
    # download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # # download the zip file using the url built above
    # latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # # extract the zip file
    # with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    #     zip_ref.extractall() # you can specify the destination folder path here
    # # delete the zip file downloaded above
    # os.remove(latest_driver_zip)
#___________________________________________________________________

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    context.browser = webdriver.Chrome(chrome_options=chrome_options,
                               executable_path='../drivers/chromedriver')

    context.browser.implicitly_wait(10)

      
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()


