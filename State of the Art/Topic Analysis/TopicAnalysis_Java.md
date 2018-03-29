# Topic Analysis in Java
This document references the work done with the library LingPipe around the subject od text classification.

The entire source for the exemple can be found in the src/ directory, it has been taken from the official website of LingPipe.

## The Data
The data used for this tests is a publicly available and well known dataset of 20 newsgroups.

sources can be found [here](http://qwone.com/~jason/20Newsgroups)
 
We will only be working our classification on 4 of the 20 news groups.

## The code
### Training

First, we train up a set of character based language models (one per newsgroup as named in the static array CATEGORIES) that processes data in 6 character sequences as specified by the NGRAM_SIZE constant.

```
private static String[] CATEGORIES
    = { "soc.religion.christian",
        "talk.religion.misc",
        "alt.atheism",
        "misc.forsale" };

private static int NGRAM_SIZE = 6;
```

The actual classifier involves one language model per classifier. In this case, we are going to use process language models. Ling Pipe has a factory method in *DynamicLMClassifier* to construct actual models.

```
DynamicLMClassifier classifier
  = DynamicLMClassifier
    .createNGramBoundary(CATEGORIES,
                         NGRAM_SIZE);
```

Training a classifier simply involves providing examples of text of the various categories. This is called through the handle method after first constructing a classification from the category and a classified object from the classification and text: 
```
Classification classification
    = new Classification(CATEGORIES[i]);
Classified<CharSequence> classified
    = new Classified<CharSequence>(text,classification);
classifier.handle(classified);
```


### Classifiying
The DynamicLMClassifier is pretty slow when doing classification so it is generally worth going through a compile step to produce the more efficient compiled version, which will classify character sequences into joint classification results. A simple way to do that is in the code as: 

```
JointClassifier<CharSequence> compiledClassifier
    = (JointClassifier<CharSequence>)
      AbstractExternalizable.compile(classifier);
```

Now comes in the machine learning:
```
JointClassification jc = compiledClassifier.classifyJoint(text);
String bestCategory = jc.bestCategory();
String details = jc.toString();
```

Which gives us the results as followed:

```
Testing on soc.religion.christian/21417
Best Cat: soc.religion.christian
Rank Cat Score P(Cat|In) log2 P(Cat,In)
0=soc.religion.christian -1.56 0.45 -1.56
1=talk.religion.misc -2.68 0.20 -2.68
2=alt.atheism -2.70 0.20 -2.70
3=misc.forsale -3.25 0.13 -3.25
```


