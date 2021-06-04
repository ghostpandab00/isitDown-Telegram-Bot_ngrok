![botimage2](https://user-images.githubusercontent.com/65948438/120762128-95133500-c533-11eb-9218-9bb70da8ad82.png)
# isitDown-Telegram-Bot_ngrok
simple Telegram Bot to check the status of websites as well as IP address. I have integrated python-telegram-bot API in my Python code and used ngrok that allows to expose a web server running on my local machine to the internet. Used webhooks instead of polling for data gathering.

It's done only for testing purpose. 

urllib.request module is used to fetch the URLs and and these requests are passed to urlopen to get the response. The exceptions are then handled by using the urllib.error module. Ping is used to get the response of IP addresses.
