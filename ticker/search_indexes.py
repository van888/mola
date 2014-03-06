import datetime
from haystack import indexes
from ticker.models import Ticker

class TickerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #print text
    company_name = indexes.EdgeNgramField(model_attr='company_name')
    business_des = indexes.CharField(model_attr='business_des')

    content_auto = indexes.NgramField(model_attr='symbol')

    def get_model(self):
        return Ticker

    def index_queryset(self, using=None):
        ### USED WHEN THE ENTIRE INDEX FOR MODEL IS UPDATED. ###
        return self.get_model().objects.all()





__author__ = 'vantran'
