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

# Comparative connectomics: methods and applications

<br>

<div class="columns">
<div>

## Benjamin D. Pedigo
(he/him)
[NeuroData lab](https://neurodata.io/)
Johns Hopkins University - Biomedical Engineering


![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [bpedigo@jhu.edu](mailto:bpedigo@jhu.edu)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>
<div>

### These slides at: 

[bdpedigo.github.io/talks/si.html](https://bdpedigo.github.io/talks/si.html)
<!-- ![](./../../images/princeton-slides-qr.png) -->

</div>
</div>

---

# Connectomes: maps of neural wiring

![center h:500](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-1.png)

<!-- _footer: Images from brain-map.org, SciDraw -->

---

# Goal: linking connectivity to other phenotypes

![center h:500](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-2.png)

<!-- _footer: Images from brain-map.org, SciDraw -->

---

# Goal: linking connectivity to other phenotypes

![center h:500](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-3.png)

<!-- _footer: Images from brain-map.org, SciDraw -->


---

# Goal: linking connectivity to other phenotypes

![center h:500](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-4.png)

<!-- _footer: Images from brain-map.org, SciDraw -->

---

# Goal: linking connectivity to other phenotypes

![center h:500](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-5.png)

<!-- _footer: Images from brain-map.org, SciDraw -->

--- 
# Comparative connectomics

<div class="columns">
<div>

#### How does a neuron's connectivity affect responses?

![center h:330](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/behave-example.png)

</div>
<div>

#### How does connectivity change during development?

![center h:280](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/dev-example.png)

</div>
</div>

#### Requires methods of comparing connectivity within and between connectomes

<!-- - explain how it could help things 
- Give some examples as they fit in to Allen institute work and what I'd want to do? 
- (reach) try to tie in function... 
- goals: 
  - statistically valid 
  - scaleable / easy to use
  - neuroscientifically interesting...  -->

---

# Larval *Drosophila* as a model system

<div class="columns">
<div>

## Genetics

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/eschbach-lines.png)

</div>
<div>

## Activity

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/activity.png)

</div>
<div>

## Behavior

<div class="columns">
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/behavior-quant.png)

</div>
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/behavior-traces.png)


</div>
</div>

</div>
</div>

<style scoped>
p {
  font-size: 20px
}
</style>

<div class="columns">
<div>

Eschbach et al. Nat. Neuro (2020)

</div>
<div>


Eschbach & Zlatic Curr. Op. Neurobio. (2020)

</div>
<div>

Klein et al. bioRxiv (2021)

Almeida-Carvalho et al. J. Experimental Bio. (2017)

</div>
</div>



---

# Larval _Drosophila_ brain connectome 

<style scoped>
p {
  justify-content: center;
  text-align: center;
  padding-top: 0px;
  margin-top: 0px;
}
</style> 

<div class="columns">
<div>

![h:400 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/Figure1-brain-render.png)

~3k neurons, ~550K synaptic sites
Both hemispheres

</div>
<div>

![h:450](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/show_data/adjacencies.png)

</div>
</div>

<!-- _footer: Winding, Pedigo et al. Science (2023) -->

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/paper-big-overview.png)

<!-- _footer: Winding, Pedigo et al. Science (2023) -->

--- 

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

# Outline

- ### **Clustering the larval brain by connectivity**
- ### Connectome comparison via network hypothesis testing
- ### Pairing neurons across connectomes via graph matching
- ### Future work

<!-- ---

# Analyzing the larval brain connecome
- Characterized flow of information (i.e. sorting neurons from sensory to descending)
- Examined routes of hemisphere integration, sensory integration, and feedback
- **Grouped neurons into "connectotypes"** -->

<!-- ---

# High-level cell types (mostly based on function) 

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/Figure1-cell-classes.png)

![h:200 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/io.png)

_footer: Winding, Pedigo et al. Science (2023) -->

---

# Neurons clustered by connectivity 

<!-- Where to stop splitting? -->

<!-- ![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/bar-dendrogram-wide.svg) -->

<div class="columns">
<div>

![h:475](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/dendrogram-adjacency.png)

</div>
<div>

