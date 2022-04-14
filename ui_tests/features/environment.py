from selenium import webdriver
import time
import os

 
t = time.localtime()     

def before_scenario(context, scenario):
  
  vname = context.scenario.name + str(time.strftime("%H:%M:%S", t))

  if 'web' in context.tags:
      os.system('./../tools/cm selenoid start')
      os.system('./../tools/cm selenoid-ui start')  
      time.sleep(5)
      
      

      capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "acceptInsecureCerts": True,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "videoName": vname + ".mp4", 
            "startMaximized": True
                        }
                            }

      context.browser = webdriver.Remote(
      command_executor="http://localhost:4444/wd/hub",
      desired_capabilities=capabilities)
  
     

 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.browser.quit()
    

def after_all(context):

      time.sleep(5)
      os.system('./../tools/cm selenoid stop')
      os.system('./../tools/cm selenoid-ui stop')
      os.system('cp ~/.aerokube/selenoid/video/*.mp4 ~/Vídeos/')
     

