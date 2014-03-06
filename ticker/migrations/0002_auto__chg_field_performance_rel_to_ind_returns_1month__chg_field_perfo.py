# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Performance.rel_to_ind_returns_1month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_1month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.absolute_returns_3month'
        db.alter_column(u'ticker_performance', 'absolute_returns_3month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_ind_returns_12month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_12month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.absolute_returns_1month'
        db.alter_column(u'ticker_performance', 'absolute_returns_1month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_mkt_returns_1month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_1month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_mkt_returns_ytd'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_ytd', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.absolute_returns_6month'
        db.alter_column(u'ticker_performance', 'absolute_returns_6month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_ind_returns_3month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_3month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_mkt_returns_3month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_3month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_mkt_returns_12month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_12month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_ind_returns_6month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_6month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.absolute_returns_12month'
        db.alter_column(u'ticker_performance', 'absolute_returns_12month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_mkt_returns_6month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_6month', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.absolute_returns_ytd'
        db.alter_column(u'ticker_performance', 'absolute_returns_ytd', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Performance.rel_to_ind_returns_ytd'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_ytd', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PSales_Ratio'
        db.alter_column(u'ticker_ratio', 'PSales_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.LongTerm_Debt_to_Total_Capital'
        db.alter_column(u'ticker_ratio', 'LongTerm_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Rev_per_Employee'
        db.alter_column(u'ticker_ratio', 'Rev_per_Employee', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Gross_Margin'
        db.alter_column(u'ticker_ratio', 'Gross_Margin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.LongTerm_Debt_to_Equity'
        db.alter_column(u'ticker_ratio', 'LongTerm_Debt_to_Equity', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PCashFlow_Ratio'
        db.alter_column(u'ticker_ratio', 'PCashFlow_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Cash_Ratio'
        db.alter_column(u'ticker_ratio', 'Cash_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Receivables_Turnover'
        db.alter_column(u'ticker_ratio', 'Receivables_Turnover', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PE_Current'
        db.alter_column(u'ticker_ratio', 'PE_Current', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Total_Debt_to_Total_Assets'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Assets', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Total_Debt_to_Total_Capital'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.EV_to_EBITDA'
        db.alter_column(u'ticker_ratio', 'EV_to_EBITDA', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Pretax_Margin'
        db.alter_column(u'ticker_ratio', 'Pretax_Margin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Total_Debt_to_Total_Equity'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Equity', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.EV_to_Sales'
        db.alter_column(u'ticker_ratio', 'EV_to_Sales', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PE_Ratio_extra_items'
        db.alter_column(u'ticker_ratio', 'PE_Ratio_extra_items', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Net_Margin'
        db.alter_column(u'ticker_ratio', 'Net_Margin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Operating_Margin'
        db.alter_column(u'ticker_ratio', 'Operating_Margin', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Total_Asset_Turnover'
        db.alter_column(u'ticker_ratio', 'Total_Asset_Turnover', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Return_on_Total_Capital'
        db.alter_column(u'ticker_ratio', 'Return_on_Total_Capital', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PBook_Ratio'
        db.alter_column(u'ticker_ratio', 'PBook_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Total_Debt_to_EV'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_EV', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Current_Ratio'
        db.alter_column(u'ticker_ratio', 'Current_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Return_on_Assets'
        db.alter_column(u'ticker_ratio', 'Return_on_Assets', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Inc_per_Employee'
        db.alter_column(u'ticker_ratio', 'Inc_per_Employee', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Quick_Ratio'
        db.alter_column(u'ticker_ratio', 'Quick_Ratio', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.PE_Ratio_no_extra_items'
        db.alter_column(u'ticker_ratio', 'PE_Ratio_no_extra_items', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Return_on_Invested_Capital'
        db.alter_column(u'ticker_ratio', 'Return_on_Invested_Capital', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Ratio.Return_on_Equity'
        db.alter_column(u'ticker_ratio', 'Return_on_Equity', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Indicator.tech_bollinger'
        db.alter_column(u'ticker_indicator', 'tech_bollinger', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.quant_value'
        db.alter_column(u'ticker_indicator', 'quant_value', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.sentiment_liquidity'
        db.alter_column(u'ticker_indicator', 'sentiment_liquidity', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.tech_composite'
        db.alter_column(u'ticker_indicator', 'tech_composite', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.tech_RSI'
        db.alter_column(u'ticker_indicator', 'tech_RSI', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.tech_MACD'
        db.alter_column(u'ticker_indicator', 'tech_MACD', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.quant_profit'
        db.alter_column(u'ticker_indicator', 'quant_profit', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.sentiment_PCVOLUME'
        db.alter_column(u'ticker_indicator', 'sentiment_PCVOLUME', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.quant_composite'
        db.alter_column(u'ticker_indicator', 'quant_composite', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.sentiment_PCOI'
        db.alter_column(u'ticker_indicator', 'sentiment_PCOI', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.quant_management'
        db.alter_column(u'ticker_indicator', 'quant_management', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.tech_stochastic'
        db.alter_column(u'ticker_indicator', 'tech_stochastic', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.sentiment_socNetwork'
        db.alter_column(u'ticker_indicator', 'sentiment_socNetwork', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.sentiment_composite'
        db.alter_column(u'ticker_indicator', 'sentiment_composite', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Indicator.quant_growth'
        db.alter_column(u'ticker_indicator', 'quant_growth', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.Last_Quarters_Earnings'
        db.alter_column(u'ticker_estimate', 'Last_Quarters_Earnings', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.Year_Ago_Earnings'
        db.alter_column(u'ticker_estimate', 'Year_Ago_Earnings', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.sell_present'
        db.alter_column(u'ticker_estimate', 'sell_present', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.buy_1_month_ago'
        db.alter_column(u'ticker_estimate', 'buy_1_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.Median_PE_on_Next_FY_Estimate'
        db.alter_column(u'ticker_estimate', 'Median_PE_on_Next_FY_Estimate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.sell_3_month_ago'
        db.alter_column(u'ticker_estimate', 'sell_3_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.sell_1_month_ago'
        db.alter_column(u'ticker_estimate', 'sell_1_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.FY_Report_Date'
        db.alter_column(u'ticker_estimate', 'FY_Report_Date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Estimate.Next_Fiscal_Year_Estimate'
        db.alter_column(u'ticker_estimate', 'Next_Fiscal_Year_Estimate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.hold_present'
        db.alter_column(u'ticker_estimate', 'hold_present', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.Number_of_Ratings'
        db.alter_column(u'ticker_estimate', 'Number_of_Ratings', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.Average_Target_Price'
        db.alter_column(u'ticker_estimate', 'Average_Target_Price', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.hold_1_month_ago'
        db.alter_column(u'ticker_estimate', 'hold_1_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.buy_3_month_ago'
        db.alter_column(u'ticker_estimate', 'buy_3_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.buy_present'
        db.alter_column(u'ticker_estimate', 'buy_present', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Estimate.Median_PE_on_CY_Estimate'
        db.alter_column(u'ticker_estimate', 'Median_PE_on_CY_Estimate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.Current_Quarter_Estimate'
        db.alter_column(u'ticker_estimate', 'Current_Quarter_Estimate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.Current_Year_Estimate'
        db.alter_column(u'ticker_estimate', 'Current_Year_Estimate', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Estimate.hold_3_month_ago'
        db.alter_column(u'ticker_estimate', 'hold_3_month_ago', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Performance.rel_to_ind_returns_1month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_1month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.absolute_returns_3month'
        db.alter_column(u'ticker_performance', 'absolute_returns_3month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_ind_returns_12month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_12month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.absolute_returns_1month'
        db.alter_column(u'ticker_performance', 'absolute_returns_1month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_mkt_returns_1month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_1month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_mkt_returns_ytd'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_ytd', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.absolute_returns_6month'
        db.alter_column(u'ticker_performance', 'absolute_returns_6month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_ind_returns_3month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_3month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_mkt_returns_3month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_3month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_mkt_returns_12month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_12month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_ind_returns_6month'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_6month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.absolute_returns_12month'
        db.alter_column(u'ticker_performance', 'absolute_returns_12month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_mkt_returns_6month'
        db.alter_column(u'ticker_performance', 'rel_to_mkt_returns_6month', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.absolute_returns_ytd'
        db.alter_column(u'ticker_performance', 'absolute_returns_ytd', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Performance.rel_to_ind_returns_ytd'
        db.alter_column(u'ticker_performance', 'rel_to_ind_returns_ytd', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PSales_Ratio'
        db.alter_column(u'ticker_ratio', 'PSales_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.LongTerm_Debt_to_Total_Capital'
        db.alter_column(u'ticker_ratio', 'LongTerm_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Rev_per_Employee'
        db.alter_column(u'ticker_ratio', 'Rev_per_Employee', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Gross_Margin'
        db.alter_column(u'ticker_ratio', 'Gross_Margin', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.LongTerm_Debt_to_Equity'
        db.alter_column(u'ticker_ratio', 'LongTerm_Debt_to_Equity', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PCashFlow_Ratio'
        db.alter_column(u'ticker_ratio', 'PCashFlow_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Cash_Ratio'
        db.alter_column(u'ticker_ratio', 'Cash_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Receivables_Turnover'
        db.alter_column(u'ticker_ratio', 'Receivables_Turnover', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PE_Current'
        db.alter_column(u'ticker_ratio', 'PE_Current', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Total_Debt_to_Total_Assets'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Assets', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Total_Debt_to_Total_Capital'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Capital', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.EV_to_EBITDA'
        db.alter_column(u'ticker_ratio', 'EV_to_EBITDA', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Pretax_Margin'
        db.alter_column(u'ticker_ratio', 'Pretax_Margin', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Total_Debt_to_Total_Equity'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_Total_Equity', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.EV_to_Sales'
        db.alter_column(u'ticker_ratio', 'EV_to_Sales', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PE_Ratio_extra_items'
        db.alter_column(u'ticker_ratio', 'PE_Ratio_extra_items', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Net_Margin'
        db.alter_column(u'ticker_ratio', 'Net_Margin', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Operating_Margin'
        db.alter_column(u'ticker_ratio', 'Operating_Margin', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Total_Asset_Turnover'
        db.alter_column(u'ticker_ratio', 'Total_Asset_Turnover', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Return_on_Total_Capital'
        db.alter_column(u'ticker_ratio', 'Return_on_Total_Capital', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PBook_Ratio'
        db.alter_column(u'ticker_ratio', 'PBook_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Total_Debt_to_EV'
        db.alter_column(u'ticker_ratio', 'Total_Debt_to_EV', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Current_Ratio'
        db.alter_column(u'ticker_ratio', 'Current_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Return_on_Assets'
        db.alter_column(u'ticker_ratio', 'Return_on_Assets', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Inc_per_Employee'
        db.alter_column(u'ticker_ratio', 'Inc_per_Employee', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Quick_Ratio'
        db.alter_column(u'ticker_ratio', 'Quick_Ratio', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.PE_Ratio_no_extra_items'
        db.alter_column(u'ticker_ratio', 'PE_Ratio_no_extra_items', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Return_on_Invested_Capital'
        db.alter_column(u'ticker_ratio', 'Return_on_Invested_Capital', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Ratio.Return_on_Equity'
        db.alter_column(u'ticker_ratio', 'Return_on_Equity', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Indicator.tech_bollinger'
        db.alter_column(u'ticker_indicator', 'tech_bollinger', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.quant_value'
        db.alter_column(u'ticker_indicator', 'quant_value', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.sentiment_liquidity'
        db.alter_column(u'ticker_indicator', 'sentiment_liquidity', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.tech_composite'
        db.alter_column(u'ticker_indicator', 'tech_composite', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.tech_RSI'
        db.alter_column(u'ticker_indicator', 'tech_RSI', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.tech_MACD'
        db.alter_column(u'ticker_indicator', 'tech_MACD', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.quant_profit'
        db.alter_column(u'ticker_indicator', 'quant_profit', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.sentiment_PCVOLUME'
        db.alter_column(u'ticker_indicator', 'sentiment_PCVOLUME', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.quant_composite'
        db.alter_column(u'ticker_indicator', 'quant_composite', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.sentiment_PCOI'
        db.alter_column(u'ticker_indicator', 'sentiment_PCOI', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.quant_management'
        db.alter_column(u'ticker_indicator', 'quant_management', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.tech_stochastic'
        db.alter_column(u'ticker_indicator', 'tech_stochastic', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.sentiment_socNetwork'
        db.alter_column(u'ticker_indicator', 'sentiment_socNetwork', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.sentiment_composite'
        db.alter_column(u'ticker_indicator', 'sentiment_composite', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Indicator.quant_growth'
        db.alter_column(u'ticker_indicator', 'quant_growth', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.Last_Quarters_Earnings'
        db.alter_column(u'ticker_estimate', 'Last_Quarters_Earnings', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.Year_Ago_Earnings'
        db.alter_column(u'ticker_estimate', 'Year_Ago_Earnings', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.sell_present'
        db.alter_column(u'ticker_estimate', 'sell_present', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.buy_1_month_ago'
        db.alter_column(u'ticker_estimate', 'buy_1_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.Median_PE_on_Next_FY_Estimate'
        db.alter_column(u'ticker_estimate', 'Median_PE_on_Next_FY_Estimate', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.sell_3_month_ago'
        db.alter_column(u'ticker_estimate', 'sell_3_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.sell_1_month_ago'
        db.alter_column(u'ticker_estimate', 'sell_1_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.FY_Report_Date'
        db.alter_column(u'ticker_estimate', 'FY_Report_Date', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Estimate.Next_Fiscal_Year_Estimate'
        db.alter_column(u'ticker_estimate', 'Next_Fiscal_Year_Estimate', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.hold_present'
        db.alter_column(u'ticker_estimate', 'hold_present', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.Number_of_Ratings'
        db.alter_column(u'ticker_estimate', 'Number_of_Ratings', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.Average_Target_Price'
        db.alter_column(u'ticker_estimate', 'Average_Target_Price', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.hold_1_month_ago'
        db.alter_column(u'ticker_estimate', 'hold_1_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.buy_3_month_ago'
        db.alter_column(u'ticker_estimate', 'buy_3_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.buy_present'
        db.alter_column(u'ticker_estimate', 'buy_present', self.gf('django.db.models.fields.IntegerField')(default=None))

        # Changing field 'Estimate.Median_PE_on_CY_Estimate'
        db.alter_column(u'ticker_estimate', 'Median_PE_on_CY_Estimate', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.Current_Quarter_Estimate'
        db.alter_column(u'ticker_estimate', 'Current_Quarter_Estimate', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.Current_Year_Estimate'
        db.alter_column(u'ticker_estimate', 'Current_Year_Estimate', self.gf('django.db.models.fields.FloatField')(default=None))

        # Changing field 'Estimate.hold_3_month_ago'
        db.alter_column(u'ticker_estimate', 'hold_3_month_ago', self.gf('django.db.models.fields.IntegerField')(default=None))

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
            'Average_Target_Price': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Consensus_1_month_ago': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Consensus_3_month_ago': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Consensus_present': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Current_Quarter_Estimate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Current_Year_Estimate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'FY_Report_Date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'Last_Quarters_Earnings': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Median_PE_on_CY_Estimate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Median_PE_on_Next_FY_Estimate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Estimate'},
            'Next_Fiscal_Year_Estimate': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Number_of_Ratings': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'Year_Ago_Earnings': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'buy_1_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'buy_3_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'buy_present': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hold_1_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hold_3_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'hold_present': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sell_1_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sell_3_month_ago': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sell_present': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'liquidity_level': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'quant_composite': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quant_growth': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quant_management': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quant_profit': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'quant_value': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sentiment_PCOI': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sentiment_PCVOLUME': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sentiment_composite': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sentiment_liquidity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'sentiment_socNetwork': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tech_MACD': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tech_RSI': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tech_bollinger': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tech_composite': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tech_stochastic': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.performance': {
            'Meta': {'object_name': 'Performance'},
            'absolute_returns_12month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'absolute_returns_1month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'absolute_returns_3month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'absolute_returns_6month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'absolute_returns_ytd': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_ind_returns_12month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_ind_returns_1month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_ind_returns_3month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_ind_returns_6month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_ind_returns_ytd': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_mkt_returns_12month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_mkt_returns_1month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_mkt_returns_3month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_mkt_returns_6month': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'rel_to_mkt_returns_ytd': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'ticker': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ticker.Ticker']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'ticker.ratio': {
            'Cash_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Current_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'EV_to_EBITDA': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'EV_to_Sales': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Gross_Margin': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Inc_per_Employee': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'LongTerm_Debt_to_Equity': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'LongTerm_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Meta': {'object_name': 'Ratio'},
            'Net_Margin': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Operating_Margin': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PBook_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PCashFlow_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PE_Current': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PE_Ratio_extra_items': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PE_Ratio_no_extra_items': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'PSales_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Pretax_Margin': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Quick_Ratio': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Receivables_Turnover': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Return_on_Assets': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Return_on_Equity': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Return_on_Invested_Capital': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Return_on_Total_Capital': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Rev_per_Employee': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Total_Asset_Turnover': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Total_Debt_to_EV': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Total_Debt_to_Total_Assets': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Total_Debt_to_Total_Capital': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'Total_Debt_to_Total_Equity': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
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