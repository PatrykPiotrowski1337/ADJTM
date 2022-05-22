import nltk

from WordCloudVisualizer import visual as wordcloud
from Classification import visual as classification

nltk.download('stopwords')
nltk.download('punkt')



wordcloud()
classification()