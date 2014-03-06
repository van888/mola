from django import forms
from models import Ticker, Comment, Estimate

class TickerForm(forms.ModelForm):

    class Meta:
        model = Ticker
        fields = ('symbol',
                  'company_name',
                  'exchange_name',
                  'security_type',
                  'sector',
                  'industry',
                  'business_des'
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'body')


