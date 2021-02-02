from playwright.sync_api import sync_playwright
import time


def run(playwright):
    tick1 = time.time()
    browser = playwright.chromium.launch(
        headless=False, executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")  # 需要指定位置的chrome
    context = browser.new_context(
        # 经纬度 #https://www.opengps.cn/Map/Tools/PickUpGPS_Baidu.aspx
        geolocation={"longitude": 116.343574, "latitude": 39.947036},
        permissions=["geolocation"]
    )

    page = context.new_page()
    page.goto("https://xxcapp.xidian.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fxxcapp.xidian.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex")
    page.click("input[placeholder=\"账号\"]")
    page.fill("input[placeholder=\"账号\"]", "17020199001")  # 账号
    page.click("input[placeholder=\"密码\"]")
    page.fill("input[placeholder=\"密码\"]", "1234567a")  # 密码
    time.sleep(0.3)
    with page.expect_navigation():
        page.click("text=\"登 录\"")
    time.sleep(0.3)
    page.click("//div[normalize-space(.)='否（No）']/span[1]")
    page.click("//div[normalize-space(.)='中国大陆（Mainland of China）']/span[1]/i")

    page.click("(//div[starts-with(normalize-space(.), '所在地点（请打开手机位置功能，并在手机权限设置中选择允许微信访问位置信息）（Detailed location (Please turn on \"Locatio')]/input[normalize-space(@placeholder)='点击获取地理位置' and normalize-space(@type)='text'])[2]")
    time.sleep(0.5)
    page.click("//li[9]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//div[normalize-space(.)='36℃~36.5℃']/span[1]")
    page.click("//li[11]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//li[12]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//li[13]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//li[14]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//div[normalize-space(.)='否']/span[1]/i")
    page.click("//li[16]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("//li[17]/div/div/div[2][normalize-space(.)='否（No）']/span[1]/i")
    page.click("text=\"提交信息(Submit)\"")
    time.sleep(1)
    page.click("text=\"确认\"")
    if time.time() - tick1 > 10:
        page.close()
        context.close()
        browser.close()
    page.click("text=\"确定\"")
    page.close()
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
