# coding: utf-8
import pandas as pd
from nltk import pos_tag
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import sys

stop_word = "a’s,able,about,above,according,accordingly,across,actually,after,afterwards,again,against,ain’t,all,allow,allows,almost,alone,along,already,also,although,always,am,among,amongst,an,and,another,any,anybody,anyhow,anyone,anything,anyway,anyways,anywhere,apart,appear,appreciate,appropriate,are,aren’t,around,as,aside,ask,asking,associated,at,available,away,awfully,be,became,because,become,becomes,becoming,been,before,beforehand,behind,being,believe,below,beside,besides,best,better,between,beyond,both,brief,but,by,c’mon,c’s,came,can,can’t,cannot,cant,cause,causes,certain,certainly,changes,clearly,co,com,come,comes,concerning,consequently,consider,considering,contain,containing,contains,corresponding,could,couldn’t,course,currently,definitely,described,despite,did,didn’t,different,do,does,doesn’t,doing,don’t,done,down,downwards,during,each,edu,eg,eight,either,else,elsewhere,enough,entirely,especially,et,etc,even,ever,every,everybody,everyone,everything,everywhere,ex,exactly,example,except,far,few,fifth,first,five,followed,following,follows,for,former,formerly,forth,four,from,further,furthermore,get,gets,getting,given,gives,go,goes,going,gone,got,gotten,greetings,had,hadn’t,happens,hardly,has,hasn’t,have,haven’t,having,he,he’s,hello,help,hence,her,here,here’s,hereafter,hereby,herein,hereupon,hers,herself,hi,him,himself,his,hither,hopefully,how,howbeit,however,i’d,i’ll,i’m,i’ve,ie,if,ignored,immediate,in,inasmuch,inc,indeed,indicate,indicated,indicates,inner,insofar,instead,into,inward,is,isn’t,it,it’d,it’ll,it’s,its,itself,just,keep,keeps,kept,know,knows,known,last,lately,later,latter,latterly,least,less,lest,let,let’s,like,liked,likely,little,look,looking,looks,ltd,mainly,many,may,maybe,me,mean,meanwhile,merely,might,more,moreover,most,mostly,much,must,my,myself,name,namely,nd,near,nearly,necessary,need,needs,neither,never,nevertheless,new,next,nine,no,nobody,non,none,noone,nor,normally,not,nothing,novel,now,nowhere,obviously,of,off,often,oh,ok,okay,old,on,once,one,ones,only,onto,or,other,others,otherwise,ought,our,ours,ourselves,out,outside,over,overall,own,particular,particularly,per,perhaps,placed,please,plus,possible,presumably,probably,provides,que,quite,qv,rather,rd,re,really,reasonably,regarding,regardless,regards,relatively,respectively,right,said,same,saw,say,saying,says,second,secondly,see,seeing,seem,seemed,seeming,seems,seen,self,selves,sensible,sent,serious,seriously,seven,several,shall,she,should,shouldn’t,since,six,so,some,somebody,somehow,someone,something,sometime,sometimes,somewhat,somewhere,soon,sorry,specified,specify,specifying,still,sub,such,sup,sure,t’s,take,taken,tell,tends,th,than,thank,thanks,thanx,that,that’s,thats,the,their,theirs,them,themselves,then,thence,there,there’s,thereafter,thereby,therefore,therein,theres,thereupon,these,they,they’d,they’ll,they’re,they’ve,think,third,this,thorough,thoroughly,those,though,three,through,throughout,thru,thus,to,together,too,took,toward,towards,tried,tries,truly,try,trying,twice,two,un,under,unfortunately,unless,unlikely,until,unto,up,upon,us,use,used,useful,uses,using,usually,value,various,very,via,viz,vs,want,wants,was,wasn’t,way,we,we’d,we’ll,we’re,we’ve,welcome,well,went,were,weren’t,what,what’s,whatever,when,whence,whenever,where,where’s,whereafter,whereas,whereby,wherein,whereupon,wherever,whether,which,while,whither,who,who’s,whoever,whole,whom,whose,why,will,willing,wish,with,within,without,won’t,wonder,would,would,wouldn’t,yes,yet,you,you’d,you’ll,you’re,you’ve,your,yours,yourself,yourselves,zero".decode(
    'utf-8')
st = stop_word.split(",")

def isNoun(str):
    if pos_tag([str], lang='eng')[0][1] in "NN":
        return True
    else:
        return False

def main(arg1):
    #Read the parametre of the categorie wanted
    categorie = arg1

    reader=pd.read_csv('C:\Users\ee\Desktop\DataSet\DataSet\categories_train_big.csv',
                       sep=',',
                       usecols=[0,2],
                       header=None)

    reader.columns = ['categorie','review']
    filterCategorie = reader.query('categorie=='+str(categorie))
    del reader


    count_vect = CountVectorizer(lowercase=True,stop_words=st,dtype=np.uint16)
    tmp = [x for x in filterCategorie["review"].tolist() if pd.notnull(x)]
    del filterCategorie
    X_count = count_vect.fit_transform(tmp)
    del tmp
    sumFrenquence = X_count.sum(axis=0).tolist()[0]
    del X_count

    vocab = count_vect.get_feature_names()
    vocab = np.array(vocab)

    bags_word_dict = dict(zip(vocab, sumFrenquence))
    del vocab
    del sumFrenquence
    bags_word_df= pd.DataFrame.from_dict(bags_word_dict,orient='index')
    bags_word_df.columns =['frequency']
    list_not_meanfull = [x.encode('UTF8') for x in bags_word_df.index.values if not isNoun(x)]
    bags_word_df_meanfull = bags_word_df.drop(list_not_meanfull)
    bags_word_df_sorted_meanfull = bags_word_df_meanfull.sort_values('frequency',ascending=False,kind='quicksort')
    bags_word_df_sorted_meanfull_mini = bags_word_df_sorted_meanfull[bags_word_df_sorted_meanfull.frequency > 100]
    path = 'C:/Users/ee/Desktop/DataSet/DataSet/'+str(categorie)+'Categorie.csv'
    bags_word_df_sorted_meanfull_mini.to_csv(path, header=None, index=True, sep=',', mode='a')

if __name__=='__main__':
    sys.exit(main(sys.argv[1]))