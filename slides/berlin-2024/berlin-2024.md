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

# Measurement design in connectomics

<br>

<div class="columns">
<div>

![h:250 center](images/optimizing-title.png)

</div>
<div>

> Would you rather have lots of noisy connectivity measurements or a little bit of high-quality data?

There exists regimes where you'd prefer either, _depending on the question_

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

<!-- _footer: MICrONS Consortium et al. *bioRxiv* (2023), Schneider-Mizell et al. *bioRxiv* (2023),  Schneider-Mizell et al. *bioRxiv* (2023) -->

---

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

<!-- _footer: Schneider-Mizell et al. *bioRxiv* (2023) -->

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

![bg center fit blur:5px opacity:40%](./images/all_edits_by_time_with_plots-target_id=271886.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](images/cell-type-legend.png)

</div>

<!-- <div style="position: absolute; bottom: 20px; right: 60px;">

![h:280](images/white.png)

</div> -->

![center h:600](images/distance-transparent.png)

---

![bg center fit](./images/all_edits_by_time_with_plots-target_id=271886.gif)

<div style="position: absolute; top: 50px; right: 50px;">

![h:50](images/cell-type-legend.png)

</div>

---

# Cell-type specific connectivity converged quickly

![h:500 center](./images/line-stack.gif)

---



---

# Counterfactual games

- So far, have looked at how neurons changed over the course of proofreading in actuality, but this is a somewhat arbitrary historical ordering
- Can replay edits (or not) according to alternative schemes
- E.g. what if we only had half the proofreading resources - how should we allocate them?

---

# How would clustering change with different proofreading schemes?

![center ](images/ari-vs-merges.png)

---

# Impactful edits are more often near the soma

![center](images/distance_vs_impact.png)


---

<!-- # (1) "sloppy" proofreading?

![](images/half_edit_heatmaps.png) -->

<!-- ---

# (2) what if I omit individual edits? (importance)

![h:500 center](images/edit_dropout_importance_root_id=864691135213953920.png) -->

<!-- ---

# (3) which neurons are "good enough"?

![h:500 center](images/closeness-by-n_outputs.png) -->

---

# Summary

<!-- - Worth understanding whether most neurons look like they have converged -->

- Monitoring proofreading with specific analyses/metrics in mind could help us decide how to allocate resources
<!-- - Counterfactual replay of various edit schemes can help understand how alternative proofreading strategies might affect downstream analyses -->
<!-- - Analyses could be applied to other datasets or even to analyze how design of automated proofreading systems affects conclusions -->

---

# Acknowledgements

<style scoped> 
p {
    font-size: 10px;
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

**PM**
Lynne Becker
Florence D'Orazi
Sarah Naylor
Shelby Suckow
David Vumbaco
Susan Sunkin

</div>
<div>

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

**MPE**
Jay Borseth
Collin Farrell
And others

</div>
<div>

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
