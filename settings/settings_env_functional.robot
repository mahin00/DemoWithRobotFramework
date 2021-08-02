*** Variables ***

${URL}                                      https://member.daraz.com.bd/user/login
${HomePage}                                 https://www.daraz.com.bd/
# Can be either headlesschrome or Chrome (set to Chrome if you would like to see "live" test,
# need to also change DOCKER to False, but be warned, the browser will keep self-focusing)
# Compulsory to test with headlesschrome and on docker before introducing changes to master
# Options:
# - headlesschrome (default)
# - Chrome (set to this to see "live" test)
${BROWSER}                                Chrome

# We use docker to keep versioning of the libraries used during robot testing consistent across different
# user environments (change this where you see fit)
# Options:
# - True (default, use this when running robot from a container)
# - False (when using BROWSER=Chrome)
${DOCKER}                                 False

# Remember to change this to fit your local environment
${USEREMAIL}                               ta1.qups@protonmail.com

# Remember to change this to fit your local environment
${PASSWORD}                               asdfgh#123

# This is the default password on a new instance
${DEFAULT_ADMIN_PASSWORD}                 asdfgh#123

#This is the Invalid password to check some of the test cases
${Invalid_Password}                       asdfghjklqwertyu#12


# Retry Intervals
${SETUP_STEP_SPEED}                       0.01s
${SELENIUM_SPEED}                         1s
${EXTENDED_SYNC_DELAY}                    10seconds
${DELAY}                                  5seconds
${SHORT_DELAY}                            1seconds     # interval length time to wait before next retry
${RETRY_INTERVAL_MAP_VIEW}                6seconds     # DONT TOUCH THIS IF YOU DON'T KNOW WHAT IT DOES
${RETRY_INTERVAL_TABLE_VIEW}              4seconds     # DONT TOUCH THIS IF YOU DON'T KNOW WHAT IT DOES
${TYPING_IN_TEXTFIELD_SPEED}              3s           # DO NOT EVER CHANGE

# Total Retry Times
${RETRY_INT_LOGIN}                        10seconds
${RETRY_INT_OP}                           16seconds
${RETRY_INT_COUNT}                        5x
${RETRY_TOTAL_MAP_VIEW}                   60seconds    # DONT TOUCH THIS IF YOU DON'T KNOW WHAT IT DOES
${RETRY_TOTAL_TABLE_VIEW}                 30seconds    # DONT TOUCH THIS IF YOU DON'T KNOW WHAT IT DOES

${IMPORT_DELAY}                           40s
${IMPORT_JOB_REFRESH_RETRIES}             10

${DOWNLOAD_LOCATION}                      /Users/daraz/Downloads   # the download location of files when running robot (NOTE: downloaded files on headlesschrome does not work as intended)
