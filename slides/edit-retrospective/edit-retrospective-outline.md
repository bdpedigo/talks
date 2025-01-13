---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
---

![bg](../themes/aibs-backgrounds/title.png)

<!-- _paginate: false -->
<!-- _class: title-slide -->

# Quantifying proofreading effects on connectivity

<div class="columns">
<div>

Ben Pedigo
(he/him)
Scientist I
Allen Institute for Brain Science

<div style='' >

![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [ben.pedigo@alleninstitute.org](mailto:ben.pedigo@alleninstitute.org)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>

</div>
<div>

</div>
</div>

---

# Outline

- Background on proofreading in connectomics
- Framework for quantifying proofreading effects
- Examples
  - Example 1
  - Example 2
  - Example 3
- Conclusions

---

# Background

<!-- - EM connectomics is done by automated segmentation, followed by human proofreading
- This process is labor intensive, takes a while, and costly -->

<div class="columns-bl">
<div>

![](images/em-pipeline.png)

</div>
<div>

</div>
</div>

<!-- _footer: MICrONS Consortium et al. (2023) -->

---

# Background

<!-- - EM connectomics is done by automated segmentation, followed by human proofreading
- This process is labor intensive, takes a while, and costly -->

<div class="columns-bl">
<div>

![](images/em-pipeline-focus.png)

</div>
<div>

![center](images/editing.png)

- Labor-intensive
- Costly
- Takes time

</div>
</div>

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Dorkenwald et al. *bioRxiv* (2023) -->

---

# Proofreading edits

- We have a record of many edits now, across several datasets
  - **>800K in Minnie, ~2.5 million in V1dd**
    ![h:300](./images/cumulative_edits.svg)

<style scoped>
h3 {
  justify-content: center;
  text-align: center;
}
</style>

### How (and how much) do these edits matter for downstream conclusions?

---

# Why investigate the effect of proofreading?

<div class="columns-bl">
<div>

- Learn how much proofreading is needed to answer a question
  - E.g. how much proofreading to identify connectivity type?
- Understand what quantitative claims we can make given proofreading-induced variability
  - E.g. how to compare short-range vs. long-range connections?
- Learn what future proofreading strategies could be most effective

</div>
<div>

![](./images/philipp-variability.png)

</div>
</div>

<!-- _footer: Schlegel et al. bioRxiv (2023) -->

---

# CAVE provides a full history of edits

---
