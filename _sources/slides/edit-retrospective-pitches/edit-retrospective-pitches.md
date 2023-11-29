---
marp: true
theme: slides
size: 16:9
paginate: true
math: true
---

<!-- _paginate: false -->

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

<style scoped>
p {
    font-size: 24px;
}
</style>

# Proofreading retrospective

## Project ideas and discussion

<div class="columns">
<div>

##### Ben Pedigo

(he/him)
Scientist I
Allen Institute for Brain Science

![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [ben.pedigo@alleninstute.org](mailto:ben.pedigo@alleninstitute.org)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>
<div>

<!-- ### These slides at:  -->

<!-- [bdpedigo.github.io/talks/aibs.html](https://bdpedigo.github.io/talks/aibs.html) -->

</div>
</div>

---

# Big picture

- We have a record of many edits, especially in Minnie
  - Opportunity to learn from these edits, see what they can teach us going forward
- Still some work required in terms of code/tooling to do things like data augmentation, as well as science

---

# < insert mind map here >

---

# Overview

- What I mean by each of these ideas
- Approach
- Brief proof-of-concepts
- Interest / Significance / Feasibility

---

# Sensitivity to proofreading: connectivity

- Understand {how, which} connectivity features change with proofreading (+ possibly other features, like distance)
  - How much proofreading needs to happen to be able to identify a cell as belonging to a particular connectivity class?
- Motivate extending analyses to volumes which include unproofread material
  - Argue that particular features don't change, or
  - Developing a convincing corrective models of the bias corrected by proofreading

---

# Stable neuron

![h:400 center](images/exc_group_connectivity_root=864691135865971164.png)

---

# Unstable neurons

<div class="columns">
<div>

![center](images/exc_group_connectivity_root=864691136578765076.png)

</div>
<div>

![center](images/exc_group_connectivity_root=864691135992790209.png)

</div>
</div>

\* super high variance comes from axon/soma merger, I think

---

# Approach

- Examine affect of proofreading on connectivity estimands,
  - e.g. $P(\text{type } i \rightarrow \text{type } j)$, $P(\text{type } i \rightarrow \text{type } j) \circledast \text{compartment}$, etc.
- Develop quantitative model of this relationship
  - e.g. predict # of missing synapses in original segmentation, using column as the training data
- Possible goal 1:
- Possible goal 2: Apply model to unproofread data, assess variance in estimand, decide if proofreading is worthwhile

---

# Prior work on quality-quantity tradeoff

## Would you rather have bit of highly-curated data, or lots of messy data?

![h:150 center](images/quantity-quality-tradeoff.png)

Depends on the question, but there exist theoretical cases where you want the latter

## Would you rather have a bit of highly-curated data or lots of ~~messy~~ _unproofread, biased_ data?

---

# Analogy to "prediction powered inference"

![center h:500](images/prediction-powered-summary.png)

<!-- _footer: Angelopoulos et al. arXiv (2023) -->

---

# Analogy from "prediction powered inference"

![center h:500](images/prediction-powered-examples.png)

<!-- _footer: Angelopoulos et al. arXiv (2023) -->

---

# Challenges

<!--
- Does not require running much classification code that hasn't already been run, since just operating on the unproofread bulk of Minnie, say -->

- Unsure what the feature set is as input for a model on how proofreading errors affect connectivity
- Answer is likely very question specific; unclear to what extent any lessons will generalize
- Likely need to assume some kind of homogeneity across the volume for this to work
  - May not be palatable to the community

---

# Resampling skeletons

- Understand {whether, how} skeleton features are affected by proofreading
- Develop classifiers/clustering methods which are robust to such differences

---

# Example frankeneurons

<iframe height=500 frameborder=0 src="images/skeleton_samples_root_id=864691135915450982_use_cc=True.html">
</iframe>

---

# Frankeneuron </br> features

![bg right:65% center h:600](images/feature_samples_root_id=864691135915450982_use_cc=True.png)

---

# Challenges

- Need to decide how to "play back" edits in a plausible way
  - E.g. make proximal edits more likely?
- Running skeletonizaiton/featurization code on $O(100,000)$ neurons $\times$ $O(1,000)$
  - May be possible to run some code on the "final" skeleton, map those features (e.g. axon/dendrite labels) onto the rest
- Open-ended in terms of the deliverable/impact...
  - What models would we be interested in training with this kind of augmented data?

---

<!-- Null space of the idea above -->

# Machine-guided or hypothesis-driven proofreading

Now that we have these connectome volumes, how should we spend our time?

- Algorithm that eats a neuron and predicts completeness
- Algorithm that eats a segmentation and predicts sites for edits
  - Better version: eats a segmentation and a _statistic_, predicts _impactful_ edits
    - Find neurons where we need information to assign C-type
    - Find edits likely to attach many synapses

---

# Approach

- Develop local feature set, ideally reusing relevant tested models (PSS, SegCLR, ...)
  - Features could involve anything in power set of {image, segmentation, skeleton, skeleton attributes}
- Using training set of available edits, train {NN, RFC, ...}
- Validate on held out neurons or subvolume
- Deployment is a tricker question
  - Initial pass could just run predictions on a fixed materialization prior to a bout of proofreading
- More elaborate version: predict (edit location, importance)
  - E.g. find me edits likely to add many synapses

---

# Example differential "importance"

Merge dependency graphs for two neurons, size of node = # of dependent synapses

<div class="columns">
<div>

![h:520 center](images/merge_dependency_tree_root=864691135995711402.png)

</div>
<div>

![h:520 center](images/merge_dependency_tree_root=864691135013445270.png)

</div>
</div>

---

# Challenges

- Feature set?
  - "Neuron" could be anything in power set of {skeleton, compartment labels, synapse locations, connectivity profile, ...}
- Little proof-of-concept for feasibility (as far as I know)
  - For a random neuron, can we predict where its primary axon might be?
  - Is it possible to predict completeness from a cell you know nothing else about?
    - What if you know something about its cell type, say from PSS features?
- Dynamics: to be useful, would this be running on neurons all the time as they are edited, like the L2cache?
- Overlap with other work on auto-proofreading?

---

# Summary

![h:500](./../../../results/figs/edit_retrospective_evaluation/retrospective_evaluation.png)

---

# Thoughts?
