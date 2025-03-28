---
marp: true
theme: slides
size: 16:9
paginate: true

---

<style>
section::after {
    content: attr(data-marpit-pagination) '/38';
}
</style>

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
NSF Graduate Research Fellow
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

#### How does a neuron's connectivity affect elicited behaviors?

![center h:330](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/behave-example.png)

</div>
<div>

#### How does connectivity change during development?

![center h:280](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/dev-example.png)

</div>
</div>

#### Requires methods of comparing connectivity within and between connectomes

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


---

# Neurons clustered by connectivity 


<div class="columns">
<div>

![h:475](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/dendrogram-adjacency.png)

</div>
<div>

- Used a variation on spectral clustering
- How many clusters to include?

</div>
</div>


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

<div class="columns">
<div>


- How well do these models generalize to the other side of the brain (let alone the next maggot)?

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/cross-val-explain.png)

</div>
<div>

![center h:520](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/sbm-swap-arrows.png)

</div>
</div>


---

# Bilateral symmetry

> "This brain is bilaterally symmetric."

> "What does that even mean? And how would we know if it wasn't?"

<style scoped>
h2 {
    justify-content: center;
    text-align: center;
}
</style>

## Are the <span style="color: var(--left)"> left </span> and <span style="color: var(--right)"> right </span> sides of this connectome <p> </p> *different*?

- Hints at how sterotyped wiring might be
- Testbed for connectome comparison methods

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
- Not assuming any nodes are matched:
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

- Overall test (comparing all blocks):<br>$H_0: \color{#66c2a5}B^{(L)} \color{black} = \color{#fc8d62}B^{(R)}$<br>p-value $<10^{-7}$

- 7 group-to-group connections are significantly different (after multiple comparisons correction)

</div>
<div>

<div class='center'>

$H_0: \color{#66c2a5}B^{(L)}_{kl} \color{black} = \color{#fc8d62}B^{(R)}_{kl}$ 

</div>

![center h:425](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_uncorrected_pvalues_unlabeled.svg)


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
   $c$ is a density-adjusting constant
  
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

![center h:520](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/match_accuracy_comparison.svg)

<!-- _footer: Pedigo et al. Network Neuroscience (2022) -->

---

# Performance improvement on the full brain

<div class="columns-br">
<div>

![center](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connection-types.png)

</div>
<div>

![center](https://raw.githubusercontent.com/neurodata/bgm/main/docs/images/matching_accuracy_upset.svg)

</div>
</div>

<!-- _footer: Pedigo et al. Network Neuroscience (2022), Winding, Pedigo et al. Science (2023), Pantazis et al. Applied Network Science (2022) -->

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

<!-- 
As mentioned, interested in leveraging this work on how we can compare connectomes to find links to these various other phenotypes. 

This is what makes the work being done at the Allen institute and UW so exciting to me; given that you all are not just measuring connectomes, but also many other modalities of data.

I’d like to give an example of how I’m approaching this kind of question in the larva, and how I think with some development, these approaches would be relevant to apply to the allen institute data. 

 -->

![bg h:700](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/connect-diagram-5.png)

---

<!-- 
Evidence that characterizing variability in connectivity (in this case, specific projections to brain output neurons), can be related to differences in behavioral outputs
 -->

# A structure-function relationship in the larva

![center](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/draft-maggot-multiomics.png)

### Behavior probabilities significantly related to projections to brain outputs

RV coefficient: 0.12, p-value: 0.0044
Distance correlation: 0.067, p-value: 0.0087

<!-- _footer: Work w/ L. Venkatasubramanian, C. Barré, JB Masson, C. Priebe, M. Zlatic -->

---

<!-- As an example of how this kind of approach would be relevant at Allen, take for example the recent work from the microns consortium to map out connections in the visual cortex of a mouse. This dataset is already revealing principles of how cortical circuits are wired, for instance in this recent paper investigating the structure of inhibition onto 

I am interested in using our network testing methods to see whether these rules hold, say, for other subvolumes in the same region of visual cortex, and in particular, whether they are different in another visual region. This would be a natural application of my work on model-based comparison of neural wiring rules.

Methodologically, answering these questions would likely involve incorporating more biological detail into these model-based descriptions of connectivity, for instance incorporating wiring rules based on space and sub-cellular compartments. I’d be excited to work with both allen institute and UW researchers on these kinds of extensions. 
 -->

# Example: do wiring rules generalize across region?

<div class="columns">
<div>

<!-- ![h:350](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/microns-volume.png) -->

![center](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/casey-paper-volume.png)

![center h:290](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/casey-paper-wiring-rules.png)

</div>
<div>

- Application of model-based network comparison
- Would likely require extensions of our simple models to account for details of wiring in cortex!

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/casey-paper-explain.png)

</div>
</div>

<!-- _footer: MICrONS Consortium et al. bioRxiv (2021), Schneider-Mizell et al. bioRxiv (2023) -->

---

<!-- Finally, as I’ve mentioned, i think the reason to do all this careful study of wiring rules is ultimately to see how this impacts function, which is part of what makes me fascinated by the microns data, where neural activity was also characterized for many neurons. 


I’m interested in 

trying to connect any variation we see in neural wiring rules to variation in aspects of neural activity, 

using some of the tools i mentioned for high dimensional independence testing in our work on the larva. -->

# ...and does any variation relate to function? 

![h:300 center](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/ding-overview.png)


<!-- _footer:  MICrONS Consortium et al. bioRxiv (2021), Ding, Fahey, Papadououlos et al. bioRxiv (2023)  -->

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

# Winding, Pedigo et al. Science (2023)

---

# Mapping a larval _Drosophila_ brain connectome 

![h:500 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/FigureS1-reconstruction.png)

<!-- _footer: Winding, Pedigo et al. Science (2023), Ohyama et al. Nature (2015)-->

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig1.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig2.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig3.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig4.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig5.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig6.png)

---

![center h:600](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/science-Fig7.png)


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

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-fdback.svg)
![h:50](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/ffwd-legend.png)

