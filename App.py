from flask import Flask,render_template,request,url_for
from bs4 import BeautifulSoup as BS
import requests
from urllib.request import urlopen as URO
# import pymongo

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/scrap',methods=['POST'])
def index():
    if request.method=='POST':
        search_data=request.form['content'].replace(" ","")
        try:
            # db_conn=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
            # db=db_conn['Scrap_Data']
            # review=db[search_data].find({})
            # if review.count()>0:
            #     return render_template('results.html',reviews=review)
            # else:
            url='https://www.flipkart.com/search?q='+search_data
            url_client=URO(url)
            link=url_client.read()
            url_client.close()
            html_info=BS(link,'html.parser')
            bigbox=html_info.findAll('div',{'class':'_1AtVbE col-12-12'})
            del bigbox[0:3]
            box=bigbox[0]
            product_link='https://www.flipkart.com'+box.div.div.div.a['href']
            link1=requests.get(product_link)
            html_info1=BS(link1.text,'html.parser')
            comments=html_info1.find_all('div',{'class':'_16PBlm'})

                # table=db[search_data]
            review=[]
            for comment in comments:
                try:
                   rating=comment.div.div.div.div.text

                except:
                   rating = 'no rating'
                try:
                   heading=comment.div.div.div.p.text
                except:
                   heading='no Heading'

                try:
                    name=comment.div.div.find_all('p',{'class':'_2sc7ZR _2V5EHH'})[0].text
                except:
                     name='No Name'
                try:
                     comment_tag_=comment.div.div.find_all('div',{'class':''})
                     comment_tag=comment_tag_[0].div.text
                except:
                     comment_tag='no Comment'
                dict1={'Product':search_data,'Rating':rating,'CommentHead':heading,'Name':name,'Comment':comment_tag}
                    # table.insert_one(dict1)
                review.append(dict1)
            return render_template('results.html',reviews=review)
        except:
            return 'Something is wrong'
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,port=8002)