- Used a variation on spectral clustering
- How many clusters to include?

</div>
</div>



<!-- ![center w:700](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/cell-type-labels-legend.png) -->

<!-- _footer: Winding, Pedigo et al. Science (2023) -->

---

# Stochastic block model

<div class="columns">
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_explain.png)

</div>
<div>

- Each node $i$ is assigned to a group, $\tau_{i}$
- $B$ is a matrix of connection probabilities between groups
- Edges generated independently according to these probabilities: 
  - $A_{ij} \sim Bernoulli(B_{\tau_{i} \tau_{j}})$

</div>
</div>

---
# Using models to evaluate candidate groupings
<!-- TODO: (2) diagram/describe SBM cross validation -->

<!-- ![center h:550](../../images/lik-by-n_params-blind.png) -->

<div class="columns">
<div>

<!-- - Clustering nodes corresponds with inferring groups in a stochastic block model (DCSBM) -->
- How well do these models generalize to the other side of the brain (let alone the next maggot)?

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/cross-val-explain.png)

</div>
<div>

![center h:550](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/sbm-swap-arrows.png)

</div>
</div>


---

<!-- Say something here about tieing this into comparing datasets in general -->

# Bilateral symmetry

> "This brain is bilaterally symmetric."

> "What does that even mean? And how would we know if it wasn't?"

<!-- ![bg center blur:3px opacity:20%](./../../../results/figs/background/background.svg) -->
<!-- ![bg opacity:.6 95%](./../../../results/figs/plot_side_layouts/2_network_layout.png) -->

<style scoped>
h2 {
    justify-content: center;
    text-align: center;
}
</style>

## Are the <span style="color: var(--left)"> left </span> and <span style="color: var(--right)"> right </span> sides of this connectome <p> </p> *different*?

--- 

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

# Outline

- ### Clustering the larval brain by connectivity
- ### **Connectome comparison via network hypothesis testing**
- ### Pairing neurons across connectomes via graph matching
- ### Future work

---
# Testing for differences

<div class="columns">
<div>

### Are these two populations different?

![center h:250](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/two_sample_testing/2_sample_real_line_wide.svg)


