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

<div class="columns">
<div>

## Ben Pedigo

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

- We have many edits which have been performed, especially in Minnie. Opportunity to learn from these edits and see what they can teach us going forward
- Still some work required in terms of code/tooling to do things like data augmentation, as well as science

---

# Categorizing these ideas

## Examples

|              | Understand                               | Improve                           |
| ------------ | ---------------------------------------- | --------------------------------- |
| Morphology   | Classifiers perform well on unproofread? | Classifiers robust to seg. errors |
| Connectivity | Motifs hold w/o proofreading?            | Target proofreading by question   |

---

# Overview

- What I mean by each of these ideas
- Brief example / vignette
- Constraints / effort / interest

---

# Understand morphology : proofreading

- How does performance of morphological classifiers change as a function of proofreading level?
  - Should we trust certain classifications more than others?
- What are the key points to edit which matter in terms of morphological classification?
- If we know the cell type (e.g. from somatic features alone) can we model how proofread a given neuron is?

---

# < insert example figure >

---

# Work to be done

---

# Understand connectivity : proofreading

- Are any connectivity patters stable without proofreading?
  - E.g. how much proofreading needs to happen to be able to identify a cell as belonging to a particular connectivity class?
  - E.g. how much would we expect conclusions about connectivity to change if we expanded analysis outside of the column, to include unproofread stuff?
- How does the chance of finding a connection depend on distance between partners?
- How much of the uncertainty in connectivity estimands (e.g. $P(\text{type 1} \rightarrow \text{type 2})$) comes from proofreading?
- Can we make a quantitative case for expanding analysis to the rest of the column?

---

# < insert example figure >

---

---

# Sensitivity - morphology

---

# Random uncategorized

<style scoped>

ul {
    font-size: 20px;
}

</style>

- How would we find cell-type connectivity pattern that we haven't seen, in the sea of
  un-proofread stuff?
  - There are tons of just disconnected axons, adding those back on would be a huge
    benefit
- Model of which neurons are close to / far from cell type specific connectivity pattern that we know
- Prediction of where edits might need to occur on a neuron, e.g. make a list of points to check w/ in neuroglancer
- How sensitive are morphological classifiers to proofreading errors? Can we make them more robust?
- Can we make a quantitative/statistical argument for expanding the analysis to the column for specific questions?
  - How does connectivity estimand depend on proofreading?
  - How much do we need to shink variance to say anything?
  - Prediction powered inference idea
- Data augmentation/resampling method for machine learning on skeletons
  - Understand how classifiers are affected by proofreading
    - Paths through feature space as a neuron is proofread
  - Develop more robust classifiers
- Predicting completeness level for a given neuron
  - Algorithm that eats a neuron in current state, predicts its level of proofreading
    - Not sure what the feature space is for this to make it useful
  - Unclear to me whether one could expect this to work for arbitrary neurons
    - Perhaps if we can predict cell type just from somatic features, or NNs from somatic features, can look at distribution of other features.
