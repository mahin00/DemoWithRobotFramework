# Common variables used in all environments (non-environment specific)
*** Variables ***

# Common directories and paths
${Login_User_Email_Field}         xpath=//body/div[2]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/input[1]
${Login_User_Pass_Field}          xpath=//input[@type="password"]
${Submit_Button}                  xpath=//button[@type="submit"]
${daraz_logout}                   https://member.daraz.com.bd/user/logout
${logo}                           //body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]
${AboutUS}                        xpath=//a[contains(text(),'About Daraz')]
${CareerPage}                     xpath=//a[contains(text(),'Careers')]
${AmarDaraz}                      xpath=//a[contains(text(),'Amar Daraz')]
${XP_SEARCH_BUTTON}               xpath=//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/div[1]/div[2]/button[1]
${SearchField}                    xpath=//input[@id='q']