#Imagine you’re creating an application for handling the stock
#of a small shop, and controlling when things go bad in the warehouse.
#We have a function that calculates the degrading quality of different
#products in a shop.
#Create all the tests you find meaningful for the following function.

#%%

from Exercise1 import Product
from Exercise1 import recalculate_quality

cheeses= [Product("cheese",0),Product("cheese",5),Product("cheese",-10),Product("cheese",1000)]
potatoes= [Product("potato",0),Product("potato",5),Product("potato",-10),Product("potato",1000)]
randoms_low = [Product("random",0),Product("blab",4),Product("apple",-10),Product("uz",1)]
randoms_high = [Product("random",5),Product("blab",10),Product("apple",100),Product("lol",10000)]



def test_recalculate_cheese():
    for cheese in cheeses:
        quality_before = cheese.quality
        recalculate_quality(cheese)
        quality_after = cheese.quality
        assert quality_before == quality_after + 2
        
def test_recalculate_potatoe():
    for potatoe in potatoes:
        quality_before = potatoe.quality
        recalculate_quality(potatoe)
        quality_after = potatoe.quality
        assert quality_before == quality_after + 0.5  
        
def test_recalculate_randomlow():
    for random in randoms_low:
        quality_before = random.quality
        recalculate_quality(random)
        quality_after = random.quality
        assert quality_before == quality_after + 3
        
def test_recalculate_randomhigh():
    for random in randoms_high:
        quality_before = random.quality
        recalculate_quality(random)
        quality_after = random.quality
        assert quality_before == quality_after
        
#%%        