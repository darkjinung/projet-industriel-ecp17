options(java.parameters = "-Xmx12000m")
require(coreNLP)

initCoreNLP()

catInHat = c("the sun did not shine.", "it was too wet to play.",
             "so we sat in the house all that cold, cold, wet day.")


run_annotators(catInHat, as_strings = TRUE, backend = "coreNLP")


output = annotateString(catInHat)

getDependency(output)

getSentiment(output)