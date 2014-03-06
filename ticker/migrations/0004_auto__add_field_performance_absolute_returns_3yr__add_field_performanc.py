# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Performance.absolute_returns_3yr'
        db.add_column(u'ticker_performance', 'absolute_returns_3yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Performance.rel_to_ind_returns_3yr'
        db.add_column(u'ticker_performance', 'rel_to_ind_returns_3yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Performance.rel_to_mkt_returns_3yr'
        db.add_column(u'ticker_performance', 'rel_to_mkt_returns_3yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Performance.absolute_returns_5yr'
        db.add_column(u'ticker_performance', 'absolute_returns_5yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Performance.rel_to_ind_returns_5yr'
        db.add_column(u'ticker_performance', 'rel_to_ind_returns_5yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Performance.rel_to_mkt_returns_5yr'
        db.add_column(u'ticker_performance', 'rel_to_mkt_returns_5yr',
                      self.gf('django.db.models.fields.FloatField')(default=None, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Performance.absolute_returns_3yr'
        db.delete_column(u'ticker_performance', 'absolute_returns_3yr')

        # Deleting field 'Performance.rel_to_ind_returns_3yr'
        db.delete_column(u'ticker_performance', 'rel_to_ind_returns_3yr')

        # Deleting field 'Performance.rel_to_mkt_returns_3yr'
        db.delete_column(u'ticker_performance', 'rel_to_mkt_returns_3yr')

        # Deleting field 'Performance.absolute_returns_5yr'
        db.delete_column(u'ticker_performance', 'absolute_returns_5yr')

        # Deleting field 'Performance.rel_to_ind_returns_5yr'
        db.delete_column(u'ticker_performance', 'rel_to_ind_returns_5yr')

        # Deleting field 'Performance.rel_to_mkt_returns_5yr'
        db.delete_column(u'ticker_performance', 'rel_to_mkt_returns_5yr')


    models = {
        u'ticker.comment': {
            'Meta': {'ordering': "['-likes', '-pub_date']", 'object_name': 'Comment'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'ticker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.Ticker']"}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ticker.estimate': {
            'Average_Recommendation': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'Average_Target_Price': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Consensus_1_month_ago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'Consensus_3_month_ago': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'Consensus_present': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'Current_Quarter_Estimate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Current_Year_Estimate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'FY_Report_Date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Last_Quarters_Earnings': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Median_PE_on_CY_Estimate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Median_PE_on_Next_FY_Estimate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Estimate'},
            'Next_Fiscal_Year_Estimate': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Number_of_Ratings': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Year_Ago_Earnings': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'buy_1_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'buy_3_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'buy_present': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hold_1_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hold_3_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hold_present': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sell_1_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sell_3_month_ago': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sell_present': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'liquidity_level': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'quant_composite': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quant_growth': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quant_management': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quant_profit': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'quant_value': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sentiment_PCOI': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sentiment_PCVOLUME': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sentiment_composite': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sentiment_liquidity': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sentiment_socNetwork': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tech_MACD': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tech_RSI': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tech_bollinger': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tech_composite': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'tech_stochastic': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.performance': {
            'Meta': {'object_name': 'Performance'},
            'absolute_returns_12month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_1month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_3month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_3yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_5yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_6month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'absolute_returns_ytd': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_12month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_1month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_3month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_3yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_5yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_6month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_ind_returns_ytd': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_12month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_1month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_3month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_3yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_5yr': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_6month': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'rel_to_mkt_returns_ytd': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.ratio': {
            'Cash_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Current_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'EV_to_EBITDA': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'EV_to_Sales': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Gross_Margin': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Inc_per_Employee': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'LongTerm_Debt_to_Equity': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'LongTerm_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Ratio'},
            'Net_Margin': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Operating_Margin': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PBook_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PCashFlow_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PE_Current': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PE_Ratio_extra_items': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PE_Ratio_no_extra_items': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'PSales_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Pretax_Margin': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Quick_Ratio': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Receivables_Turnover': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Return_on_Assets': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Return_on_Equity': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Return_on_Invested_Capital': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Return_on_Total_Capital': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Rev_per_Employee': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Total_Asset_Turnover': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Total_Debt_to_EV': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Total_Debt_to_Total_Assets': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Total_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'Total_Debt_to_Total_Equity': ('django.db.models.fields.FloatField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.reportscreen': {
            'Meta': {'ordering': "('title',)", 'object_name': 'ReportScreen'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'tickers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ticker.Ticker']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ticker.supplement_ticker_info': {
            'Meta': {'object_name': 'Supplement_ticker_info'},
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.ticker': {
            'Meta': {'ordering': "('symbol', 'company_name')", 'object_name': 'Ticker'},
            'business_des': ('django.db.models.fields.TextField', [], {}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'exchange_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sector': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'security_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['ticker']