# WSB-Scraper
Uses Praw to Scrape /r/wallstreetbets and keeps track of recently mentioned and trending stocks. It then posts the information as an embed to a discord channel

![WSB-Post](Firelink/firelink.gif)





Learned how to use the python reddit api wrapper (praw) and discord library to create a bot. 

The bot scrapes the last 25 posts from top, rising, hot, and new and keeps track of mentions for each NASDAQ stock. The top 10 stocks mentioned and trending (based on hourly, daily, and weekly reports) are then posted to an investment discord. 

The script is automatically ran every hour using cron jobs. 
