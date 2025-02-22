Before writing the program, I analyzed the website to determine whether it was static or dynamic.
Since the website uses JavaScript to load data dynamically, Scrapy alone would not be effective. Scrapy's spider can only crawl basic static HTML content, and if a website renders content via JavaScript, Scrapy alone cannot extract that data.
To overcome this, I integrated Selenium WebDriver. Selenium loads the dynamic content by opening the webpage in a browser (headless or with UI), ensuring that JavaScript executes and renders the necessary elements.
Selenium WebDriver is used to open the page, allowing JavaScript to render all event details.
Once the page loads completely, all live events become accessible.
There are a total of 48 live events on the page, so I implemented a loop to capture all of them and convert them into JSON format.
Initializes the Selenium WebDriver with Chrome in __init__ Method
for loading the page i gave some time for 5 minutes, after rleative xpath has been written for each name ,location,phonenumber,image url
after that i saved total output in json file

