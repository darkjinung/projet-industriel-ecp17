Goal here is to highlight how topic analysis can be done in R, via LDA (Latent Dirichlet Allocation) algorithm.

Following links were helpful

<http://davidmeza1.github.io/2015/07/20/topic-modeling-in-R.html>

<https://rpubs.com/chrisbail/nlp_and_topic_models>

<http://tidytextmining.com/topicmodeling.html>

**The dataset "Consumer review on Amazon products"** originated from Kaggle <https://www.kaggle.com/datafiniti/consumer-reviews-of-amazon-products/data>

**Step1 : Importing necessary libraries and setting working directory**

``` r
library(topicmodels)
library(dplyr)
library(tm)
setwd('C:/Users/benhamza/AppData/Local/NoBackup/Perso/CentraleSupelec/Projet Industriel/projet-industriel-ecp17/State of the Art/Topic Analysis')
```

**Step 2.1 : Getting data into a dataframe**

``` r
reviews.data <- read.csv2("./consumer-reviews-of-amazon-products/7817_1.csv",sep=",")
```

**Data Dimenstion**

``` r
dim(reviews.data)
```

*results*

    ## [1] 1597   27

**Column names**

``` r
names(reviews.data)
```

*results*

    ##  [1] "id"                   "asins"                "brand"               
    ##  [4] "categories"           "colors"               "dateAdded"           
    ##  [7] "dateUpdated"          "dimension"            "ean"                 
    ## [10] "keys"                 "manufacturer"         "manufacturerNumber"  
    ## [13] "name"                 "prices"               "reviews.date"        
    ## [16] "reviews.doRecommend"  "reviews.numHelpful"   "reviews.rating"      
    ## [19] "reviews.sourceURLs"   "reviews.text"         "reviews.title"       
    ## [22] "reviews.userCity"     "reviews.userProvince" "reviews.username"    
    ## [25] "sizes"                "upc"                  "weight"

**Step 2.2 : Extracting useful information Id and Text**

``` r
reviews.data <- read.csv2("./consumer-reviews-of-amazon-products/7817_1.csv",sep=",")
reviews.init <- select(reviews.data,c(1,20))
reviews.init$row_id <- row.names(reviews.init)
dim(reviews.init)
```

*results*:

    ## [1] 1597    3

**Step 3 : Creating Corpus & Pre-Proessing Text**

``` r
#compose the corpus
reviews_corpus <- Corpus(VectorSource(as.vector(reviews.init$reviews.text))) 
#remove punctation
reviews_corpus <- tm_map(reviews_corpus, content_transformer(removePunctuation))
#remove numbers
reviews_corpus <- tm_map(reviews_corpus, content_transformer(removeNumbers))
#lowering texts
reviews_corpus <- tm_map(reviews_corpus, content_transformer(tolower))
#remove whitespace
reviews_corpus <- tm_map(reviews_corpus , content_transformer(stripWhitespace))
#remmove stop words
stoplist <- read.csv("stop-word-list.csv", header=FALSE, stringsAsFactors = FALSE)
stoplist<-stoplist$V1
reviews_corpus  <- tm_map(reviews_corpus , content_transformer(removeWords), stoplist)
#stemming
#reviews_corpus  <- tm_map(reviews_corpus , content_transformer(stemDocument), language = "english")
```

**Step 4 : Corpus to Matrix**

``` r
reviews_DTM <- DocumentTermMatrix(reviews_corpus)
#remove sparse terms
#reviews_DTM <- removeSparseTerms(reviews_DTM , 0.9) 
#remove lines with zero lines
reviews_DTM <- reviews_DTM[rowSums(as.matrix(reviews_DTM[,-1])) != 0,]
#find freq terms
findFreqTerms(reviews_DTM, 1000)
```

*results*:

    ## [1] "amazon" "more"   "kindle" "like"

**Step5 : Runing LDA training using Gibbs Sampling Method**

``` r
#set burn in
burnin <-1000
#set iterations
iter<-500
#thin the spaces between samples
thin <- 500
#set random starts at 5
nstart <-5
#use random integers as seed 
seed <- list(254672,109,122887,145629037,2)
# return the highest probability as the result
best <-TRUE
#set number of topics 
k <-7
#run the LDA model
ldaOut <- LDA(reviews_DTM,k, method="Gibbs", control=
                list(nstart=nstart, seed = seed, best=best, burnin = burnin, iter = iter, thin=thin))
```

**Frequent terms per topic**

``` r
terms(ldaOut,6)
```

*results*:

    ##      Topic 1   Topic 2      Topic 3      Topic 4    Topic 5      Topic 6 
    ## [1,] "love"    "ive"        "great"      "use"      "like"       "kindle"
    ## [2,] "echo"    "sound"      "screen"     "more"     "headphones" "ipad"  
    ## [3,] "tap"     "dont"       "want"       "roku"     "just"       "tablet"
    ## [4,] "alexa"   "more"       "tablet"     "like"     "nice"       "hdx"   
    ## [5,] "speaker" "headphones" "paperwhite" "content"  "dont"       "device"
    ## [6,] "just"    "people"     "new"        "features" "really"     "years" 
    ##      Topic 7    
    ## [1,] "prime"    
    ## [2,] "amazon"   
    ## [3,] "device"   
    ## [4,] "movies"   
    ## [5,] "hdx"      
    ## [6,] "available"

**CONCLUSION** LDA is a convenient method to cluster into topics, a set of documents. In our case above, we choosed to classify into 7 clusters and we run the training once.

In usage, getting the right fit "Documents vs Topics" will require more trainings adapting every time LDA inputs including the fitting method (either Gibbs or VEM currently)
