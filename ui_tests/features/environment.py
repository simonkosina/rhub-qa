from selenium import webdriver
import time
#import os

# # def before_all(context):
# #   os.system('./../tools/cm selenoid start')
# #   os.system('./../tools/cm selenoid-ui start')  
# #   time.sleep(5)

def before_scenario(context, scenario):
  t = time.localtime()
  vname = context.scenario.name + str(time.strftime("%H:%M:%S", t))

  if 'web' in context.tags:
      

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
    

#def after_all():
    #actual videos folder .aerokube/selenoid/video 
    #the basic idea is move the reports and the video evidences to a folder or a host that
    #can be managed or latter acceced 
    #the script isn't done by permissions issues.

