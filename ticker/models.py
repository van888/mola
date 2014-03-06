from django.db import models
from django.utils import timezone

class Ticker(models.Model):
    symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    exchange_name = models.CharField(max_length=50)
    security_type = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    business_des = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.symbol, self.company_name)

    class Meta:
        ordering = ('symbol','company_name')

    def get_absolute_url(self):
        return "/finance/%s/" % self.symbol

class Performance(models.Model): #1 PK and 29 fields
    ticker = models.OneToOneField(Ticker, primary_key=True)
    absolute_returns_1month = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_1month = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_1month = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_3month = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_3month = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_3month = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_6month = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_6month = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_6month = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_12month = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_12month = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_12month = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_ytd = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_ytd = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_ytd = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_3yr = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_3yr = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_3yr = models.FloatField(default=None, blank=True,null=True)

    absolute_returns_5yr = models.FloatField(default=None, blank=True,null=True)
    rel_to_ind_returns_5yr = models.FloatField(default=None, blank=True,null=True)
    rel_to_mkt_returns_5yr = models.FloatField(default=None, blank=True,null=True)

    def __unicode__(self):
        return self.ticker.symbol

class Indicator(models.Model):
    ticker = models.OneToOneField(Ticker, primary_key=True)
    tech_RSI = models.IntegerField(default=None, blank=True,null=True)
    tech_bollinger = models.IntegerField(default=None, blank=True,null=True)
    tech_stochastic = models.IntegerField(default=None, blank=True,null=True)
    tech_MACD = models.IntegerField(default=None, blank=True,null=True)
    tech_composite = models.IntegerField(default=None, blank=True,null=True)
    #sentiment_crowd = models.IntegerField(blank=True,null=True)
    #sentiment_trader = models.IntegerField(blank=True,null=True)
    sentiment_PCVOLUME = models.IntegerField(default=None, blank=True,null=True)
    sentiment_PCOI = models.IntegerField(default=None, blank=True,null=True)
    sentiment_liquidity = models.IntegerField(default=None, blank=True,null=True)
    sentiment_socNetwork = models.IntegerField(default=None, blank=True,null=True)
    sentiment_composite = models.IntegerField(default=None, blank=True,null=True)

    #place_holder = models.IntegerField(default=None, blank=True,null=True)
    #place_holder = models.IntegerField(default=None, blank=True,null=True)
    liquidity_level = models.CharField(default=None, blank=True, null=True,max_length=50)
    quant_value = models.IntegerField(default=None, blank=True,null=True)
    quant_growth = models.IntegerField(default=None, blank=True,null=True)
    quant_profit = models.IntegerField(default=None, blank=True,null=True)
    quant_management = models.IntegerField(default=None, blank=True,null=True)
    quant_composite = models.IntegerField(default=None, blank=True,null=True)

    def __unicode__(self):
        return self.ticker

class Ratio(models.Model):
    ticker = models.OneToOneField(Ticker, primary_key=True)
    # Valuation
    PE_Current = models.FloatField(default=None, blank=True,null=True)
    PE_Ratio_extra_items = models.FloatField(default=None, blank=True,null=True)
    PE_Ratio_no_extra_items = models.FloatField(default=None, blank=True,null=True)
    PSales_Ratio = models.FloatField(default=None, blank=True,null=True)
    PBook_Ratio = models.FloatField(default=None, blank=True,null=True)
    PCashFlow_Ratio = models.FloatField(default=None, blank=True,null=True)
    EV_to_EBITDA = models.FloatField(default=None, blank=True,null=True)          #new
    EV_to_Sales = models.FloatField(default=None, blank=True,null=True)
    Total_Debt_to_EV = models.FloatField(default=None, blank=True,null=True)
    #Efficiency
    Rev_per_Employee = models.FloatField(default=None, blank=True,null=True)      #new
    Inc_per_Employee = models.FloatField(default=None, blank=True,null=True)      #new
    Receivables_Turnover = models.FloatField(default=None, blank=True,null=True)
    Total_Asset_Turnover = models.FloatField(default=None, blank=True,null=True)
    #Liquidity
    Current_Ratio = models.FloatField(default=None, blank=True,null=True)
    Quick_Ratio = models.FloatField(default=None, blank=True,null=True)
    Cash_Ratio = models.FloatField(default=None, blank=True,null=True)
    #Profitability
    Gross_Margin = models.FloatField(default=None, blank=True,null=True)
    Operating_Margin = models.FloatField(default=None, blank=True,null=True)
    Pretax_Margin = models.FloatField(default=None, blank=True,null=True)
    Net_Margin = models.FloatField(default=None, blank=True,null=True)
    #Management Effectiveness
    Return_on_Assets = models.FloatField(default=None, blank=True,null=True)
    Return_on_Equity = models.FloatField(default=None, blank=True,null=True)
    Return_on_Total_Capital = models.FloatField(default=None, blank=True,null=True)
    Return_on_Invested_Capital = models.FloatField(default=None, blank=True,null=True)
    #Capital_Structure
    Total_Debt_to_Total_Equity = models.FloatField(default=None, blank=True,null=True)
    Total_Debt_to_Total_Capital = models.FloatField(default=None, blank=True,null=True)
    Total_Debt_to_Total_Assets = models.FloatField(default=None, blank=True,null=True)
    LongTerm_Debt_to_Equity = models.FloatField(default=None, blank=True,null=True)
    LongTerm_Debt_to_Total_Capital = models.FloatField(default=None, blank=True,null=True)

    def __unicode__(self):
        return self.ticker.symbol


