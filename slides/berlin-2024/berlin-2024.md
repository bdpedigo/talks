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

# Measurement design in connectomics

<br>

<div class="columns">
<div>

![h:250 center](images/optimizing-title.png)

</div>
<div>

> Would you rather have many noisy connectivity measurements, or a few high-quality ones?

> There exists cases where you'd actually prefer the "sloppy" version

</div>
</div>

<br>

### Given finite resources, worth reflecting on how to proofread with specific scientific goals in mind

<!-- _footer: Priebe et al. *Communications in Statistics* (2013) -->

---

# Measurements in modern connectomics

### Automated segmentation + proofreading

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

![h:500 center](./images/all_edits_by_time-target_id=271886.gif)

</div>
</div>

<!-- ### How do these edits affect downstream conclusions? -->

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Schneider-Mizell et al. *bioRxiv* (2023) -->

---

# Inhibition in mouse visual cortex

![h:160 center](images/inhibition-census-wide.png)

![center h:300](images/casey-heatmap.png)

<div style="position: absolute; bottom: 30px; right: 140px;">

![h:60](images/casey-legend.png)

</div>

<!-- _footer: Schneider-Mizell et al. *bioRxiv* (2023) -->

<!-- ---

# Inhibition in mouse visual cortex

<div class="columns">
<div>

![](images/inhibitory-gallery.png)

</div>
<div>

- 163 inhibitory neurons were heavily proofread
- Characterized how inhibitory neurons distribute their outputs:

{diagram of proportion of outputs metric}

</div>
</div>

<!--
# CAVE allows us to extract the complete edit history

![h:500 center](./images/all_edits_by_time-root_id=864691135213953920.gif)

_footer: Dorkenwald, Schneider-Mizell et al. *bioRxiv* (2023) -->

---

<!-- # Connectivity during proofreading -->

![bg center fit](./images/all_edits_by_time_with_plots-target_id=271886.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](images/cell-type-legend.png)

</div>

<div style="position: absolute; bottom: 20px; right: 60px;">

![h:280](images/white.png)

</div>

---

<!-- # Connectivity during proofreading -->

<!-- _backgroundImage: None -->

![bg blur:5px opacity:40%](./images/paused.png)

<!-- <div style="position: absolute; bottom: 20px; right: 60px;">

![h:280](images/white.png)

</div> -->

![center h:600](images/distance-transparent.png)

---

![bg center fit](./images/all_edits_by_time_with_plots-target_id=271886-copy.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](images/cell-type-legend.png)

</div>

---

# Cell-type specific connectivity converged quickly

![h:500 center](./images/distance-lines-animation.gif)

---

# Counterfactual proofreading

Replay specific edits and not others, reconstruct what the network would look like

<div class="columns">
<div>

### What if I'd proofread each neuron to 50% extension?

![](images/clustering-target_p=0.5.png)

</div>
<div>

### Full proofreading

<br>

![](images/clustering-target_p=1.png)

</div>
</div>

<span style="text-align: center;">

NMI(50% proofreading, full proofreading) = 0.82

</span>

<!-- - So far, have looked at how neurons changed over the course of proofreading in actuality, but this is a somewhat arbitrary historical ordering
- Can replay edits (or not) according to alternative schemes
- E.g. what if we only had half the proofreading resources - how should we allocate them? -->

---

# Summary

<!-- - Worth understanding whether most neurons look like they have converged -->

- NOT saying we need less proofreading...
- Monitoring proofreading with specific analyses/metrics in mind could help us decide how much proofreading is needed for a specific question
- Counterfactual replay of edits can help understand how alternative proofreading strategies would affect downstream analyses

# Ongoing work

- Prediction of edit impact with respect to a feature of interest
- Prediction of whether a neuron is proofread enough for a specific analysis

