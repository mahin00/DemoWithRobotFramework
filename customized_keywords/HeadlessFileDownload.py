from robot.libraries.BuiltIn import BuiltIn

class HeadlessFileDownload(object):
    _download_dir = None

    def enable_download_in_headless_chrome(self, download_dir):
        # add missing support for chrome "send_command"  to selenium webdriver
        self._download_dir = download_dir
        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sl.driver
        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
        command_result = driver.execute("send_command", params)
        print("response from browser:")
        for key in command_result:
            print("result:" + key + ":" + str(command_result[key]))