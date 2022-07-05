# Brooks' Law visualizer
This script draws an image with the lines of communication between a given amount of elements.

## History
The history of "Brook's law is described on Wikipedia in detail. The shortform:

Brooks' law is an observation about software project management according to which "adding manpower to a late software project makes it later".
It was coined by Fred Brooks in his 1975 book The Mythical Man-Month.

According to Brooks, under certain conditions, an incremental person when added to a project makes it take more, not less time.

https://en.wikipedia.org/wiki/Brooks%27s_law


## Overview
I saw a tweet about the "lines of communication" and a nice visual. Researching to find a source, I came across this post: http://leftfoot.com.au/blog/brooks-law-lines-of-communication-calculator-siri-shortcut

I wondered, how a visual with a huge amount of lines of communication would look like, so I began to look for a program, which would draw that with any given input size. I didn't find one.

So I decided to program one myself. 
As a professional tester, coding was never my strong suit and coding tutorials without any practical need never kept me for long.


This is my learning journey.
//Raw thoughts; need to refine them later:
- Starting reading up on the origin, found the formula to calculate the number of relationships ( n*(n-1)/2 ).
- Researched in tools, which draw nodes and edges.
- Read up on Graph Theory
- Decided on Python; seems to be an "easier" programming language to start with.
- Started to setup my coding environment (IntelliJ IDEA), installed python3
- Found GraphViz as a drawing tool
- Needed to create the graph file needed for drawing from scratch; no variable usage in dot language (˜GraphViz)



## Team size of 40 and the respective lines of communication
<img src="https://user-images.githubusercontent.com/13218613/177407375-b0e477b8-dd8d-46b1-a4d9-fb727bd33406.png" width=50% height=50%>