<!-- - Counterfactual replay of various edit schemes can help understand how alternative proofreading strategies might affect downstream analyses -->
<!-- - Analyses could be applied to other datasets or even to analyze how design of automated proofreading systems affects conclusions -->

---

# Acknowledgements

<style scoped>
p {
    font-size: 11px;
}
</style>

<div class="columns">
<div>

**Network Anatomy**
Clay Reid
Agnes Bodor
Adam Bleckert
JoAnn Buchanan
Casey M. Schneider-Mizell
Dan Bumbarger
Derrick Brittain
Forrest Collman
Steven Cook
Nuno da Costa
Bethanny Danskin
Sven Dorkenwald
Leila Elabbady
Emily Joyce
Dan Kapner
Sam Kinn
Cheryl Lea
Gayathri Mahalingam
Ben Pedigo
Sharmi Seshamani
Jenna Schardt
Marc Takeno
Russel Torres
Wenjing Yin
Chi Zhang

</div>
<div>

**PM**
Lynne Becker
Florence D'Orazi
Sarah Naylor
Shelby Suckow
David Vumbaco
Susan Sunkin

**Morphology and 3D Reconstruction**
Rachel Dalley
Clare Gamlin
Staci Sorensen
Grace Williams

**Modeling & Simulation**
Ani Nandi
Tom Chartrand
Anatoly Buchin
Yina Wei
Soo Yeun Lee
Costas Anastassiou

**Technology**
Tim Fliss
Rob Young
And others

**IT**
Brian Youngstrom
Stuart Kendrick
Scott Harrison
Nathaniel Middleton
And others

</div>
<div>

**MPE**
Jay Borseth
Collin Farrell
And others

**MindScope**
Reza Abbasi-Asi
Anton Arkhipov
Michael Buice
Daniel Denman
Brian Hu
Josh Larkin
Stefan Mihalas
Daniel Millmann
Gabe Ocker
Naveen Ouellette
Kevin Takasaki
Saskia de Vries
Jun Zhuang

**Alen Institute for Brain Sciences**
Tanya Daigle
Shenqin Yao
Nikolas Jorstad
Trygve Bakken
Rebecca Hodge
Nathan Gouwens
Bosiljka Tasic
Ed Lein
Hongkui Zeng
And many others

</div>
<div>

**Princeton**
Sven Dorkenwald
Tommy Macrina
Sebastian Seung
Nick Turner
And team

**Baylor**
Jake Riemer
Andreas Tolias
And team

**Harvard Medical School**
Brett Graham
Wei-Chung Lee
And team

**Janelia**
Khaled Khairy
Stephan Saalfeld
Carolyn Ott
Jennifer Lippincott-Schwartz
And others

**JHU**
Jenna Glatzer
Dwight Bergles

**APL**
Brock Wester
And team

</div>
<div>

**Neuro Surgery and Behavior**
**Lab Animal Services**
**Transgenic Colony Management**
**Finance**
**Legal**

**Computing Resources**
BBP5 Supercomputing Resources
National Energy Research Computing Center
AI HPC
Google Cloud

**Funding**
IARPA - MICRONS
NSF - NeuroNex
NIH – BICCN

</div>
</div>

<!-- ---

# How would clustering change with different proofreading schemes?

![center ](images/ari-vs-merges.png)

--- -->
<!--
# Impactful edits are more often near the soma

![center](images/distance_vs_impact.png)

--- -->
<!--
# Space of simple edit allocation schemes

![center](images/iso-edit-contours.png) -->

<!-- # (1) "sloppy" proofreading?

![](images/half_edit_heatmaps.png) -->

<!-- ---

# (2) what if I omit individual edits? (importance)

![h:500 center](images/edit_dropout_importance_root_id=864691135213953920.png) -->

<!-- ---

# (3) which neurons are "good enough"?

![h:500 center](images/closeness-by-n_outputs.png) -->

## <!--

# Estimating reciprocal ratios

![center](images/reciprocal-ratio.png) -->
