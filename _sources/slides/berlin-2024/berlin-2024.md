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

# Connectome proofreading

<!-- ![bg](../themes/aibs-backgrounds/Slide4.png) -->

<div class="columns-br">
<div>

![](images/editing.png)

<div class="p" style="font-size: 0.55em; text-align: center;">

CAVE: Connectome Annotation Versioning Engine
Dorkenwald, Schneider-Mizell et al. _bioRxiv_ (2023)

</div>

</div>
<div>

![](./images/all_edits_by_time-target_id=271886.gif)

</div>
</div>

### How and how much do these edits matter for downstream conclusions?

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Schneider-Mizell et al. *bioRxiv* (2023),  Schneider-Mizell et al. *bioRxiv* (2023) -->

---

# Inhibition in mouse visual cortex

![](images/inhibition-census-gallery.png)

<!--
# CAVE allows us to extract the complete edit history

![h:500 center](./images/all_edits_by_time-root_id=864691135213953920.gif)

_footer: Dorkenwald, Schneider-Mizell et al. *bioRxiv* (2023) -->

<!-- _footer: Schneider-Mizell et al. *bioRxiv* (2023) -->

---

# Quantifying proofreading impact

![h:500 center](./images/all_edits_by_time_with_plots-target_id=271886.gif)

![h:50 center](images/cell-type-legend.png)

<!-- _footer: Neurons/colors from Schneider-Mizell et al *bioRxiv* (2023) -->

---

# Measuring distance from the fully proofread neuron

<div class="columns">
<div>

{ describe distances idea }

</div>
<div>

![right h:400](./images/historical-ordering-props_by_mtype-distance-root_id=864691135213953920.png)

</div>
</div>

---

# Most neurons "converged" fairly quickly

![h:500 center](./images/multi-metrics.png)

---

# Counterfactual games

- So far, have looked at how neurons changed over the course of proofreading in actuality, but this is a somewhat arbitrary historical ordering
- Can replay edits (or not) according to alternative schemes

---

# (1) "sloppy" proofreading?

![](images/half_edit_heatmaps.png)

---

# (2) what if I omit individual edits? (importance)

![h:500 center](images/edit_dropout_importance_root_id=864691135213953920.png)

---

# (3) which neurons are "good enough"?

![h:500 center](images/closeness-by-n_outputs.png)

---

# Summary

- Monitoring proofreading with specific analyses or metrics in mind ...
- Counterfactual replay of various edit schemes can help understand how ...
- Analyses could be applied to other datasets (especially CAVE-backed) or even to analyze automated proofreading systems
