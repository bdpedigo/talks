---
marp: true
theme: slides
size: 16:9
paginate: true
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

# Big picture

## Examples

|              | Understand                               | Improve                           |
| ------------ | ---------------------------------------- | --------------------------------- |
| Morphology   | Classifiers perform well on unproofread? | Classifiers robust to seg. errors |
| Connectivity | Motifs hold w/o proofreading?            | Target proofreading by question   |

---

# Ideas (big picture)

- Sensitivity analysis
  - Connectivity motifs / classification
  - Morphological classifiers or clustering
- Data augmentation
- Prediction

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

---

# Understand connectivity : proofreading

- Are any connectivity patters stable without proofreading?
  - E.g. how much proofreading needs to happen to be able to identify a cell as belonging to a particular connectivity class?
  - E.g. how much would we expect conclusions about connectivity to change if we expanded analysis outside of the column, to include unproofread stuff?

---

# < insert example figure >

---

# Sensitivity - morphology

---

# Random uncategorized (many from Forrest)

- How would we find cell-type connectivity pattern that we haven't seen, in the sea of
  un-proofread stuff?
  - There are tons of just disconnected axons, adding those back on would be a huge
    benefit
- how much would conclusions change if the connectivity analysis was expanded to the
  entire column?
- model of which neurons are close to / far from cell type specific connectivity pattern
  that we know
