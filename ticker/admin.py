from django.contrib import admin
from ticker.models import Ticker, Performance, Indicator, Ratio, Estimate, Supplement_ticker_info, Comment

#admin.site.register(Ticker)

class PerformanceInLine(admin.TabularInline):
    model = Performance

class IndicatorInLine(admin.TabularInline):
    model = Indicator

class RatioInline(admin.TabularInline):
    model = Ratio

class EstimateInline(admin.TabularInline):
    model = Estimate

class Supplement_ticker_infoInline(admin.TabularInline):
    model = Supplement_ticker_info

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class TickerAdmin(admin.ModelAdmin):
#    fieldsets = [        (None, {'fields': ['business_des', 'symbol']}),    ]
    inlines = [
        PerformanceInLine,
        IndicatorInLine,
        RatioInline,
        EstimateInline,
        Supplement_ticker_infoInline,
        CommentInline
    ]

admin.site.register(Ticker, TickerAdmin)


#admin.site.register(Performance)
#admin.site.register(Indicator)
#admin.site.register(Snapshot)
#admin.site.register(Estimate)
#admin.site.register(Supplement_ticker_info)
#admin.site.register(Comment)
#admin.site.register(Test_Data)
