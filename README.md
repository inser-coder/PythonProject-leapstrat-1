The python script is bascially made of scrapy with selenuim.
i tried to write the programe scrapy with spider 
Going before the writing the programe i check how the website structure is it dynamic or static.
when i check website is dynamic it no longer where i can use scrapy with spider beacuse spider will crwal only on 
basic static html content if the website is desgined with javascript and to load the data if it render with same spider will not help.
beacuse of that i need to load the dynamic content, for loading dynamic content i need to get the selenuim webdriver into picture so ,i used the webdriver for that 
once webdriver open the page in head or headles browser automatically java script also will be rendered.
In page there total 48 events are live so i used a loop to grab the all events and convert into json .

