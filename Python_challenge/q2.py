#################################################################################
# ShopGrok Python Challenge - Regular Expression
# Question 2.2
# By Sean Go
#################################################################################

import re
generic_urls = [
    "https://www.genericdomain.com/abc/def/1290aodwb23-ghi.img",
    "https://www.genericdomain.com/abc/31287bdwakj-jkl.img",
    "https://www.genericdomain.com/19unioawd02-jkl.img"
]

test_list = list()
for url in generic_urls:
    special_sequence = re.search('/\w*-', url).group().strip('/-')
    test_list.append(special_sequence)

#################################################################################
# Test
#################################################################################

assert test_list == ['1290aodwb23', '31287bdwakj', '19unioawd02']
    