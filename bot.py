import os
import urllib.parse
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# The code snippet `DOWNLOAD_FOLDER = "downloads"` defines a variable `DOWNLOAD_FOLDER` with the value
# "downloads", which represents the name of the folder where downloaded files will be saved.
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# The code snippet you provided is setting up options for the Chrome WebDriver in Selenium.
# The line `options.add_argument(r'--user-data-dir=C:\Users\Username\AppData\Local\Google\Chrome\User
# Data\Default')` in the provided code snippet is setting the user data directory for the Chrome
# WebDriver in Selenium.

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(r'--user-data-dir=C:\Users\Username\AppData\Local\Google\Chrome\User Data\Default') # Get Your Profile Path in chrome://version/ paste in chrome 
options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(options=options)
driver.get("https://discord.com/channels/@me") # Change this link to your channel discord, make sure add the midjouney_bot to your channel
print("✅ Successfull login into Discord!")

def get_filename_from_url(url):
    parsed_url = urllib.parse.urlparse(url)
    return os.path.basename(parsed_url.path)

def download_image_with_curl(image_url):
    try:
        filename = os.path.join(DOWNLOAD_FOLDER, get_filename_from_url(image_url))
        curl_command = f'curl -L "{image_url}" --output "{filename}"'
        os.system(curl_command)
        print(f"✅ Image successfully downloaded: {filename}")
    except Exception as e:
        print(f"❌ Error downloading image: {e}")

def get_upscaled_image_url():
    try:
        latest_message = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((
                By.XPATH, "(//li[contains(@class, 'messageListItem')]//*[contains(text(), 'Zoom Out')]/ancestor::li)[last()]"
            ))
        )
        original_link = latest_message.find_element(By.XPATH, ".//a[contains(@class, 'originalLink_af017a')]")
        return original_link.get_attribute("href")
    except Exception:
        return None

def send_prompt(prompt):
    try:
        print(f"📝 Sending prompt: {prompt}")
        chat_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        chat_box.click()
        time.sleep(1)
        chat_box.send_keys("/imagine")
        time.sleep(1)
        chat_box.send_keys(Keys.TAB)
        time.sleep(1)
        chat_box.send_keys(f" {prompt}")
        time.sleep(1)
        chat_box.send_keys(Keys.RETURN)
        print(f"✅ Prompt has been sent: {prompt}")
    except Exception as e:
        print(f"❌ Failed to typing prompt: {e}")

def wait_for_midjourney_reply(prompt, upscale=False):
    print(f"⏳ Waiting for a reply to the prompt: {prompt}")
    for _ in range(60):
        try:
            messages = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.XPATH, "//li[contains(@class, 'messageListItem')]")
            ))
            for msg in messages:
                text = msg.text.lower()
                if prompt.lower() in text:
                    if upscale and "u1" in text:
                        print("✅ Reply found for upscale!")
                        return msg
                    elif not upscale and "v1" in text:
                        print("✅ Reply found for varian!")
                        return msg
        except Exception:
            pass
        time.sleep(5)
    print("❌ Did not find a reply from MidJourney!")
    return None

def wait_for_u_buttons():
    print("⏳ Waiting status message upscale")
    for _ in range(60): 
        try:
            latest_message = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located(
                    (By.XPATH, "(//li[contains(@class, 'messageListItem') and .//button[contains(., 'U1')]])[last()]")
                )
            )
            print("✅ Upscale buttons found!")
            return latest_message
        except Exception:
            pass
        time.sleep(5)
    print("❌ Upscale buttons not found!")
    return None

def click_u_buttons_sequentially():
    latest_message = wait_for_u_buttons()
    if not latest_message:
        return
    
    
    try:
        for i in range(1, 5):
            button = latest_message.find_element(By.XPATH, f".//button[contains(., 'U{i}')]")
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button))
            driver.execute_script("arguments[0].click();", button)
            print(f"✅ Upscaling images {i}")
            
            time.sleep(10) 
            image_url = get_upscaled_image_url()
            if image_url:
                print(f"🔗 URL Images not found: {image_url}")
                download_image_with_curl(image_url)
            else:
                print("❌ Did not find the URL of the upscaled image!")
            time.sleep(5) 
    except Exception as e:
        print(f"❌ Unable to find upscaling button! {e}")

# The code snippet you provided is reading prompts from a file named "prompts.txt" and then performing
# a series of actions for each prompt read from the file.
with open("prompts.txt", "r", encoding="utf-8") as file:
    prompts = [line.strip() for line in file if line.strip()]

for prompt in prompts:
    send_prompt(prompt)
    message = wait_for_midjourney_reply(prompt)
    if message:
        time.sleep(5)
        click_u_buttons_sequentially()
    time.sleep(10)

driver.quit()