&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;$\color{#66c2a5} Y^{(1)} \sim F^{(1)} \quad \color{#fc8d62} Y^{(2)} \sim F^{(2)}$

<div class='center'>

<!-- &nbsp; &nbsp; $\color{#66c2a5} Y^{(1)} \sim F^{(1)}$ $\color{#fc8d62} Y^{(2)} \sim F^{(2)}$ -->
$H_0: \color{#66c2a5} F^{(1)} \color{black} = \color{#fc8d62} F^{(2)}$ vs. $H_A: \color{#66c2a5} F^{(1)} \color{black} \neq \color{#fc8d62} F^{(2)}$

</div>


</div>
<div>

### Are these two *networks* different?

![center h:250](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/show_data/2_network_layout.png)


&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; $\color{#66c2a5} A^{(L)} \sim F^{(L)} \quad \quad \color{#fc8d62} A^{(R)} \sim F^{(R)}$

<div class='center'>

$H_0: \color{#66c2a5} F^{(L)} \color{black} = \color{#fc8d62}F^{(R)}$ 
vs. 
$H_A: \color{#66c2a5} F^{(L)} \color{black} \neq  \color{#fc8d62} F^{(R)}$

</div>

</div>
</div>

---
# Assumptions
- Know the direction of synapses, so network is *directed*
- Consider networks to be *unweighted*
- Consider the <span style='color: var(--left)'> left $\rightarrow$ left </span> and <span style='color: var(--right)'> right $\rightarrow$ right </span> (*ipsilateral*) connections
- Not going to assume any nodes are matched
![center h:200](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/unmatched_vs_matched/unmatched_vs_matched.svg)
- If $F$ is again a stochastic block model, then...


---
# Connection probabilities between groups

<style scoped>
    .columns {
        display: grid;
        grid-template-columns: 1fr 2fr;
        gap: 0rem;
    }
</style>


<div class="columns">
<div>

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/Figure1-cell-classes-vertical.png)

</div>
<div>


![center w:700](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_clean.svg)

</div>
</div>

<!-- _footer: Winding, Pedigo et al. Science (2023), Pedigo et al. eLife (2023) -->


--- 
# Detect differences in group connection probabilities

<div class="columns">
<div>

<div class='center'>

$H_0: \color{#66c2a5}B^{(L)}_{kl} \color{black} = \color{#fc8d62}B^{(R)}_{kl}$ 

</div>

![center h:425](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_pvalues_unlabeled.svg)

</div>
<div>

- 7 group-to-group connections are significantly different (after multiple comparisons correction)
- Overall test (comparing all blocks):<br>$H_0: \color{#66c2a5}B^{(L)} \color{black} = \color{#fc8d62}B^{(R)}$<br>p-value $<10^{-7}$

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2023) -->

---
# An overall difference in density
<div class="columns">
<div>

- For significant comparisons, probabilities on right side are higher
- Even network densities are different<br>(1-block/Erdos-Renyi model)
- Maybe the right is just a "scaled up" version of the left?
   - $H_0: \color{#66c2a5}B^{(L)} \color{black}  = c \color{#fc8d62}B^{(R)}$  
  where $c$ is a density-adjusting constant, $\frac{\color{#66c2a5} p^{(L)}}{\color{#fc8d62} p^{(R)}}$

</div>
<div>

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/significant_p_comparison.svg)

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2023) -->

---
# After adjusting for density, differences are in KCs

<div class="columns">
<div>

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/adjusted_methods_explain.svg)

</div>
<div>

![h:450](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/sbm_pvalues_unlabeled.svg)

<style scoped>
p {
    justify-content: center;
    text-align: center;
}
</style>

Overall p-value: $<10^{-2}$

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2023) -->

---
# To sum up...

> "This brain is bilaterally symmetric."

Depends on what you mean...

<div class="columns">
<div>

#### With Kenyon cells
|   Model   |                       $H_0$ (vs. $H_A \neq$)                       |    p-value    |
| :-------: | :----------------------------------------------------------------: | :-----------: |
|  **ER**   |  $\color{#66c2a5} p^{(L)} \color{black} = \color{#fc8d62}p^{(R)}$  | ${<}10^{-23}$ |
|  **SBM**  | $\color{#66c2a5} B^{(L)} \color{black} = \color{#fc8d62} B^{(R)}$  | ${<}10^{-7}$  |
| **daSBM** | $\color{#66c2a5}B^{(L)} \color{black}  = c \color{#fc8d62}B^{(R)}$ | ${<}10^{-2}$  |


</div>
<div>

#### Without Kenyon cells
|   Model   |                       $H_0$ (vs. $H_A \neq$)                       |    p-value     |
| :-------: | :----------------------------------------------------------------: | :------------: |
|  **ER**   |  $\color{#66c2a5} p^{(L)} \color{black} = \color{#fc8d62}p^{(R)}$  | ${<}10^{-26}$  |
|  **SBM**  | $\color{#66c2a5} B^{(L)} \color{black} = \color{#fc8d62} B^{(R)}$  |  ${<}10^{-2}$  |
| **daSBM** | $\color{#66c2a5}B^{(L)} \color{black}  = c \color{#fc8d62}B^{(R)}$ | $\approx 0.60$ |

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2023) -->

--- 

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)


# Outline

- ### Clustering the larval brain by connectivity
- ### Connectome comparison via network hypothesis testing
- ### **Pairing neurons across connectomes via graph matching**
- ### Future work

---

# Bilaterally homologous neuron pairs 

<div class="columns-br">
<div>

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/mbon-expression-crop.jpg)

</div>
<div>

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/bilateral-pairs.png)


</div>
</div>

<!-- _footer: Eschbach et al. eLife (2021), Winding, Pedigo et al. Science (2023) -->

--- 
# How can we pair on connectivity?

<div class="columns-bl">
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/network-matching-explanation.svg)

</div>
<div>

$\min_{P \in \mathcal{P}} \underbrace{\|A_1 - \overbrace{PA_2P^T}^{\text{reordered } A_2}\|_F^2}_{\text{distance between adj. mats.}}$

where $\mathcal{P}$ is the set of permutation matrices

</div>
</div>


---
# From graph matching to bisected graph matching

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/explain-bgm.svg)

We generalized a state-of-the-art GM algorithm to solve BGM!

<!-- _footer: Pedigo et al. Network Neuroscience (2022), Vogelstein et al. PLOS One (2015)-->

--- 
# Contralateral connections aid matching!

![center h:550](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/match_accuracy_comparison.svg)

<!-- _footer: Pedigo et al. Network Neuroscience (2022) -->

---

# Performance improvement on the full brain
![center](https://raw.githubusercontent.com/neurodata/bgm/main/docs/images/matching_accuracy_upset.svg)

<!-- _footer: Pedigo et al. Network Neuroscience (2022), Pantazis et al. Applied Network Science (2022) -->

---
# Open source tools

<div class="columns">
<div>

![h:200](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/graspologic_svg.svg)


[![h:40](https://pepy.tech/badge/graspologic)](https://pepy.tech/project/graspologic)  [![h:40](https://img.shields.io/github/stars/microsoft/graspologic?style=social)](https://github.com/microsoft/graspologic)


[github.com/microsoft/graspologic](https://github.com/microsoft/graspologic)

</div>
<div>

## Related publications

[Chung, Pedigo et al. JMLR (2019)](https://jmlr.org/papers/v20/19-490.html)

[Vogelstein et al. Curr. Opin. Neurobio. (2019)](https://www.sciencedirect.com/science/article/abs/pii/S0959438818301430?via%3Dihub)

[Chung et al. Annual Review of Stats and Its Application (2021)](https://www.annualreviews.org/doi/abs/10.1146/annurev-statistics-042720-023234)


</div>
</div>

--- 

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

# Outline

- ### Clustering the larval brain by connectivity
- ### Connectome comparison via network hypothesis testing
- ### Pairing neurons across connectomes via graph matching
- ### **Future work**

---
# Future work

- Develop and apply methods for comparing multimodal connectomics datasets, e.g.
  - Across cortical regions
  - Across disease states
- Relate differences in connectivity to differences in function, e.g.
  - What differences in wiring for a neuron are predictive of function?

<!-- ---
# How do wiring rules generalize across regions of cortex? To new species? Disease states?

- Requires knowing *what* to compare...
  - E.g. how to find the same cell type in non-human primate and mouse
- And *how* to compare...
  - E.g. addressing some of the limitations of current state of the art -->

<!-- ---
i love comparative
excited to see how these methods could, with allen data, help understand how differences in connectivity relate to  -->

<!-- ---
# Techniques can be applied to light level data as well...
 -->

<!-- ## Methods, e.g.
- Improve methods for mapping between datasets
- Improve methods for evaluating differences between datasets

## Applications, e.g. 
- How do wiring rules generalize across regions of cortex -->

---
# Example: a structure-function relationship in the larva

![center](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/draft-maggot-multiomics.png)

### Behavior probabilities significantly related to projections to brain outputs

RV coefficient: 0.12, p-value: 0.0044
Distance correlation: 0.067, p-value: 0.0087

<!-- _footer: Work w/ L. Venkatasubramanian, C. Barré, JB Masson, C. Priebe, M. Zlatic -->

<!-- ---
# Mapping representations between modalities
- Give SegCLR example, how well does it generalize -->

<!-- ---
# Stereotypy of wiring rules across cortical regions, modalities
- Naively, an application of some form of network testing
- In reality, likely issues with differences in samples that need to be accounted for -->

<!-- ---
# Mapping between behavior/response and connectivity -->

---

# How does this relate to work at Allen?

---

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)

## References

[Winding, M. & Pedigo, B.D. et al. The connectome of an insect brain. Science (2023).](https://www.science.org/doi/10.1126/science.add9330)

[Pedigo, B. D. et al. Generative network modeling reveals quantitative definitions of bilateral symmetry exhibited by a whole insect brain connectome. eLife (2023).](https://elifesciences.org/articles/83739)

[Pedigo, B. D. et al. Bisected graph matching improves automated pairing of bilaterally homologous neurons from connectomes. Network Neuroscience (2022).](https://direct.mit.edu/netn/article/doi/10.1162/netn_a_00287/113527/Bisected-graph-matching-improves-automated-pairing)

## Code

<div class="columns">
<div>


[github.com/neurodata/maggot_models](github.com/neurodata/maggot_models)

[github.com/neurodata/bilateral-connectome](github.com/neurodata/bilateral-connectome)

[github.com/neurodata/bgm](github.com/neurodata/bgm)

</div>
</div>


--- 

![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)


# Acknowledgements

#### Team

<style scoped> 

p {
    font-size: 24px;
}
</style>


<div class='minipanels'>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/michael_winding.png)
Michael Winding

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/mike-powell.jpg)
Mike Powell

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/bridgeford.jpg)
Eric Bridgeford

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/ali_saad_eldin.jpeg)
Ali <br> Saad-Eldin

</div>


<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/marta_zlatic.jpeg)
Marta Zlatic

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/albert_cardona.jpeg)
Albert Cardona

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/priebe_carey.jpg)
Carey Priebe

</div>

<div>

![person](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/people/vogelstein_joshua.jpg)
Joshua Vogelstein

</div>

</div>

Tracers who contributed to larva connectome, Lalanti Venkatasubramanian, Chloé Barré, Jean-Baptiste Masson, Heather Patsolic, Youngser Park, NeuroData lab, Microsoft Research

Figures from Scidraw (A. Bates, V. Kumar, E. Tyler, L. Kravitz, H. Robinson, E. Thompson), brain-map.org

#### Funding
NSF Graduate Research Fellowship (B.D.P.), NSF CAREER Award (J.T.V.), NSF NeuroNex Award (J.T.V and C.E.P.), NIH BRAIN Initiative (J.T.V.)

---


![bg center blur:3px opacity:20%](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/background.svg)


# Questions?

<div class="columns">
<div>

### Benjamin D. Pedigo
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/email.png) [bpedigo@jhu.edu](mailto:bpedigo@jhu.edu)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo](https://github.com/bdpedigo)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod](https://twitter.com/bpedigod)
![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/)

</div>
<div>

### These slides at:
[bdpedigo.github.io/talks/si.html](https://bdpedigo.github.io/talks/si.html)

</div>
</div>


---

# Extras

---

# Mapping a larval _Drosophila_ brain connectome 

![h:500 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/FigureS1-reconstruction.png)

<!-- _footer: Winding, Pedigo et al. Science (2022), Ohyama et al. Nature (2015)-->

---



---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/revamp_sbm_methods_sim/tippett_null_cdf.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/revamp_sbm_methods_sim/relative_power.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/revamp_sbm_methods_sim/tippett_power_matrix.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/revamp_sbm_methods_sim/null_distributions.svg)

---

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/revamp_sbm_methods_sim/tippett_sim_composite.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/single_subgraph_power/power_heatmap_contours.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/er_unmatched_test/er_density.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/er_unmatched_test/er_methods.svg)


---

![center h:600](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/kc_minus/kc_minus_composite.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_block_power/sbm_pvalues.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_block_power/n_possible_by_block.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_block_power/empirical_power_by_block.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/matched_vs_unmatched_sims/er_power_comparison.svg)

---

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/thresholding_methods.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/input_proportion_histogram.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/input_threshold_pvalues_legend.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_threshold_pvalues.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_threshold_pvalues_legend.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/weight_notions.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_weight_histogram.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/probs_uncorrected.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_methods_explain.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_pvalues_unlabeled.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_simple_methods.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/fisher_sbm_pvalues.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_explain.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/significant_p_comparison.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/probs_scatter.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_composite.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/group_counts.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_pvalues.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/adjusted_methods_explain.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/sbm_pvalues.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/adjusted_sbm_composite.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/sbm_pvalues_unlabeled.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/resampled_pvalues_distributions.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/resampled_pvalues_distribution.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/adjusted_sbm_unmatched_test/edge_removal_methods.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/two_sample_testing/2_sample_real_line_wide.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/two_sample_testing/2_sample_real_line.svg)




---
# Erdos-Renyi model
<!-- Timing: ~10 -->

- All edges are independent
- All edges generated with the same probability, $p$

![center](../../../results/figs/er_unmatched_test/er_explain.svg)


---
# Detect a difference in density

<div class="columns">
<div>

![center h:500](./../../../results/figs/er_unmatched_test/er_methods.svg)


</div>
<div>

![center h:400](../../../results/figs/er_unmatched_test/er_density.svg)

<style scoped>
p {
  justify-content: center;
  text-align: center;
}
</style>

p-value < $10^{-22}$


</div>
</div>

<!-- _footer: Pedigo et al. eLife (2022) -->

--- 
# Group connection test

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_methods_explain.svg)

<!-- _footer: Pedigo et al. eLife (2023) -->

---
skip

---

# High level (mostly anatomical) cell types

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/Figure1-cell-classes.png)

![h:200 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/io.png)

<!-- _footer: Winding, Pedigo et al. Science (2023) -->

---

# Sorting the network

![h:400 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-fdback-improved-explain.png)

<!-- _footer: Carmel et al. IEEE Vis. and Comp. Graphics (2004), Burkard et al. Assignment Problems (2009)  -->

---
# Quantifying high-level "feedforward/feedback"

<div class="columns-br">
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-fdbk.png)

</div>
<div>

<!-- ![h:300 center](./../../images/fig2f.png) -->

<div class="columns">
<div>


![h:300 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-fdback-cropped.png) 
![h:50 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-legend.png)

</div>
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/rank-hist.svg)

