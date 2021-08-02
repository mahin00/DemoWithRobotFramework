*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Dialogs
Library    DateTime
Library    String
Library    BuiltIn
Library    Process
Library    Screenshot
Library    Collections
Library    ../customized_keywords/HeadlessFileDownload.py
Library    ../customized_keywords/Helper.py
Library    ../customized_keywords/MultipleFilesUpload.py
Library    ../customized_keywords/PerformanceTiming.py
Library    ../customized_keywords/RobotEnvironmentSetup.py
Library    ../customized_keywords/UnzipFile.py



# USAGE: Uncomment the line to use and comment out the line that you don't wish to use


# ENVIRONMENT SETTINGS (choose 1)

# Use this when running the functional test
Resource    settings_env_functional.robot

# Use this when running the performance test
#Resource    settings_env_performance.robot

# This is the your own custom local environment settings (make this file on your own, do not push to remote) 
#Resource    settings_env_local.robot


# GLOBAL VARIABLES (choose 1)

# Use this when running the functional test
Resource    ../variables/variables_functional.robot

# Use this when running the performance test on ANZ like medim box or small box
#Resource    ../variables/variables_performance_medium_box.robot

# Use this when running the performance test on lagre environments
#Resource    ../variables/variables_performance_large_box.robot

# This is the your own custom local variables (make this file on your own, do not push to remote)
#Resource    ../variables/variables_local.robot


# FIXED GLOBAL VARIABLES (do not uncomment)

# This file contains all the users and roles that are used by all environments
Resource    ../variables/variables_users_and_roles.robot

# This file contains all the variables that are commonly used by all environments
Resource    ../variables/variables_common.robot
