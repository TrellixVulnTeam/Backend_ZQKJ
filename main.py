from flask import Flask,jsonify,request,send_file
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 

app = Flask(__name__)

stopwords = set(STOPWORDS)
def mainProcess(inputString):
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(inputString) 

    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.savefig('penv/1.png',bbox_inches='tight')

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message':'Working'})

@app.route('/backend',methods=['POST'])
def wordCloud():
    if request.method=="POST":
        inputString = request.json["data"]
        mainProcess(inputString)
        return send_file('1.PNG')

if __name__ == "__main__":
    app.run(debug=True)