</div>
</div>


</div>
</div>

<!-- _footer: Winding, Pedigo et al. Science (2023) -->

--- 

# Morphology enables splitting axons/dendrites 

<div class="columns">
<div>

![h:500 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/fig2c-half.png)

<!-- ![h:500 center](../../images/fig2a.png) -->

</div>
<div>

![](../../../../../bilateral/bilateral-connectome/docs/images/ffwd-fdback.svg)
![h:50](../../../../../bilateral/bilateral-connectome/docs/images/ffwd-legend.png)

</div>
</div>

---
# Spectral embedding

<div class="columns">
<div>

- Spectral decomposition of the adjacency matrix (or Laplacian)
- Clustering on this representation is a consistent estimator of block model labels

</div>
<div>

![h:400 center](../../../../../bilateral/bilateral-connectome/docs/images/spec-clust.png)

</div>
</div>

---
# Examining the effect of edge weights

<div class="columns">
<div>

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/weight_notions.svg)

</div>
<div>

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/thresholding_methods.png)

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2023) -->

---

# Even high synapse count networks show asymmetry

<div class="columns">
<div>

<span> </span>
<span> </span>
<span> </span>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/synapse-count.png)

</div>
<div>

![h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_threshold_pvalues_legend.svg)

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2022) -->

---

