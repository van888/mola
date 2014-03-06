from django.shortcuts import render, render_to_response
from ticker.models import Ticker, Comment, Performance, Ratio
from forms import TickerForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from haystack.query import SearchQuerySet

def home(request):
    args = {}
    args.update(csrf(request))
    args['tickers'] = Ticker.objects.all()

    # What content is on home page?
    # - mkt data
    # - marketing info
    # - search, img,
    return render_to_response('home.html', args)

def faq(request):
    return render_to_response('FAQ.html', request)

def tickers(request):

    args = {}
#    args.update(csrf(request))
    args['tickers'] = Ticker.objects.all()

    #return render_to_response('ticker.html', {'tickers': Ticker.objects.all()})
    return render_to_response('ticker.html', args)

#def article(request, article_id=1):
#    return render_to_response('article.html',
#        {'article': Article.objects.get(id=article_id) }
#    )

def get_sector_performer(symbol):
    ticker = Ticker.objects.get(symbol=symbol)
    sector = ticker.sector
    ytd = ticker.performance.absolute_returns_ytd
    p_test = Performance.objects.filter(ticker__sector=sector)
    print p_test
    #Ticker.objects.filter(super.performance.absolute_returns_ytd>ytd)
    #filter for other tickers where performance greater than that of selected ticker
    return p_test

def get_industry_performer(symbol):
    industry = Ticker.objects.get(symbol=symbol).industry
    return industry

def ticker(request, symbol="XOM"):
    ticker_id = Ticker.objects.get(symbol=symbol).id
    print ticker_id,"=", symbol

    sector = get_sector_performer(symbol)
    #print sector[0].ticker.symbol
    args = {}
    args.update(csrf(request))

    try:
        args['comment'] = Comment.objects.all()
    except:
        args['comment'] = None

#    args['performance'] = Performance.objects.all()
    args['sect'] = sector
    args['ticker'] = Ticker.objects.get(symbol=symbol)

    #return render_to_response('ticker.html', {'ticker': Ticker.objects.get(symbol=symbol)})
    return render_to_response('ticker.html', args)

def ticker_ratio(request, symbol):
    ticker_id = Ticker.objects.get(symbol=symbol).id
    print ticker_id,"=", symbol
    args = {}
    args['ratio'] = Ratio.objects.all()
    args['ticker'] = Ticker.objects.get(symbol=symbol)

    return render_to_response('ticker_ratio.html', args)

def add_comment(request, symbol):
    tic = Ticker.objects.get(symbol=symbol)
    if request.method == "POST":
        print symbol
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.ticker = tic
            c.save()
        return HttpResponseRedirect('/finance/%s' % symbol)
    else:
        f = CommentForm()
    args = {}
    args.update(csrf(request))
    args['ticker'] = tic
    args['form'] = f
    return render_to_response('add_comment.html', args)

def like_comment(request, symbol, id):
    print Comment.objects.get(id=id)
    if id:
        #id = Ticker.objects.get(symbol=symbol).id
        c = Comment.objects.get(id=id)
        count = c.likes
        count += 1
        c.likes = count
        c.save()
    return HttpResponseRedirect('/finance/%s/' % symbol)

def search_ticker(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    print 'ticker.views.search_ticker is running'
    t1 = Ticker.objects.filter(symbol__icontains=search_text)
    t2 = Ticker.objects.filter(company_name__icontains=search_text)
    tickers =t1|t2

    return render_to_response('ajax_search.html', {'tickers':tickers})

#    sqs1 = SearchQuerySet().filter(content_auto=request.POST.get('search_text',''))
#    sqs2 = SearchQuerySet().autocomplete(company_name=request.POST.get('search_text',''))
#    tickers = sqs1 | sqs2
#    return render_to_response('ajax_search.html', {'tickers':tickers})


