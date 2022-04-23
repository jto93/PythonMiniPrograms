#RSS Feed Generator 
import feedparser
import datetime
from tkinter.filedialog import askdirectory
import shutil

def defHTML(i):
    x = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<link rel="icon" type="image/png" href="img/Cool-icon.png" />\n<title>%s</title>\n<!-- Link to Normalize, a package that normalizes CSS across browsers-->\n<link rel="stylesheet"href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css">\n<!-- Link to font-awesome-->\n<link rel="stylesheet"href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" />\n<!-- FONTS-->\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css?family=Source+Code+Pro:400,900 | Source+Sans+Pro:300,900&display=swap" rel="stylesheet"/>\n<link rel="stylesheet" href="css/style.css">\n</head>\n<body>\n' %(i)
    return(x)

def rssFeed(): 
    defPath = 'C:/Users/j_t_o/Desktop/RSSFeeds/'
    orgCSSPath = 'C:/Users/j_t_o/Desktop/Python Projects/Text_Projects/rssFeed/css/style.css'

    if defPath == '': 
        defPath = askdirectory()

    defCSSPath = defPath + 'css/style.css'
    #Refresh CSS from default CSS path in directory
    shutil.copyfile(orgCSSPath, defCSSPath)

    urlLib = {'MLB':"https://www.mlb.com/feeds/news/rss.xml?_gl=1*1wot1ap*_gcl_dc*R0NMLjE2NDk5NDkzMDAuMDQwMjFhYzI4ZDFlMWQwZTllYzc3ODlhYjc3MWUwNzk.",
    'MiLB':'http://www.milb.com/partnerxml/gen/news/rss/milb.xml'
    }
    d = datetime.date.today()
    

    for x in urlLib: 
        feed = feedparser.parse(urlLib[x])

        try: 
            if feed.status == 200: 
                
                path = "%s/%s_%s.html" %(defPath,x,d)
                with open(path, "w", encoding="utf-8") as f:
                    htmlHead = defHTML(x)
                    f.write(htmlHead)
                    pageTitle = "<h1>%s News - %s</h1><br>" %(x,d)
                    f.write(pageTitle)
                    for entry in feed.entries:
                        title = "<a href=%s><h2 class='title'><b>%s</b></h2></a><br>" %(entry.link,entry.title)
                        author = "<h3 class='author'><b>Author</b>: %s</h3><br>" %(entry.author)
                        f.write(title)
                        f.write(author)    
                    f.write('</body>\n</html>')
                    f.close()   
                
        except: 
            print('Something has gone wrong.')
            

    #Feed and Entries
  

rssFeed()