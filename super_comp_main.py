from super_market_compare import compare_prices 

laughs_tissues = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
glomark_tissues = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

laughs_bread = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
glomark_bread = 'https://glomark.lk/sandwich-bread-450g/p/13606'

print("\n")
compare_prices(laughs_coconut,glomark_coconut)
print("\n")
compare_prices(laughs_bread,glomark_bread)
print("\n")
compare_prices(laughs_tissues,glomark_tissues)
print("\n")