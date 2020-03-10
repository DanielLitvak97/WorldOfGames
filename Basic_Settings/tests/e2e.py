from selenium import webdriver
my_driver = webdriver.Chrome(executable_path='C:/dr/chromedriver_win32/chromedriver.exe')


def test_scores_service(application_url):
    my_driver.get(application_url)
    score = my_driver.find_element_by_xpath('//*[@id="score"]').text
    if int(score[1:-1]) in range(1, 1001):
        return True
    return False


def main_function():
    if test_scores_service("http://127.0.0.1:8777"):
        return 0
    return exit(-1)


