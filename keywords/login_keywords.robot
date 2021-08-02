*** Settings ***
Resource          ../settings/common_settings.robot

*** Keywords ***
Open Application
    [Arguments]    ${browser_alias}=None
    Run Keyword If    ${DOCKER}==False    Run Keywords    Open browser    ${URL}    ${BROWSER}    ${browser_alias}
    ...    AND    Set Window Size    1800    1400
    Run Keyword If    ${DOCKER}==True    Run Keywords    Chrome_Setup    ${browser_alias}
    ...    AND    Go To    ${URL}
    Set Selenium Speed    ${SELENIUM_SPEED}

Open Alex
    [Arguments]    ${user_name}    ${browser_alias}=None
    Open Application    ${browser_alias}
    Login    ${user_name}

Chrome_Setup
    [Arguments]    ${browser_alias}=None
    [Documentation]    DO NOT REMOVE - Google Chrome for Robotframework in Docker
    ${browser_options} =    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${browser_options}    add_argument    --headless
    Call Method    ${browser_options}    add_argument    --no-sandbox
    Call Method    ${browser_options}    add_argument    --disable-gpu
    Call Method    ${browser_options}    add_argument    --window-size\=1800,1400
    Call Method    ${browser_options}    add_argument    --disable-dev-shm-usage
    Create Webdriver    Chrome    chrome_options=${browser_options}    alias=${browser_alias}

Login
    [Arguments]    ${current_user_email}    ${current_password}=${PASSWORD}
    [Documentation]    This method will login the website
    Input Email       ${current_user_email}
    Input Password    ${current_password}
    Continue
    Welcome Page Should Be Open
    Sleep    ${SHORT_DELAY}

Log Out
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Go To    ${daraz_logout}

Close Application
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Close All Browsers

Input Email
    [Arguments]    ${useremail}
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Input Text       ${Login_User_Email_Field}         ${useremail}

Continue
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Button    ${Submit_Button}

Input Password
    [Arguments]    ${password}
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Input Text    ${Login_User_Pass_Field}    ${password}

Submit Credentials
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Click Button    ${Submit_Button}

Login Page Should Be Open
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Page Should Contain Element    xpath=//div[@class="mod-login"]

Welcome Page Should Be Open
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Page Should Contain Element    xpath=//span[@id='myAccountTrigger']
    # Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Location Should Be    ${HOME} #This can't use becasue the Home URL is dynamic
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Title Should Be    ${Manage_Account_title}


Verify Invalid Login Message
    [Arguments]    ${message}
    Wait Until Keyword Succeeds    ${RETRY_INT_OP}    ${SHORT_DELAY}    Page Should Contain Element    //div[contains(text(),"${message}")]