</div>
</div>

---
# Spectral embedding

<div class="columns">
<div>

- Spectral decomposition of the adjacency matrix (or Laplacian)

</div>
<div>

![h:400 center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/spec-clust.png)

</div>
</div>

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


---

# Pedigo et al. eLife (2023)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_methods_explain.svg)

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

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_block_power/n_possible_by_block.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_block_power/empirical_power_by_block.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/matched_vs_unmatched_sims/er_power_comparison.svg)

---

![center h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/thresholding_methods.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/weight_notions.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/input_threshold_pvalues_legend.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_threshold_pvalues_legend.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/input_proportion_histogram.svg)

---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/thresholding_tests/synapse_weight_histogram.svg)

---

![center h:600](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/probs_uncorrected.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/sbm_simple_methods.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/probs_scatter.svg)


---

![center](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_unmatched_test/group_counts.svg)




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

# Pedigo et al. Network Neuroscience (2022)


---
# How do we do graph matching?

- Relax the problem to a continuos space
  - Convex hull of permutation matrices
- Minimize a linear approximation of objective function (repeat)
- Project back to the closest permutation matrix

<!-- _footer: Vogelstein et al. PLOS One (2015) -->

---

# Algorithm

![](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/algo-bgm.png)

---

![h:500](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_matched_test/edge_scatter_matched.png)

Pearson's corr = 0.82

---

<div class="columns">
<div>

### Unpaired

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_matched_test/pvalue_heatmap_unpaired_matched.png)

</div>
<div>

### Paired 
![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/results/figs/sbm_matched_test/pvalue_heatmap_paired_matched.png)

</div>
</div>

---
# Testing for "stereotypy" in edge structure

Is matching stronger than expected under some model of independent networks?

<div class="columns">
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/kc-stereotypy-diagram.svg)

</div>
<div>

![](https://raw.githubusercontent.com/neurodata/bilateral-connectome/main/docs/images/kc_alignment_dist.svg)

</div>
</div>

<!-- _footer: Eichler et al. Nature (2017), Fishkind et al. Applied Network Science (2021) -->
