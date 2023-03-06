# CloudFlare Captcha Bypass Using Selenium and undetected_chromedriver

This script demonstrates how to bypass CloudFlare Captchas using Selenium and undetected_chromedriver. 

'I have used brave browser here and we have same driver for brave and chrome . '

## Why Brave uses chromedriver for Selenium?

Brave is a privacy-focused web browser that is based on the open-source Chromium project. This means that it shares many of the same underlying components and functionality as Google Chrome. One of those components is the ChromeDriver, which is a standalone executable that allows Selenium to control the Chrome browser.

Because Brave is built on the Chromium project, it also implements the Chrome DevTools Protocol, which is the same protocol that the Chrome browser uses to communicate with its renderer process. This means that Brave can be controlled using the ChromeDriver, just like Chrome.

Therefore, if you want to use Selenium with Brave, you can simply use the same ChromeDriver that you would use with Chrome. This makes it easy to write automated tests or scripts that work with both browsers.

## Requirements

- Python 3.6+
- Pipenv
- Selenium
- undetected_chromedriver

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/subash1237/CloudFlare_Captcha_bypass_selenium.git

2. Change into the project directory:


cd your-repository


3. Install the required packages using `pipenv`:


pipenv install


4. Activate the virtual environment:

pipenv shell



5. Install `undetected_chromedriver`:

pip install undetected-chromedriver


## Usage

1. Run the script:


python main.py



2. Follow the instructions on the screen to enter the URL of the website you want to visit and to complete any required captchas.

3. Once the script has completed, you will see the HTML content of the website in your terminal.

## Contributing

Contributions are welcome! Please create a pull request with your proposed changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


