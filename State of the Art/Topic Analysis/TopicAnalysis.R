library(topicmodels)
library(dplyr)
library(tm)
setwd('C:/Users/benhamza/AppData/Local/NoBackup/Perso/CentraleSupelec/Projet Industriel/projet-industriel-ecp17/State of the Art/Topic Analysis')

reviews.data <- read.csv("./consumer-reviews-of-amazon-products/7817_1.csv")
reviews.init <- select(reviews.data,c(1,20))
reviews.init$row_id <- row.names(reviews.init)


### Text Pre-Proessing ###
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


### Corpus to Matrix ###
reviews_DTM <- DocumentTermMatrix(reviews_corpus)
#remove sparse terms
#reviews_DTM <- removeSparseTerms(reviews_DTM , 0.9) 
#remove lines with zero lines
#reviews_DTM <- reviews_DTM[rowSums(as.matrix(reviews_DTM[,-1])) != 0,]
#find freq terms
findFreqTerms(reviews_DTM, 1000)

### Run Latent Dirichlet Allocation (LDA) using Gibbs Sampling
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

terms(ldaOut,6)