class Estimate(models.Model):
    ticker = models.OneToOneField(Ticker, primary_key=True)
    #Estimates_Series1
    Average_Recommendation = models.CharField(default=None, blank=True,null=True,max_length=10)
    Number_of_Ratings   = models.IntegerField(default=None, blank=True,null=True)
    FY_Report_Date  = models.DateField(default=None, blank=True,null=True)
    Last_Quarters_Earnings = models.FloatField(default=None, blank=True,null=True)
    Year_Ago_Earnings = models.FloatField(default=None, blank=True,null=True)
    #Estimates_Series2
    Average_Target_Price = models.FloatField(default=None, blank=True,null=True)
    Current_Quarter_Estimate = models.FloatField(default=None, blank=True,null=True)
    Current_Year_Estimate = models.FloatField(default=None, blank=True,null=True)
    Median_PE_on_CY_Estimate = models.FloatField(default=None, blank=True,null=True)
    Next_Fiscal_Year_Estimate = models.FloatField(default=None, blank=True,null=True)
    Median_PE_on_Next_FY_Estimate = models.FloatField(default=None, blank=True,null=True)
    #Recommendations
    buy_present = models.IntegerField(default=None, blank=True,null=True)
    hold_present = models.IntegerField(default=None, blank=True,null=True)
    sell_present = models.IntegerField(default=None, blank=True,null=True)
    Consensus_present = models.CharField(default=None, blank=True,null=True,max_length=10)
    buy_1_month_ago = models.IntegerField(default=None, blank=True,null=True)
    hold_1_month_ago = models.IntegerField(default=None, blank=True,null=True)
    sell_1_month_ago = models.IntegerField(default=None, blank=True,null=True)
    Consensus_1_month_ago = models.CharField(default=None, blank=True,null=True,max_length=10)
    buy_3_month_ago = models.IntegerField(default=None, blank=True,null=True)
    hold_3_month_ago = models.IntegerField(default=None, blank=True,null=True)
    sell_3_month_ago = models.IntegerField(default=None, blank=True,null=True)
    Consensus_3_month_ago = models.CharField(default=None, blank=True,null=True,max_length=10)

    def __unicode__(self):
        return self.ticker.symbol

class Supplement_ticker_info(models.Model):
    ticker = models.OneToOneField(Ticker, primary_key=True)
    thumbnail = None
    company_website = None

    def __unicode__(self):
        return self.ticker.symbol

class Comment(models.Model):
    user = models.CharField(max_length=50)
    body = models.TextField()
    pub_date = models.DateTimeField('date_published')
    likes = models.IntegerField(default=0)
    ticker = models.ForeignKey(Ticker)

    def __unicode__(self):
        return self.ticker.symbol

    class Meta:
        ordering = ['-likes','-pub_date']



class ReportScreen(models.Model):
    tickers = models.ManyToManyField(Ticker)
    title = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField('date_published')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)


