# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ticker'
        db.create_table(u'ticker_ticker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('exchange_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('security_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sector', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('business_des', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ticker', ['Ticker'])

        # Adding model 'Performance'
        db.create_table(u'ticker_performance', (
            ('ticker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ticker.Ticker'], unique=True, primary_key=True)),
            ('absolute_returns_1month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_ind_returns_1month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_mkt_returns_1month', self.gf('django.db.models.fields.FloatField')()),
            ('absolute_returns_3month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_ind_returns_3month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_mkt_returns_3month', self.gf('django.db.models.fields.FloatField')()),
            ('absolute_returns_6month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_ind_returns_6month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_mkt_returns_6month', self.gf('django.db.models.fields.FloatField')()),
            ('absolute_returns_12month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_ind_returns_12month', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_mkt_returns_12month', self.gf('django.db.models.fields.FloatField')()),
            ('absolute_returns_ytd', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_ind_returns_ytd', self.gf('django.db.models.fields.FloatField')()),
            ('rel_to_mkt_returns_ytd', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'ticker', ['Performance'])

        # Adding model 'Indicator'
        db.create_table(u'ticker_indicator', (
            ('ticker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ticker.Ticker'], unique=True, primary_key=True)),
            ('tech_RSI', self.gf('django.db.models.fields.IntegerField')()),
            ('tech_bollinger', self.gf('django.db.models.fields.IntegerField')()),
            ('tech_stochastic', self.gf('django.db.models.fields.IntegerField')()),
            ('tech_MACD', self.gf('django.db.models.fields.IntegerField')()),
            ('tech_composite', self.gf('django.db.models.fields.IntegerField')()),
            ('sentiment_PCVOLUME', self.gf('django.db.models.fields.IntegerField')()),
            ('sentiment_PCOI', self.gf('django.db.models.fields.IntegerField')()),
            ('sentiment_liquidity', self.gf('django.db.models.fields.IntegerField')()),
            ('sentiment_socNetwork', self.gf('django.db.models.fields.IntegerField')()),
            ('sentiment_composite', self.gf('django.db.models.fields.IntegerField')()),
            ('liquidity_level', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('quant_value', self.gf('django.db.models.fields.IntegerField')()),
            ('quant_growth', self.gf('django.db.models.fields.IntegerField')()),
            ('quant_profit', self.gf('django.db.models.fields.IntegerField')()),
            ('quant_management', self.gf('django.db.models.fields.IntegerField')()),
            ('quant_composite', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ticker', ['Indicator'])

        # Adding model 'Ratio'
        db.create_table(u'ticker_ratio', (
            ('ticker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ticker.Ticker'], unique=True, primary_key=True)),
            ('PE_Current', self.gf('django.db.models.fields.FloatField')()),
            ('PE_Ratio_extra_items', self.gf('django.db.models.fields.FloatField')()),
            ('PE_Ratio_no_extra_items', self.gf('django.db.models.fields.FloatField')()),
            ('PSales_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('PBook_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('PCashFlow_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('EV_to_EBITDA', self.gf('django.db.models.fields.FloatField')()),
            ('EV_to_Sales', self.gf('django.db.models.fields.FloatField')()),
            ('Total_Debt_to_EV', self.gf('django.db.models.fields.FloatField')()),
            ('Rev_per_Employee', self.gf('django.db.models.fields.FloatField')()),
            ('Inc_per_Employee', self.gf('django.db.models.fields.FloatField')()),
            ('Receivables_Turnover', self.gf('django.db.models.fields.FloatField')()),
            ('Total_Asset_Turnover', self.gf('django.db.models.fields.FloatField')()),
            ('Current_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('Quick_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('Cash_Ratio', self.gf('django.db.models.fields.FloatField')()),
            ('Gross_Margin', self.gf('django.db.models.fields.FloatField')()),
            ('Operating_Margin', self.gf('django.db.models.fields.FloatField')()),
            ('Pretax_Margin', self.gf('django.db.models.fields.FloatField')()),
            ('Net_Margin', self.gf('django.db.models.fields.FloatField')()),
            ('Return_on_Assets', self.gf('django.db.models.fields.FloatField')()),
            ('Return_on_Equity', self.gf('django.db.models.fields.FloatField')()),
            ('Return_on_Total_Capital', self.gf('django.db.models.fields.FloatField')()),
            ('Return_on_Invested_Capital', self.gf('django.db.models.fields.FloatField')()),
            ('Total_Debt_to_Total_Equity', self.gf('django.db.models.fields.FloatField')()),
            ('Total_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')()),
            ('Total_Debt_to_Total_Assets', self.gf('django.db.models.fields.FloatField')()),
            ('LongTerm_Debt_to_Equity', self.gf('django.db.models.fields.FloatField')()),
            ('LongTerm_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'ticker', ['Ratio'])

        # Adding model 'Estimate'
        db.create_table(u'ticker_estimate', (
            ('ticker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ticker.Ticker'], unique=True, primary_key=True)),
            ('Average_Recommendation', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Number_of_Ratings', self.gf('django.db.models.fields.IntegerField')()),
            ('FY_Report_Date', self.gf('django.db.models.fields.DateField')()),
            ('Last_Quarters_Earnings', self.gf('django.db.models.fields.FloatField')()),
            ('Year_Ago_Earnings', self.gf('django.db.models.fields.FloatField')()),
            ('Average_Target_Price', self.gf('django.db.models.fields.FloatField')()),
            ('Current_Quarter_Estimate', self.gf('django.db.models.fields.FloatField')()),
            ('Current_Year_Estimate', self.gf('django.db.models.fields.FloatField')()),
            ('Median_PE_on_CY_Estimate', self.gf('django.db.models.fields.FloatField')()),
            ('Next_Fiscal_Year_Estimate', self.gf('django.db.models.fields.FloatField')()),
            ('Median_PE_on_Next_FY_Estimate', self.gf('django.db.models.fields.FloatField')()),
            ('buy_present', self.gf('django.db.models.fields.IntegerField')()),
            ('hold_present', self.gf('django.db.models.fields.IntegerField')()),
            ('sell_present', self.gf('django.db.models.fields.IntegerField')()),
            ('Consensus_present', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('buy_1_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('hold_1_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('sell_1_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('Consensus_1_month_ago', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('buy_3_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('hold_3_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('sell_3_month_ago', self.gf('django.db.models.fields.IntegerField')()),
            ('Consensus_3_month_ago', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'ticker', ['Estimate'])

        # Adding model 'Supplement_ticker_info'
        db.create_table(u'ticker_supplement_ticker_info', (
            ('ticker', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ticker.Ticker'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'ticker', ['Supplement_ticker_info'])

        # Adding model 'Comment'
        db.create_table(u'ticker_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('likes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ticker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticker.Ticker'])),
        ))
        db.send_create_signal(u'ticker', ['Comment'])

        # Adding model 'ReportScreen'
        db.create_table(u'ticker_reportscreen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'ticker', ['ReportScreen'])

        # Adding M2M table for field tickers on 'ReportScreen'
        m2m_table_name = db.shorten_name(u'ticker_reportscreen_tickers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reportscreen', models.ForeignKey(orm[u'ticker.reportscreen'], null=False)),
            ('ticker', models.ForeignKey(orm[u'ticker.ticker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['reportscreen_id', 'ticker_id'])


    def backwards(self, orm):
        # Deleting model 'Ticker'
        db.delete_table(u'ticker_ticker')

        # Deleting model 'Performance'
        db.delete_table(u'ticker_performance')

        # Deleting model 'Indicator'
        db.delete_table(u'ticker_indicator')

        # Deleting model 'Ratio'
        db.delete_table(u'ticker_ratio')

        # Deleting model 'Estimate'
        db.delete_table(u'ticker_estimate')

        # Deleting model 'Supplement_ticker_info'
        db.delete_table(u'ticker_supplement_ticker_info')

        # Deleting model 'Comment'
        db.delete_table(u'ticker_comment')

        # Deleting model 'ReportScreen'
        db.delete_table(u'ticker_reportscreen')

        # Removing M2M table for field tickers on 'ReportScreen'
        db.delete_table(db.shorten_name(u'ticker_reportscreen_tickers'))


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
            'Average_Recommendation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Average_Target_Price': ('django.db.models.fields.FloatField', [], {}),
            'Consensus_1_month_ago': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Consensus_3_month_ago': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Consensus_present': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Current_Quarter_Estimate': ('django.db.models.fields.FloatField', [], {}),
            'Current_Year_Estimate': ('django.db.models.fields.FloatField', [], {}),
            'FY_Report_Date': ('django.db.models.fields.DateField', [], {}),
            'Last_Quarters_Earnings': ('django.db.models.fields.FloatField', [], {}),
            'Median_PE_on_CY_Estimate': ('django.db.models.fields.FloatField', [], {}),
            'Median_PE_on_Next_FY_Estimate': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'Estimate'},
            'Next_Fiscal_Year_Estimate': ('django.db.models.fields.FloatField', [], {}),
            'Number_of_Ratings': ('django.db.models.fields.IntegerField', [], {}),
            'Year_Ago_Earnings': ('django.db.models.fields.FloatField', [], {}),
            'buy_1_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'buy_3_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'buy_present': ('django.db.models.fields.IntegerField', [], {}),
            'hold_1_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'hold_3_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'hold_present': ('django.db.models.fields.IntegerField', [], {}),
            'sell_1_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'sell_3_month_ago': ('django.db.models.fields.IntegerField', [], {}),
            'sell_present': ('django.db.models.fields.IntegerField', [], {}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'liquidity_level': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quant_composite': ('django.db.models.fields.IntegerField', [], {}),
            'quant_growth': ('django.db.models.fields.IntegerField', [], {}),
            'quant_management': ('django.db.models.fields.IntegerField', [], {}),
            'quant_profit': ('django.db.models.fields.IntegerField', [], {}),
            'quant_value': ('django.db.models.fields.IntegerField', [], {}),
            'sentiment_PCOI': ('django.db.models.fields.IntegerField', [], {}),
            'sentiment_PCVOLUME': ('django.db.models.fields.IntegerField', [], {}),
            'sentiment_composite': ('django.db.models.fields.IntegerField', [], {}),
            'sentiment_liquidity': ('django.db.models.fields.IntegerField', [], {}),
            'sentiment_socNetwork': ('django.db.models.fields.IntegerField', [], {}),
            'tech_MACD': ('django.db.models.fields.IntegerField', [], {}),
            'tech_RSI': ('django.db.models.fields.IntegerField', [], {}),
            'tech_bollinger': ('django.db.models.fields.IntegerField', [], {}),
            'tech_composite': ('django.db.models.fields.IntegerField', [], {}),
            'tech_stochastic': ('django.db.models.fields.IntegerField', [], {}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.performance': {
            'Meta': {'object_name': 'Performance'},
            'absolute_returns_12month': ('django.db.models.fields.FloatField', [], {}),
            'absolute_returns_1month': ('django.db.models.fields.FloatField', [], {}),
            'absolute_returns_3month': ('django.db.models.fields.FloatField', [], {}),
            'absolute_returns_6month': ('django.db.models.fields.FloatField', [], {}),
            'absolute_returns_ytd': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_ind_returns_12month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_ind_returns_1month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_ind_returns_3month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_ind_returns_6month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_ind_returns_ytd': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_mkt_returns_12month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_mkt_returns_1month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_mkt_returns_3month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_mkt_returns_6month': ('django.db.models.fields.FloatField', [], {}),
            'rel_to_mkt_returns_ytd': ('django.db.models.fields.FloatField', [], {}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.ratio': {
            'Cash_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'Current_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'EV_to_EBITDA': ('django.db.models.fields.FloatField', [], {}),
            'EV_to_Sales': ('django.db.models.fields.FloatField', [], {}),
            'Gross_Margin': ('django.db.models.fields.FloatField', [], {}),
            'Inc_per_Employee': ('django.db.models.fields.FloatField', [], {}),
            'LongTerm_Debt_to_Equity': ('django.db.models.fields.FloatField', [], {}),
            'LongTerm_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'Ratio'},
            'Net_Margin': ('django.db.models.fields.FloatField', [], {}),
            'Operating_Margin': ('django.db.models.fields.FloatField', [], {}),
            'PBook_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'PCashFlow_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'PE_Current': ('django.db.models.fields.FloatField', [], {}),
            'PE_Ratio_extra_items': ('django.db.models.fields.FloatField', [], {}),
            'PE_Ratio_no_extra_items': ('django.db.models.fields.FloatField', [], {}),
            'PSales_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'Pretax_Margin': ('django.db.models.fields.FloatField', [], {}),
            'Quick_Ratio': ('django.db.models.fields.FloatField', [], {}),
            'Receivables_Turnover': ('django.db.models.fields.FloatField', [], {}),
            'Return_on_Assets': ('django.db.models.fields.FloatField', [], {}),
            'Return_on_Equity': ('django.db.models.fields.FloatField', [], {}),
            'Return_on_Invested_Capital': ('django.db.models.fields.FloatField', [], {}),
            'Return_on_Total_Capital': ('django.db.models.fields.FloatField', [], {}),
            'Rev_per_Employee': ('django.db.models.fields.FloatField', [], {}),
            'Total_Asset_Turnover': ('django.db.models.fields.FloatField', [], {}),
            'Total_Debt_to_EV': ('django.db.models.fields.FloatField', [], {}),
            'Total_Debt_to_Total_Assets': ('django.db.models.fields.FloatField', [], {}),
            'Total_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {}),
            'Total_Debt_to_Total_Equity': ('django.db.models.fields.FloatField', [], {}),
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
            'Meta': {'object_name': 'Ticker'},
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