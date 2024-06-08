---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
---

<!-- <style>
section::after {
    content: attr(data-marpit-pagination) '/24';
}
</style> -->

<!-- _paginate: false -->
<!-- _class: title-slide -->

![bg](../themes/aibs-backgrounds/title.png)

<!-- ![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg) -->

<!-- <h1 style="margin-top: 200px;">
Connectivity properties in light of proofreading
</h1> -->

<!-- <br> -->

# Connectivity properties in light of proofreading

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

# Proofreading impacts on connectomes

<!-- ![bg](../themes/aibs-backgrounds/Slide4.png) -->

<div class="columns">
<div>

![h:300](images/editing.png)

<span style="font-size: 0.6em; text-align: right;">*Dorkenwald, Schneider-Mizell et al. *bioRxiv* (2023)*</span>

Labor-intensive, Costly, Takes time

</div>
<div>

![](./images/all_edits_by_time-root_id=864691135213953920.gif)

</div>
</div>

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Dorkenwald et al. *bioRxiv* (2023) -->

### How and how much do these edits matter for downstream conclusions?

---

# CAVE allows us to extract the complete edit history

![h:500 center](./images/all_edits_by_time-root_id=864691135213953920.gif)

---

# Explain the proportion of outputs metric

{show how one of these neurons changes over time}

---

# Examples: stable neuron

<!-- Replaying some proportion of merges onto a neuron, evaluating connectivity -->

<!-- ![h:400 center](images/exc_group_connectivity_root=864691135865971164.png)
 -->

<div class="columns">
<div>

![center h:400](images/exc_group_connectivity_root_n=864691135865971164.png)

</div>
<div>

![center h:400](images/exc_group_connectivity_root_p=864691135865971164.png)

</div>
</div>

![h:100 center](images/cell-type-legend.png)

<!-- _footer: Neurons/colors from Schneider-Mizell et al *bioRxiv* (2023) -->

---

# Examples: unstable neuron

![bg](../themes/aibs-backgrounds/Slide4.png)

<div class="columns">
<div>

![center h:400](images/exc_group_connectivity_root_n=864691135992790209.png)

</div>
<div>

![center h:400](images/exc_group_connectivity_root_p=864691135992790209.png)

</div>
</div>

![h:100 center](images/cell-type-legend.png)

<!-- _footer: Neurons/colors from Schneider-Mizell et al *bioRxiv* (2023) -->

---
