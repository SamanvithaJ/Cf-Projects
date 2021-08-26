import requests      # To import our news API from which we are going to get news to our app
import tkinter as tk

def getNews():
    api_key = "69098ca7575f42069325e5168a565e07"
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key  
    getNews = requests.get(main_url).json()    # request to extract data and store it in json format
    #print(getNews)
    article = getNews["articles"]   # The result is in json format.We have got status, total results,articles in the output. But we are intersested only on source(rather th article)
    #print(article) 

    news_article=[]          #Even the articles has got many sub layers("author name,like link to the news etc."),but we are interested only in the main headlines
    my_news =""
    for arti in article:
        news_article.append(arti['title'])
        #print(news_article)      #This prints our news in the terminal. So to print it in our window, we config it

  #   for i in range(len(news_article)):     #To display all the top news articles 
    for i in range(10):                #To display the top 10 news articles
        my_news = my_news + str(i+1) + ". " + news_article[i] + "\n"   
        label.config(text= my_news)

fiScreen = tk.Tk()
fiScreen.title("News App")
fiScreen.geometry("1470x600")
# fiScreen.state("zoomed")                  # This will always open our app/window in full screen
button = tk.Button(fiScreen, font =24, text="Refresh the news", command = getNews)
button.pack(pady =20)  # Giving a padding of 20 to the Y- coordinate

label = tk.Label(fiScreen, font =18, justify= "left" )    # We used justify : To get all our text to left
label.pack(pady = 20)

getNews()


fiScreen.mainloop()
