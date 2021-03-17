#################################################################################
# ShopGrok Python Challenge - Regular Expression
# Question 2.1
# By Sean Go
#################################################################################

import re
product_count_text = "381 Products found"
product_count_int = int(re.search('[0-9]*', product_count_text).group())

#################################################################################
# Test
#################################################################################

assert product_count_int == 381
assert type(product_count_int) is int
    