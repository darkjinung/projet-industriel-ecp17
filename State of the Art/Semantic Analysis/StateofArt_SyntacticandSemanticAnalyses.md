# Syntactic and Semantic Analyses

## Problematic

To represent the meaning of a sentence we need a precise method because words have multiple meanings so the solution is the use of formal languages.

There is varied types of knowledge relevant to natural language understanding:

**Syntactic knowledge**: how sequences of words form correct sentences. Knowledge of the rules of grammar.

**Semantic knowledge**: how words have "meaning"; how words have reference (denotation) and associated concepts (connotations)

**Pragmatic knowledge**: "how sentences are used in different situations and how their use affects the interpretation of the sentence," this involves the intentions and context of the conversation.

**Discourse knowledge**: how preceding sentences determine the meaning of a sentence, such as in the case of the referent of a pronoun.

**World knowledge**: general knowledge about, for example, other users beliefs and goals in a conversation.

## General Process

Starting with a sentence in natural language , the result of syntactic analysis will yield a syntatic representation ( often displayed in a tree diagram),
the result of that representation will yield to the logical form of the sentence, logical form is used to capture semantic meaning and depict this eaning independent of any such context,
then we need a general knowledge representation which allows a contextual interpretaiton of the context free form analysis and logical form

Some process that help to understand efficiently a sentence:

**Interpretation process**: maps natural language sentence to the formal language
**Parser**: maps  natural language to their suntactic stucture on representation and their logical form ( uses the rules of gammar and word meanings )
**Contextual interpretation** : maps the logical form to its final knowledge representation

To accomplish the semantic and syntactic analysis , there will be common elements in any such parser :

1. There'll be a grammar ( the legal ways for combining the units - syntactically and semantically ) to result in other constituents,
2. The processor will have an algorithm using the rules of the grammar
3. an orcle , a mechanism of resolving ambiguities

## What is a *good grammar* 

A good grammar have to be:

	* General : the range of sentence the grammar analyzes correctly
	* Selective : the range of non sentence it identifies as problematic 
	* Understandable : the simplicity of the grammer
 
The context-free grammar consists of rules that apply independent of the context
 
One way for context-free grammar is the list notation

> Exemple: Izanami write the readme
> 
>		(S		(NP		(Name	Izanami))
>				(VP		(V		write)
>						(NP		(NP		(ART	the)
>								(N		readme)))))
 
 
## What is a parser ?
A parsing technique is the mehode of analyzing a sentence to determine its structure, in accordance with grammar it may adopt a top-down or bottom-up strategy

Type of parser:

	1. noise-disposal : scans a sentence looking for selected words, which are in its defined vocabulary. During the process any words not in the range of those the computer is looking for are considered "noise" and rejected; the problem with that type of parser is that the user may intented something different from the action accomplished.
		Exemple : the user wants to "Sort the 10 first files" ; the computer will take the action "Sort" as the main action without any condition and will sort all the files.
	2. state-machine : have the caracteristic of changing the state each time, by reading the first word then predict the possibilities for the next word, the next word will be limited to what is grammaticaly correct. The state machine need two databases, one containing a vocabulary of words and their types, and the second containing the current state of the sentence being parsed, that last database will bring the "backtrack" feature. The problem with that type of parser is that it include many word ( fit into more than one category ) and their lexical categorization
	3. Definite Clause Grammer (DCG): top-down recursive analysis most likely depth-first
	
> For more information : https://boomtrain.com/understanding-semantic-analysis/
 http://www.mind.ilstu.edu/curriculum/protothinker/natural_language_processing.php