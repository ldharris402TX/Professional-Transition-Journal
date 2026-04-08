#[List] of houses exercise
portfolio = ["221B Baker St", "Beverly Hills 90210", "1234 Main St"]
#{Dictionary} using labels(address) and values(house price) no quotes around the price
lhr_house = {"address": "221B Baker St", "price":500_000, "status":"Available"}
bev_house = {"address": "Beverly Hills 90210", "price": 5_000_000, "status": "Available"}
mco_house = {"address": "1234 Main St", "price": 2_500_000, "status": "Available"}
#adding {dictionary} variables to [list]
re_office = [lhr_house,bev_house,mco_house]
#for loop-"for house"pick one folder & name it house "in re_office" tells it which drawer to look in
for house in re_office:
    print(house)