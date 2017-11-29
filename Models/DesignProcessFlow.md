We describe here both main concepts and high level design steps of the customers' reviews evalution (classification & polarity) system


## **<span style="color:blue">Main Concepts</span>**

The review system will be composed of various models :

**1- Classifaction** : 
* Input : text field
* Output : class category (from a defined set of categories)

**2- Key Fragments Recognition** :
* Input : text field, class category?
* Output : set of words, adjectives and verbs (could be 1, 2 or 3 grams) 

**3- Meaningful chunks Recognition** : 
* Input : text field, class category
* Output : set of features

**4- Polarity** :   
* Input : text field
* Output : polarity (positive, quite positive, neutral, quite negative, negative) 

Models 2 and 3 depend on model 1 ouput (tbc)

## **<span style="color:blue">Example</span>**

Review from amazon :<https://www.amazon.com/Hitachi-RB24EAP-2-Cycle-Powered-Handheld/dp/B003VYC31Q/ref=gbps_tit_s-3_af4e_3100115b?smid=ATVPDKIKX0DER&pf_rd_p=f113943e-1d84-4883-b871-13290264af4e&pf_rd_s=slot-3&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=6FWVKVKW6XJH20J>

~~~~
Lightweight, a little loud, but really throws a huge volume of air! It's much better
performance than the leaf vac/blower combo I replaced. Plus the blower tube stays on the
blower, my old one would always fall off.
I bought this blower in Sept 2011 and got 3 solid summers out of it with no issues at all. 4th
summer was a different story, as I started to experience stalling issues. It would start back up
then stall again. I looked at the fuel lines and found the black tube was starting to perforate
right where it connects to the carb; and the pink / clear looking line from the primer bulb was
disintegrating inside the plastic fuel tank. Looks like ethanol in the fuel was eating away at
these parts.
~~~~

**Class Category** : Garden & Outdoor

**Meaningful chunks Recognition**
* Lightweight
* Little Loud
* Throws huhe volume of air
* Tube stays on the blower
* No issues at all
* Experience stalling issues
* Black tube starting to perforate

**Product Features Recognition** : blower, leaf vac, tube, fuel line, carb, bulb, fuel tank 

**Polarity** : Quite Positive

## **<span style="color:blue">High Level Design</span>**

Classfication and polarity models design will be quite identical. We'll describe them jointly.

Recognition models design will be described separately.

### **Classification and polarity model**

The design of every model will follow below steps :

1- In parrallel : 
* a- Define categories and meaning of each category 
* b- Select training and test datasets 
* c- Experiment & evaluate models, keep a short list

2- Benchmark models (cf. benchmark criteria), select model and build language

3- Train the model (using cross validation)

4- Test the model, evaluate output accuracy; loop to step 3 if needed until accuracy is acceptable (95%) 

5- Deploy the model

### **Product Features Recognition**
This model will be designed as following :

1- For every class category, define an ontology (for i.e. in the form of bag of words)

2- Build a text processing function in order to match text input with corresponding class category ontology
 
### **Meaningful chunks Recognition** 

TBD
