---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
---

<style>
a {
  position: fixed;
  /* border: 10px solid #73AD21; */
}
embed{
  border: 0px;
}
h1 {
  margin-bottom: 0px;
  padding-bottom: 5px;
}
section {
  --soma: rgb(0, 227, 255);
  --shaft: rgb(239, 230, 69);
  --spine: rgb(233, 53, 161);
  --legend: |
  <div style="font-size:16px">
  <span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
  <img src="./../../images/icons/sphere-dashed.svg" style="display: inline; position: relative; top: 2px"></img> vortex
  <img src="./../../images/icons/rect.svg" style="display: inline; position: relative; top: 2px"></img> model
  </div>;
}
img {
  display: inline;
  position: relative;
  top: 2px
}
</style>

<!-- _paginate: false -->
<!-- _backgroundImage: ../themes/aibs-backgrounds/blank.png -->

![bg opacity:0.6](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

<br>

# Mesh signatures

<div class="columns">
<div>

<br>
<br>
<br>
<br>
<br>
<br>
<br>

Ben Pedigo
(he/him)
Scientist I
Allen Institute for Brain Science
[ben.pedigo@alleninstitute.org](mailto:ben.pedigo@alleninstitute.org)

<div style='' >

<!-- ![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/github.png) [@bdpedigo (Github)](https://github.com/bdpedigo) -->
<!-- ![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/twitter.png) [@bpedigod (Twitter)](https://twitter.com/bpedigod) -->
<!-- ![icon](https://raw.githubusercontent.com/bdpedigo/talks/main/docs/images/icons/web.png) [bdpedigo.github.io](https://bdpedigo.github.io/) -->

</div>

</div>
<div>

</div>
</div>

---

# Outline

- **Motivation**
- Intuition for heat kernel signatures
- Computing heat kernel signatures
- Application to spine prediction
- Extensions

---

<!-- ---

# Morphological featurization of neuron morphology

- "Kernel" based: compare all $n$ neurons to all other $n-1$ neurons, build up a similarity/dissimilarity matrix
  - NBLAST
  - CAJAL
- Hand-crafted features:
  - IVSCC pipeline features
  - Nuclear features
- Learning-based:
  - GNNs on skeletons (Weis papers)
  - NEURD
  - SegCLR -->

<!-- ---

# Problem statement

## Current spine classifcations have remained unsatisfying -->

---

# Fine-scale morphological features

---

# NEURD classifies many spines as shaft

_Bethanny Danskin, Erika Neace, Rachael Swanstrom_

<div class="columns">
<div>

![center](./images/vortex_neurd_simple_confusion_matrix_normalized.svg)

</div>
<div>

Coverage: 66% of VORTEX compartment labels are in the NEURD table

</div>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/vortex_neurd/vortex_neurd_sample_meshes_0.svg" width="96%" height="600px" name="vortex_neurd_sample_meshes_0"></embed>

<a href="./images/vortex_neurd/vortex_neurd_sample_meshes_0.html" target="vortex_neurd_sample_meshes_0">
<img src="./../../images/icons/search.svg"></img>
</a>

</div>

<!-- _footer:  -->

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/vortex_neurd/vortex_neurd_sample_meshes_1.svg" width="96%" height="600px" name="vortex_neurd_sample_meshes_1"></embed>

<a href="./images/vortex_neurd/vortex_neurd_sample_meshes_1.html" target="vortex_neurd_sample_meshes_1">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/vortex_neurd/vortex_neurd_sample_meshes_2.svg" width="96%" height="600px" name="vortex_neurd_sample_meshes_2"></embed>

<a href="./images/vortex_neurd/vortex_neurd_sample_meshes_2.html" target="vortex_neurd_sample_meshes_2">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/vortex_neurd/vortex_neurd_sample_meshes_3.svg" width="96%" height="600px" name="vortex_neurd_sample_meshes_3"></embed>

<a href="./images/vortex_neurd/vortex_neurd_sample_meshes_3.html" target="vortex_neurd_sample_meshes_3">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/vortex_neurd/vortex_neurd_sample_meshes_4.svg" width="96%" height="600px" name="vortex_neurd_sample_meshes_4"></embed>

<a href="./images/vortex_neurd/vortex_neurd_sample_meshes_4.html" target="vortex_neurd_sample_meshes_4">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Outline

- Motivation
- **Intuition for heat kernel signatures**
- Computing heat kernel signatures
- Application to spine prediction
- Extensions

---

# Heat diffusion

Imagine placing a unit of heat at a point on a surface, watching how that heat diffuses

![](https://upload.wikimedia.org/wikipedia/commons/d/d9/Fundamental_solution_to_the_heat_equation.gif)

<!-- _footer: https://en.wikipedia.org/wiki/Heat_equation -->

---

![bg fit](./images/heat_diffusion_example.svg)

<!-- _backgroundImage: -->

---

# Tracking heat diffusion

<div class="columns">
<div>

![](./images/heat_diffusion_example.svg)

</div>
<div>

![](./images/heat_diffusion_curves.svg)

</div>
</div>

---

# Defining the heat kernel signature (HKS)

Let $k_{\tau}(x, y)$ be the amount of heat that diffuses from point $x$ to point $y$ after time $\tau$.

The authors then consider $k_{\tau}(x, x)$; in other words, how much heat is left at $x$ after some amount of time $\tau$.

Then, for some set of timescales $T = \{\tau_1, \tau_2, ... \tau_d\}$, the HKS for a node $x$ is

$$HKS(x) = [k_{\tau_1}(x,x), k_{\tau_2}(x,x), ..., k_{\tau_d}(x,x)]$$

<!-- _footer: Sun et al. (2008) -->

---

# Intuition for multiscale matching

<div class="columns">
<div>

![](./images/hks_paper_synthetic_example.png)

</div>
<div>

<!-- Do a scoped resizing of the font here -->

> Since all four points have isometric neighborhoods at small scales, their HKS’s are the same for small $t$’s ($< t_1$). Point 1 and point 3 have isometric neighborhoods at middle scales and thus their HKS’s coincide even for middle $t$’s ($[t_1,t_3]$), as do the HKS’s of point 2 and point 4 ($[t_1,t_2]$). The signatures of points 3 and 4 are similar for large $t$’s since ... their neighborhoods at large scale are close.

</div>
</div>

<!-- _footer: Sun et al., _Eurographics_ (2008) -->

---

# Clustering on heat kernel signatures

<div class="columns">
<div>

![center](./images/hks_clustermap.png)

</div>
<div>

<div>
<embed src="./images/hks_clustered.svg" width="96%" height="500px" name="hks_clustered"></embed>

<a href="./images/hks_clustered.html" target="hks_clustered">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

</div>
</div>

---

# Outline

- Motivation
- Intuition for heat kernel signatures
- **Computing heat kernel signatures**
- Application to spine prediction
- Extensions

---

# Heat diffusion

Evolution of heat $u$ over time $t$ is governed by the heat equation:

$$\frac{\partial{u}}{\partial{t}} = \Delta u$$

where $\delta$ is the Laplacian (2nd derivative) operator.

Heat transferred from point $x$ to $y$ at time $t$ is given by the heat kernel $k_t(x,y)$:

$$k_t(x,y) = \sum_{i=0}^{\infty} e^{-\lambda_i t} \phi_i(x) \phi_i(y)$$

where $\lambda_i$ and $\phi_i$ are the eigenvalues and eigenvectors of the Laplacian operator.

**We just need these eigenvectors/eigenvalues to describe heat**

---

# Heat on a 1D grid

<div class="columns">
<div>

For a 1D grid,

![](./images/discrete_heat/1d_grid.svg)

the eigenvectors of the Laplacian are:

</div>
<div>

![](./images/discrete_heat/1d_eigenvectors.svg)

</div>
</div>

---

# Laplacian eigenvectors

<div class="columns">
<div>

### 1D grid

![](./images/discrete_heat/1d_eigenvectors.svg)

</div>
<div>

### 2D grid

![](./images/discrete_heat/plane_eigenvector_199.svg)

</div>
<div>

### Mesh

<!-- ![](./images/fastest-evec.html)
 -->

<embed src="./images/fastest-evec.html" width="100%" height="400px" style="border:0px"></embed>

</div>
</div>

---

# Computing the eigendecomposition

- :white_check_mark: Very sparse problem: power iteration methods/ARPACK are efficient
- :white_check_mark: Can truncate the eigendecomposition to get an approximate solution
- :x: Need $O(\text{Thousands})$ of eigenvectors to get resolution down to the scale of spines, mesh has $O(\text{Millions})$ of points
  - Was taking $\thicksim$ 1-3 Hours to compute eigendecomposition on a single neuron

---

# Improvement #1: band-by-band algorithm

Band-by-band algorithm of Vallet and Levy (2008):

- Use the "shift-invert" trick, do $\tilde{L} = L - \lambda_S I$ for some $\lambda_S$
  - Converts the problem to one where power iteration methods are efficient for that range of eigenvalues
- Compute eigenpairs (ARPACK)
- Compute contribution of each eigenpair to HKS, throw away
  - Memory efficient
- Compute a new $\lambda_S$, repeat until reach desired eigenvalue

<!--
<div class="columns">
<div>

> - Replace L with L - $\lambda_S$ I
> -

</div>
<div>


</div>
</div> -->

<!-- _footer: Vallet and Levy, _Eurographics_ (2008) -->

---

# Improvement #2: chunking

- Intuition: don't need low frequency information to distinguish local features
- Can break the mesh into pieces, compute the eigendecomposition on each chunk
- Use overlapping mesh chunking to minimize edge effects at borders

<div class="columns">
<div>

![](./images/show_mesh_splitting/submeshes.svg)

</div>
<div>

![](./images/show_mesh_splitting/submeshes_overlapped.svg)

</div>
</div>

---

# Timing

<!-- Need to profile more comprehensively, but,

~1-2 min to simplify mesh
~1-2 min to subdivide mesh
~1-4 min for (parallelized on 12 cores) eigendecomposition/HKS, longer for very big neurons -->

<div class="columns">
<div>

Per chunk

![center h:420](./images/timing/timing_n_vertices_vs_wall_time.svg)

</div>
<div>

Whole neuron

![center h:420](./images/timing/timing_n_vertices_vs_wall_time_per_root.svg)

</div>
</div>

$*$ Doesn't include mesh simplification/subdivision, adds $\thicksim 1-3$ minutes per neuron

---

# Outline

- Motivation
- Intuition for heat kernel signatures
- Computing heat kernel signatures
- **Application to spine prediction**
- Extensions

---

# Spine prediction

- Trained on dense spine labels for 6 neurons
  - _Bethanny Danskin, Erika Neace, Rachael Swanstrom_
- Trained on HKS features from the mesh point closest to synapse center point
- Used a simple random forest, didn't do much tuning or exploration here

---

# Random forrest, leave-on-neuron-out testing

<div class="columns">
<div>

![](./images/model_comparison/metrics-Heat-RF-NEURD.svg)

</div>
<div>

![](./images/model_comparison/metrics-Heat-RF.svg)

</div>
</div>

---

# Best neuron

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/model0/neuron_posterior_best.svg" width="96%" height="520px" name="neuron_posterior_best"></embed>

<a href="./images/model0/neuron_posterior_best.html" target="neuron_posterior_best">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Worst neuron

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg"></img> vortex
<img src="./../../images/icons/rect.svg"></img> model
</div>

<div>
<embed src="./images/model0/neuron_posterior_worst.svg" width="96%" height="520px" name="neuron_posterior_worst"></embed>

<a href="./images/model0/neuron_posterior_worst.html" target="neuron_posterior_worst">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: rgb(0, 227, 255);">soma</span> <span style="color: rgb(239, 230, 69);">shaft</span> <span style="color: rgb(233, 53, 161);">spine</span> 
<img src="./../../images/icons/sphere-dashed.svg" style="display: inline; position: relative; top: 2px"></img> vortex
<img src="./../../images/icons/rect.svg" style="display: inline; position: relative; top: 2px"></img> model
</div>

<div>
<embed src="./images/model0/incorrect_gallery.svg" width="96%" height="600px" name="incorrect_gallery"></embed>

<a href="./images/model0/incorrect_gallery.html" target="incorrect_gallery">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Pseudo-active learning

<div class="columns">
<div>

- Used model from these 6 neurons to predict on 20 more neurons
  - These varied more in dendrite thickness and spine density
- Plotted the posterior on the mesh, hand-labeled points I thought looked bad
- Took $\thicksim 2$ clicky hours
- Retrain
- Applied model to another 20 more neurons (not the ones trained on)

</div>
<div>

![h:450 center](./images/clicky-task.png)

</div>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135182486274_posterior.svg" width="96%" height="600px" name="864691135182486274_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135182486274_posterior.html" target="864691135182486274_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135182839810_posterior.svg" width="96%" height="600px" name="864691135182839810_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135182839810_posterior.html" target="864691135182839810_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135335398121_posterior.svg" width="96%" height="600px" name="864691135335398121_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135335398121_posterior.html" target="864691135335398121_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135361404743_posterior.svg" width="96%" height="600px" name="864691135361404743_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135361404743_posterior.html" target="864691135361404743_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135416507322_posterior.svg" width="96%" height="600px" name="864691135416507322_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135416507322_posterior.html" target="864691135416507322_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135491229535_posterior.svg" width="96%" height="600px" name="864691135491229535_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135491229535_posterior.html" target="864691135491229535_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135501563458_posterior.svg" width="96%" height="600px" name="864691135501563458_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135501563458_posterior.html" target="864691135501563458_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135645292783_posterior.svg" width="96%" height="600px" name="864691135645292783_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135645292783_posterior.html" target="864691135645292783_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135655141314_posterior.svg" width="96%" height="600px" name="864691135655141314_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135655141314_posterior.html" target="864691135655141314_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135693690303_posterior.svg" width="96%" height="600px" name="864691135693690303_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135693690303_posterior.html" target="864691135693690303_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135696697498_posterior.svg" width="96%" height="600px" name="864691135696697498_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135696697498_posterior.html" target="864691135696697498_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135697250714_posterior.svg" width="96%" height="600px" name="864691135697250714_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135697250714_posterior.html" target="864691135697250714_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135737477764_posterior.svg" width="96%" height="600px" name="864691135737477764_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135737477764_posterior.html" target="864691135737477764_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135800244578_posterior.svg" width="96%" height="600px" name="864691135800244578_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135800244578_posterior.html" target="864691135800244578_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135851482823_posterior.svg" width="96%" height="600px" name="864691135851482823_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135851482823_posterior.html" target="864691135851482823_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135875972691_posterior.svg" width="96%" height="600px" name="864691135875972691_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135875972691_posterior.html" target="864691135875972691_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136005566154_posterior.svg" width="96%" height="600px" name="864691136005566154_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136005566154_posterior.html" target="864691136005566154_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136109645240_posterior.svg" width="96%" height="600px" name="864691136109645240_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136109645240_posterior.html" target="864691136109645240_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136437250718_posterior.svg" width="96%" height="600px" name="864691136437250718_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136437250718_posterior.html" target="864691136437250718_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136923636708_posterior.svg" width="96%" height="600px" name="864691136923636708_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136923636708_posterior.html" target="864691136923636708_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Inhibitory neurons

---

<div>
<embed src="./images/boosted_model_posteriors/864691135014021110_posterior.svg" width="96%" height="600px" name="864691135014021110_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135014021110_posterior.html" target="864691135014021110_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691135497617939_posterior.svg" width="96%" height="600px" name="864691135497617939_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135497617939_posterior.html" target="864691135497617939_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136195002188_posterior.svg" width="96%" height="600px" name="864691136195002188_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136195002188_posterior.html" target="864691136195002188_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691136143786292_posterior.svg" width="96%" height="600px" name="864691136143786292_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691136143786292_posterior.html" target="864691136143786292_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div>
<embed src="./images/boosted_model_posteriors/864691137020205166_posterior.svg" width="96%" height="600px" name="864691137020205166_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691137020205166_posterior.html" target="864691137020205166_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Zero-shot prediction on a H01 neuron

<div>
<embed src="./images/h01/h01_posterior.svg" width="96%" height="550px" name="h01_posterior"></embed>

<a href="./images/h01/h01_posterior.html" target="h01_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Outline

- Motivation
- Intuition for heat kernel signatures
- Computing heat kernel signatures
- Application to spine prediction
- **Extensions**

---

# Extensions

---

# Extensions

<div class="columns">
<div>

### Computation

- Pade-Chebyshev polynomials

### Physical properties

- Scale-invariance: Bronstein et al. (2011)
- Volumetric HKS: Rustamov et al. (2009); Rustamov (2011)

</div>
<div>

### More elaborate learning

- Classical ML: Bronstein...
- Deep learning:
  - DiffusionNet
  - Hodge Net

</div>
</div>

---

# Volumetric diffusion distance / HKS

<div class="columns">
<div>

![h:500 center](./images/rustamov_heat_distance.png)

</div>
<div>

</div>
</div>

<!-- _footer: Rustamov et al., *Eurographics* (2009); Rustamov, *The Visual Computer* (2011)  -->

---

# Computing heat signatures from local integration

- Padé-Chebyshev polynomials paper

---

# Scale-invariance

- Bronstein paper

---

# More elaborate learning schemes

- DiffusionNet/Hodge Net
- Self-supervised learning?

---

# Summary

- Introduced the application of heat kernel signatures to neuron morphology
  - Translation/rotation/reflection invariant
  - Has some intrinsic "knowledge" of shape without learning
- Showed how to efficiently scale computation of HKS to scale/detail of neuronal meshes
- Showed these features can be used to create accurate classifiers for morphological features with relatively little training data

---

# Acknowledgements

Casey M. Schneider-Mizell
Forrest Collman
Bethanny Danskin
Erika Neace
Rachael Swanstrom

---

# Acknowledgements - extended

<style scoped>
p {
    font-size: 11px;
}
</style>

<div class="columns">
<div>

_Network Anatomy_
Clay Reid
Agnes Bodor
Adam Bleckert
JoAnn Buchanan
**Casey M. Schneider-Mizell**
Dan Bumbarger
Derrick Brittain
**Forrest Collman**
Steven Cook
Nuno da Costa
**Bethanny Danskin**
Sven Dorkenwald
Leila Elabbady
Emily Joyce
Dan Kapner
Sam Kinn
Cheryl Lea
Xiaoyu Lu
Gayathri Mahalingam
**Erika Neace**
Ben Pedigo
Sharmi Seshamani
Jenna Schardt
**Rachael Swanstrom**
Marc Takeno
Russel Torres
Keith Wiley
Wenjing Yin
Chi Zhang

</div>
<div>

_PM_
Lynne Becker
Florence D'Orazi
Sarah Naylor
Shelby Suckow
David Vumbaco
Susan Sunkin

_Morphology and 3D Reconstruction_
Rachel Dalley
Clare Gamlin
Staci Sorensen
Grace Williams

_Modeling & Simulation_
Ani Nandi
Tom Chartrand
Anatoly Buchin
Yina Wei
Soo Yeun Lee
Costas Anastassiou

_Technology_
Tim Fliss
Rob Young
And others

_IT_
Brian Youngstrom
Stuart Kendrick
Scott Harrison
Nathaniel Middleton
And others

</div>
<div>

_MPE_
Jay Borseth
Collin Farrell
And others

_MindScope_
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

_Alen Institute for Brain Sciences_
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

_Princeton_
Sven Dorkenwald
Tommy Macrina
Sebastian Seung
Nick Turner
And team

_Baylor_
Jake Riemer
Andreas Tolias
And team

_Harvard Medical School_
Brett Graham
Wei-Chung Lee
And team

_Janelia_
Khaled Khairy
Stephan Saalfeld
Carolyn Ott
Jennifer Lippincott-Schwartz
And others

_JHU_
Jenna Glatzer
Dwight Bergles

_APL_
Brock Wester
And team

</div>
<div>

_Neuro Surgery and Behavior_
_Lab Animal Services_
_Transgenic Colony Management_
_Finance_
_Legal_

_Computing Resources_
BBP5 Supercomputing Resources
National Energy Research Computing Center
AI HPC
Google Cloud

_Funding_
IARPA - MICRONS
NSF - NeuroNex
NIH – BICCN

</div>
</div>
