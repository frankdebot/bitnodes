# Bitnodes - Litecoin
Bitnodes is currently being developed to estimate the size of the Litecoin network by finding all the reachable nodes in the network. The current methodology involves sending [getaddr](https://en.Litecoin.it/wiki/Protocol_specification#getaddr) messages recursively to find all the reachable nodes in the network, starting from a set of seed nodes. Bitnodes uses Litecoin protocol version 70001 (i.e. >= /Satoshi:0.8.x/), so nodes running an older protocol version will be skipped.

## Setup
See [Provisioning Litecoin Network Crawler](https://github.com/ayeowch/bitnodes/wiki/Provisioning-Litecoin-Network-Crawler)

BITNODES TAKES UP ONE CONNECTION SLOT FROM EACH REACHABLE NODE IN THE NETWORK. IF YOU INTEND TO USE BITNODES TO CRAWL THE NETWORK, PLEASE CONSIDER RUNNING ONLY 1 INSTANCE OF THE CRAWLER TO AVOID TAKING UP THE VALUABLE CONNECTION SLOTS FROM EACH NODE.

## License
Copyright (c) 2014 Addy Yeow Chin Heng &lt;ayeowch@gmail.com&gt;

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
