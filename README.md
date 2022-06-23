# Page Rank Scrapper vis Scrapy

Scrape PageRank data using `scrapy`. 

Original library forked from: https://github.com/scloudyy/PageRank




# Collect Page Rank Dataset

We use `scrapy` to collect page rank dataset.

## Usage

0. Create a python virtual environment

You can use the virtual env package of your choice (pip,conda,etc.). 
Use python 3.10 as the virtual env python version. 
Perform all operations inside your virual env. 

Tutorials:
https://www.tutorialspoint.com/how-to-create-a-virtual-environment-in-python
https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/


1. install scrapy first (inside the virtual env). 

```shell
pip install scrapy
```

2. run `scrapy` inside `scrapy\`

```shell
cd scrapy
scrapy crawl pagerank
```


## Dataset

The data collected by spider will be stored into `keyvalue`, `transition` and `pr0` respectively.

`keyvalue` records the each url and its key, splited by '\t':

```
0\thttps://github.com/\n
1\thttps://github.com/features\n
2\thttps://github.com/business\n
3\thttps://github.com/explore\n
...
```

`transtion` records the relationship betwenn pages:

```
0\t0,1,2,3,4,5,6,7,8,9\n
...
```

page of id 0 points to pages of id 0,1,2,3,4,5,6,7,8,9, they are splited by '\t'

`pr0` is the initial page rank value for each page:

```
0\t1\n
1\t1\n
2\t1\n
...
```


## Reference

- [Original library](https://github.com/scloudyy/PageRank)
- [The PageRank Citation Ranking: Bringing Order to the Web, Page, Lawrence and Brin, Sergey and Motwani, Rajeev and Winograd, Terry](http://ilpubs.stanford.edu:8090/422/)
- [CONVERGENCE ANALYSIS OF AN IMPROVED PAGERANK ALGORITHM, Ilse C. F , Ipsen , Steve Kirkland](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.330.8697)
