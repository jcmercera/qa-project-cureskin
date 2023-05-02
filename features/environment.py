from selenium import webdriver
from selenium.webdriver.firefox.service import Service as Firefox_Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from app.application import Application
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger


# def get_options():
#     chrome_options = Options()
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--start-maximized")
#     chrome_options.add_argument("--headless")
#     return chrome_options


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    # # Enable for Chrome
    # context.driver = webdriver.Chrome(executable_path='/Users/JeiM/Documents/Automation/aqa_internship/chromedriver')
    # context.driver = webdriver.Chrome()

    # # Enable for Firefox
    # service = Service('/Users/JeiM/Documents/Automation/aqa_internship/geckodriver')
    # # context.driver = webdriver.Firefox(service=service)
    # #context.driver.set_window_size(2000, 694)

    # # Enable for Safari
    # context.driver = webdriver.Safari()
    # context.browser = webdriver.Safari()


    ## Enable for Chrome HEADLESS ##
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(chrome_options=options, service = Service('/Users/JeiM/Documents/Automation/aqa_internship/chromedriver'))

    ## Enable for Firefox HEADLESS ##
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")

    # context.driver = webdriver.Firefox(
    #     options=options, service=service)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings

    desired_cap = {
        'browserName': 'Firefox',
        'bstack:options': {
            'os': 'Windows',
            'osVersion': '10',
            'sessionName': test_name
        }
    }
    bs_user = 'jcmercera_qM1LKj'
    bs_key = '3VRzGqpPo8Xiz6azyqeY'

    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario)
    logger.info(f'Started scenario:{scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