# High input percentage networks show no asymmetry

<!-- <div class='columns'>
<div>

## Synapse count thresholding  -->

<!-- ![center h:400](./../../../results/figs/thresholding_tests/synapse_threshold_pvalues.svg) -->

<!-- </div>
<div>

## Input proportion thresholding -->
<!-- 
</div>
</div> -->

<div class="columns">
<div>


<span> </span>
<span> </span>
<span> </span>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/input-prop.png)

</div>
<div>

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/input_threshold_pvalues_legend.svg)

</div>
</div>

<!-- _footer: Pedigo et al. eLife (2022) -->



<!-- _footer: Winding, Pedigo et al. Science (2023) -->

<!-- ---

# This split induces 4 graphs (or layers)

<div class="columns">
<div>

![h:500](./../../images/fig2d.png)

</div>
<div>

![h:200](./../../images/fig2e.png)

</div>
</div> -->

<!-- _footer: Winding, Pedigo et al. bioRxiv (2022) -->


<!-- # What are these different "channels" doing?

<div class="columns">
<div>

![h:500](./../../images/figS5e.png)

</div>
<div>


</div>
</div> -->

<!-- _footer: Winding, Pedigo et al. bioRxiv (2022) -->

<!--
---

# Sorting the network

![h:400 center](./../../images/flow-method-explain.png)
-->

