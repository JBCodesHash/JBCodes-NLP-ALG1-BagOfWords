#JBCodes
#BagOfWords Example 1
#https://twitter.com/CodesJb
#https://jbcodes.hashnode.dev/

import string

#We define our blurb of text as a string
TextBlurb = "Blue is one of the three primary colours of pigments in painting and traditional colour theory, as well as in the RGB colour model. It lies between violet and green on the spectrum of visible light. The eye perceives blue when observing light with a dominant wavelength between approximately 450 and 495 nanometres. Most blues contain a slight mixture of other colours; azure contains some green, while ultramarine contains some violet. The clear daytime sky and the deep sea appear blue because of an optical effect known as Rayleigh scattering. An optical effect called Tyndall effect explains blue eyes. Distant objects appear more blue because of another optical effect called aerial perspective."\
"Blue has been an important colour in art and decoration since ancient times. The semi-precious stone lapis lazuli was used in ancient Egypt for jewellery and ornament and later, in the Renaissance, to make the pigment ultramarine, the most expensive of all pigments. In the eighth century Chinese artists used cobalt blue to colour fine blue and white porcelain. In the Middle Ages, European artists used it in the windows of cathedrals. Europeans wore clothing coloured with the vegetable dye woad until it was replaced by the finer indigo from America. In the 19th century, synthetic blue dyes and pigments gradually replaced organic dyes and mineral pigments. Dark blue became a common colour for military uniforms and later, in the late 20th century, for business suits. Because blue has commonly been associated with harmony, it was chosen as the colour of the flags of the United Nations and the European Union."\
"Surveys in the US and Europe show that blue is the colour most commonly associated with harmony, faithfulness, confidence, distance, infinity, the imagination, cold, and occasionally with sadness. In US and European public opinion polls it is the most popular colour, chosen by almost half of both men and women as their favourite colour. The same surveys also showed that blue was the colour most associated with the masculine, just ahead of black, and was also the colour most associated with intelligence, knowledge, calm and concentration."

#We also don't care about capitalization.
TextBlurb = TextBlurb.lower()

#Next we define our data structure we intend to use in tokenization,
#I've chosen to use a dictionary but this can be done other ways.
BagOfWords = {}

#Pre-remove all punctuation:
TextBlurb.translate(str.maketrans('', '', string.punctuation))
TextBlurb = TextBlurb.replace(",","")

#We take our blurb, and tokenize it based on Spaces " ".
SplitBlurb = TextBlurb.split(" ")

#Define our stopword array
StopWords = ["i", "me", "my", "myself", "we", "our", "ours",
             "ourselves", "you", "your", "yours", "yourself",
             "yourselves", "he", "him", "his", "himself",
             "she", "her", "hers", "herself", "it", "its",
             "itself", "they", "them", "their", "theirs",
             "themselves", "what","which", "who", "whom",
             "this", "that", "these", "those", "am", "is",
             "are", "was", "were", "be", "been", "being",
             "have", "has", "had", "having", "do", "does",
             "did", "doing", "a", "an", "the", "and", "but",
             "if", "or", "because", "as", "until", "while",
             "of", "at", "by", "for", "with", "about", "against",
             "between", "into", "through", "during", "before",
             "after", "above", "below", "to", "from", "up",
             "down", "in", "out", "on", "off", "over", "under",
             "again", "further", "then", "once", "here", "there",
             "when", "where", "why", "how", "all", "any", "both",
             "each", "few", "more", "most", "other", "some",
             "such", "no", "nor", "not", "only", "own", "same",
             "so", "than", "too", "very", "s", "t", "can", "will",
             "just", "don", "should", "now"]


#Lastly we iterate through the split blurb;
#Using logic: 
#If it isn't in our dictionary, we add it with value 1.
#If it is in our dictionary, we increase the value by 1.

for i in SplitBlurb:
    #Remove stopwords
    if i in StopWords:
        continue
    else:
        #Check if the key is in the dict already
        if  i in BagOfWords:
            BagOfWords[i] = BagOfWords[i] + 1
        #add it w/ value of 1 if not.    
        else:
            BagOfWords[i] = 1
#End For
            
#Sort the dictionary
BagOfWordsList = sorted(BagOfWords.items(), key=lambda x: x[1])

print("Bag Of Words:")
for i in BagOfWords:
    if BagOfWords[i] > 1:
        print(i + " : " + str(BagOfWords[i]) + ", ", end = " ")
x = input()


 
