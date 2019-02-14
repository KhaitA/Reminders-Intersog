from bs4 import BeautifulSoup
import requests

# сoздаю конструктор, чтобы пройти авторизацию "Google"
# проверяла на "Gmail" с легкостью попадаю на страницу входящих сообщений
# действую аналогично с "Inbox by Gmail"б но авторизация не проходит 

form_data={'Email': 'a.shxxxxxxxxx@gmail.com', 'Passwd': 'Xxx111111'}
post = "https://accounts.google.com/signin/challenge/sl/password"

with requests.Session() as s:
    soup = BeautifulSoup(s.get("https://inbox.google.com").text, features="lxml")
    for inp in soup.select("#gaia_loginform input[name]"):
        if inp["name"] not in form_data:
            form_data[inp["name"]] = inp["value"]
    s.post(post, form_data)
    html = s.get("https://inbox.google.com/reminders?pli=1").content
    print(html)
    
    
# создаю Scrape constructor, однако дальше продвинуться не получается из-за неавторизованности
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())

div = soup.find('div')
#print(div.prettify())
reminders = div.find("div", class_= "tE")

    