<!-- ---

# Comparing independently sorted "channels"

![bg right:68% h:650](./../../images/figs6.png) -->

<!-- _footer: Winding, Pedigo et al. bioRxiv (2022) -->


<!-- --- 
# Edge reciprocity

![h:400 center](./../../images/fig2h-reciprocity.png)

_footer: Winding, Pedigo et al. bioRxiv (2022) -->



---
# Many ways to try to improve on this...

- Edge types allow for "multilayer" graph matching
- Partial knowledge of the matching (seeds)
- Morphology (e.g. NBLAST)

<!-- <style scoped>
h1, h2 {
    padding-top: 140px;
    justify-content: center;
    text-align: center;
}
</style> -->

# Thus far, we've not used the contralateral connections

## These are about 1/3 of the edges in the brain!

<!-- _footer: Pantazis et al. Applied Network Science (2022), Fishkind et al. Pattern Recognition (2019) -->

---
# How do we do graph matching?

- Relax the problem to a continuos space
  - Convex hull of permutation matrices
- Minimize a linear approximation of objective function (repeat)
- Project back to the closest permutation matrix

<!-- _footer: Vogelstein et al. PLOS One (2015) -->


---
# Matching (by connectivity only) performs fairly well

![center h:450](./../../_build/html/_images/left-pair-predictions.svg)


