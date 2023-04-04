---
marp: true
theme: slides
size: 16:9
paginate: true
---
 
# Opening slide 

--- 
# Why we care about connectomics 
- Linking the connectome to other things 

--- 
# Comparison as one natural solution to this 
- explain how it could help things 
- Give some examples as they fit in to Allen institute work and what I'd want to do? 
- (reach) try to tie in function... 
- goals: 
  - statistically valid 
  - scaleable / easy to use
  - neuroscientifically interesting... 

--- 
# Outline 
- maggot work, introduce the data 
- Work on comparing the hemispheres 
- Matching 

---
# Show the data 
- morphology
- connectivity 

---
... say more about the science paper? 

---
# bilateral symmetry - what is it, how would we know? 
- remember to tie back into this idea of comparison of datasets in general

---
# testing 
- two sample testing and two network sample testing on the same slide 

--- 
# assumptions slide (maybe)

---
# stochastic block model slide
- show what the model is 
- maybe (on the same slide) show that it is valid/powerful 
- mention happy to talk about methods otherwise 

--- 
# differences in group connection probabilities 
- show the p-value heatmap 

---
# but wait 
- if you run this with the "one block model" or erdos renyi model, also significant! 
  
---
# should we be surprised 
- show probability comparison left right for the significant ones 

--- 
# summary of this part 
- mention that the paper also talks about weights and the power of these tests, and 
  that i'd be happy to talk about any details 

---
# homologous neuron pairing 
- show examples of these neurons in light images 

--- 
# graph matching 
- show the diagram and the frob norm measure, hopefully on the same slide

--- 
# bisected graph matching explanation 
- show that it improves things on 5 different datasets 

--- 
# show performance with all bells and whistles 
- mention that we're also working with greg jefferis to incorporate morphology, maybe 

---
# graspologic 
- mention collaboration with microsoft research, where we've used some of the network 
  data science tools we've created to explore search and/or workplace communication. 

--- 
# what i want to do next 

**want to understand the regularities and variations in neural wiring**
*and ultimately, how these differences (or lack thereof) give rise to function*

what i said in the app 
- (1) techniques to enable robust alignment between datasets, including of complex neuron annotations and phenotypes, 
- (2) improved methods of comparing connectivity patterns within and between connectomes, and 
- (3) inferring relationships between variation in connectivity and other phenotypes.

map, compare, relate (so what)

---
# mapping between datasets

- how to associate {neurons, neuron types, ...} in one {dataset, modality} with that in 
  another 
- mention morphology, NBLAST, SegCLR
  - how well do these elements transfer to new {modalities, datasets}, e.g. 
    - when geometry changes in a new part of cortex
    - when proofreading was done to slightly different levels
    - changes in age of the sample (e.g. P36 or P54)
  - (maybe) mention the transfer learning, 0-shot ideas with a few anchors

--- 
# given these mappings, want to do comparisons! 
...
- want to account for technological variability

---

---
# references 
- science 
- elife
- network neuroscience 
- jmlr 
  
- stat conn
- connectal coding 

- goat 
- multiscale comparative connectomics