<style scoped>
p {
    justify-content: center;
    text-align: center;
}
</style>

With "vanilla" graph matching: ~80% correct (according to expert annotator)


---
# Testing for "stereotypy" in edge structure

Is matching stronger than expected under some model of independent networks?

<div class="columns">
<div>

![](../../images/kc-stereotypy-diagram.svg)

</div>
<div>

![](../../images/kc_alignment_dist.svg)

</div>
</div>

_footer: Eichler et al. Nature (2017), Fishkind et al. Applied Network Science (2021)


---

# Comparative connectomics

![center h:350](../../../../../bilateral/bilateral-connectome/docs/images/connect-diagram.png)

- Map connectomes from related individuals/organisms which may differ in feature $X$
- Compare connectomes
- Understand how $X$ {affects, is affected by, is associated with} connectome structure

---

<div class="columns">
<div>

![](../../../../../bilateral/bilateral-connectome/docs/images/behavior-cc.png)

> Comparative connectomics across experience, sex and species is a key next step.

</div>
<div>

![](../../../../../bilateral/bilateral-connectome/docs/images/evo-cc.png)

> With comparative connectomics, the search for neural circuit architectures common across species or independently converged into an optimal layout is now possible.

</div>
</div>


---

# Why is comparative connectomics hard?

- Collecting the data is still a large effort...

- But how do we even compare connectomes once we have them?

## How do we know whether a proposed experiment could even *hope* to answer our questions? How **powerful** is comparative connectomics?


<!-- - ~~Data are networks~~
  - Data are networks with rich attributes
- Data will always have noise
  - "Experimental noise"
  - "Biological noise"
- Data are big (and getting bigger) -->
 



---

# A hypothetical difference we want to detect...

![center h:300](../../../../../bilateral/bilateral-connectome/docs/images/perturbation-diagram.png)

- Start from some subgraph in the connectome, $A$
- Perturb a copy of it, $B$ (add edges)
- Test for differences between $A$ and $B$

---
# Pairs facilitate more powerful tests

![center](./../../../results/figs/matched_vs_unmatched_sims_pn_lhn/er_power_comparison.svg)


--- 

<!-- ### Cluster morphology  -->

![bg h:750 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/all-morpho-plot-clustering=dc_level_7_n_components=10_min_split=32-discrim=True-wide.png)


--- 

# Cluster morphology 

![bg opacity:25% h:750 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/all-morpho-plot-clustering=dc_level_7_n_components=10_min_split=32-discrim=True-wide.png)

![h:300 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/intra-cluster-morpho.png)

## Discriminability:
$P[$ within cluster NBLAST sim. $>$ between cluster NBLAST sim. $] \approx 0.81$ 

<!-- _footer: Costa et al. Neuron (2016), Bridgeford et al. PLOS Comp. Bio. (2021)-->
