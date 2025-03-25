---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
transition: fade 0.1s
---

<!-- TODO cell types plot -->

<style>
a {
  position: fixed;
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
[data-morph] {
  view-transition-name: attr(data-morph type(<custom-ident>), none);
}
section::after {
    content: attr(data-marpit-pagination) '/51';
}
</style>

<!-- _paginate: false -->
<!-- _backgroundImage: ../themes/aibs-backgrounds/blank.png -->

![bg opacity:0.4](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

<br>

# <!-- fit --> Mapping million spines in EM with spectral shape analysis

<div class="columns">
<div>

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

</div>

</div>
<div>

</div>
</div>

---

<!-- NOTE spines are a prevalent morphological features, and a fundamental building block of connectivity between neurons -->

# Dendritic spines

<div class="columns">
<div>

<embed src="./images/new_posterior_plots/basic_neuron.html" width="99%" height="550px" name="basic_neuron" style="border-width: 0px; border-color: white; display: block; margin: 0 auto;" data-morph="microns"></embed>

</div>
<div>

* Primary site of excitatory $\rightarrow$ excitatory synapses
* Chemo-electrically isolated
* Dynamic
* Mechanism for neurons to "reach out" to partners

</div>
</div>

<!-- _transition: fade 0.5s -->

---
<style scoped>
.fig belowcaption {
    position: absolute;
    bottom: 5%;
    left: 15%;
    vertical-align: top;
    text-anchor: start;
    font-size: 20px;
    font-weight: normal;
}
</style>

# MICrONS

<div class="columns-bl">
<div>

<figure class='fig'>
<img src="./images/microns_covers/minnie_activity_12color.png" style="display: block; margin: 0 auto;" data-morph="microns"></img>

<belowcaption>

Forrest Collman

</belowcaption>

</figure>

</div>
<div>

* Scale
* Pre- and post-synaptic partners
* Cell types
* EM imagery

<!-- * Correlated activity -->

</div>
</div>

<!-- _footer: MICrONS consortium et al. Nature (In press) -->


<!-- ![center h:560](./images/microns_covers/minnie_activity_12color.png) -->


<!-- NOTE Once you've gotten all this cool EM data, there's still a lot of work to add semantic information -->

<!-- NOTE can see all sorts of patterns like myelin, somas, spines, etc but it is still a lot of work to measure -->

<!-- NOTE Briefly mention some papers that have worked on adding this info, like cell type, dendritic features  -->

---

# Community interest in spines in EM: VORTEX

<!-- NOTE Nothing existed in this space for doing something as fine as spines -->
<!-- NOTE Many people had questions about spines -->
<!-- NOTE This led to Virtual observatory of cortex grant doing a bunch of hand annotation -->


<div class="columns">
<div>

VORTEX - supporting scientific community engagement with MICrONS

* Basket cells onto spines with multiple inputs
* Spines with spine head apparatus
* Computational questions about modeling spine heads as distinct compartments
<!-- * Analyzing how passing axons relate to dendritic morphology -->

</div>
<div>

</div>
</div>

---

# Community interest in spines in EM: VORTEX

<div class="columns">
<div>

VORTEX: supporting community interest in MICrONS:

- Basket cells onto spines with multiple inputs
-  Spines with spine head apparatus
- Computational questions about modeling spine heads as distinct compartments
<!-- * Analyzing how passing axons relate to dendritic morphology -->

</div>
<div>

<div style="font-size:20px">

_Bethanny Danskin, Erika Neace, Rachael Swanstrom_

Synapses labeled <span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>

</div>

<div>
<embed src="./images/vortex_labels/vortex_labels_example.html" width="96%" height="450px" name="vortex_labels_example"></embed>

</div>
</div>


---

<style scoped>
section {
  align-content: center;
}
p {
  font-size: 30px;
}
</style>

<div id='highlightbox'>

# <!-- fit --> Goal: pipeline for automated postsynaptic structure prediction

<!-- Develop an accurate, robust, and scaleable prediction of postsynaptic structure -->

</div>

---

![bg opacity:0.2](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

# Outline

- Motivation
* **Intuition for heat kernel signatures**
* Computational pipeline for postsynaptic structure prediction
* Postsynaptic structures in MICrONS

---

<!-- First choice to make is what representation to use -->
<!-- Explain what segmentation, mesh, and skeleton are -->
<!-- Each of these differs in scale and size and ease of operaition etc. -->
<!-- First intuition was that we should be able to use the mesh to find spines, because people do -->

# Morphological representations

<div class="columns">
<div>

Segmentation/imagery
(_Voxels_)

![](./images/explain_morphology_representations/segmentation.svg)

</div>
<div>

Mesh
(_Triangulation of surface_)

<!-- ![](./images/explain_morphology_representations/mesh.svg) -->

<img src="./images/explain_morphology_representations/mesh.svg" data-morph="mesh"></img>

</div>
<div>

Skeleton
(_Coarse medial axis_)

![](./images/explain_morphology_representations/skeleton.svg)

</div>
</div>

<div style="text-align: center">

$\leftarrow$ More expensive &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Less expensive $\rightarrow$

</div>

<!-- _transition: fade 1s -->

---

# How to generate features for a mesh?

<div class="columns">
<div>

<img src="./images/explain_morphology_representations/mesh.svg" data-morph="mesh"></img>

</div>
<div>

![center](./images/sun-et-al.png)

</div>
</div>


---

# Heat diffusion

Imagine placing a unit of heat at a point on a surface, watching how that heat diffuses

![](https://upload.wikimedia.org/wikipedia/commons/d/d9/Fundamental_solution_to_the_heat_equation.gif)

<!-- _footer: https://en.wikipedia.org/wiki/Heat_equation -->

---

<div style="font-size:20px">
<span style="color: var(--soma);"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>

<!-- ![gallery h:540 center](./images/show_heat_diffusion/heat_diffusion_gallery.svg) -->

<img src="./images/show_heat_diffusion/heat_diffusion_gallery.svg" height="540px" data-morph="gallery" style="display: block; margin: 0 auto;" ></img>

<div style="font-size:30px; text-align: center; top: -40px; position: relative;">

Increasing time $\rightarrow$

</div>

<!-- _transition: fade 0.5s -->

---

<!-- TODO EXP fix this up so the y axis starts the same for the panel at right -->

# Tracking heat diffusion

<div class="columns">
<div>

<!-- ![gallery](./images/show_heat_diffusion/heat_diffusion_gallery.svg) -->

<img src="./images/show_heat_diffusion/heat_diffusion_gallery.svg" data-morph="gallery"></img>

</div>
<div>

<img src="./images/show_heat_diffusion/heat_diffusion_time_scale.svg" data-morph="hks-curves"></img>


</div>
</div>

<!-- _transition: fade 0.5s -->

---

# Defining the heat kernel signature (HKS)

<div class="columns">
<div>

<img src="./images/show_heat_diffusion/heat_diffusion_time_scale.svg" data-morph="hks-curves"></img>

</div>
<div>

* $k_{t}(x)$: amount of heat left at $x$ after time $t$.
* For timescales $\{t_1, ... t_d\}$ the HKS for point $x$ is
  $$HKS(x) = [k_{t_1}(x), ..., k_{t_d}(x)]$$
* Often scale these: $\frac{k_{t_1}(x)}{\sum_i k_{t_1}(i)}$
* <div id="highlightbox"> HKS is a vector for each <span style="font-weight: bold">node</span> in a mesh which describes its heat diffusion properties </div>


</div>
</div>

<!-- _footer: Sun et al., _Eurographics_ (2008) -->

---

# Intuition for HKS matching

<style scoped>

p {
  font-size: 20px;
}

</style>

<div class="columns">
<div>

<!-- ![h:350 center](./images/hks_paper_synthetic_example.png) -->

<img src="./images/hks_paper_synthetic_example.png" data-morph="hks-plot" height=350px style="display: block; margin: 0 auto;"></img>

> ...all four points have isometric neighborhoods at small scales, their HKS’s are the same for small $t$’s ($< t_1$).

</div>
<div>

![center](./images/horses.png)

<!-- <img src="./images/horses.png" data-morph="octopus"></img> -->

</div>
</div>

<!-- _footer: Sun et al., _Eurographics_ (2008) -->

---

# Clustering on heat kernel signatures

<div class="columns">
<div>

![h:270 center](./images/show_heat_diffusion/hks_lines.svg)

![center h:270](./images/show_heat_diffusion/hks_clustermap.png)

<!-- <img src="./images/show_heat_diffusion/hks_lines.svg" data-morph="hks-plot" height=270px style="display: block; margin: 0 auto;"></img> -->

</div>
<div>

<div>
<embed src="./images/show_heat_diffusion/hks_clustered.html" width="96%" height="550px" name="hks_clustered" data-morph="octopus"></embed>

</div>
</div>
</div>

---

# Postsynaptic structure prediction (with labels)

<div class="columns">
<div>

![](./images/vortex_labels/vortex_labels_example.svg)

</div>
<div>

- Synapse target labels from VORTEX _(Erika Neace, Rachael Swanstrom, Bethanny Danskin)_
* HKS features from the mesh point closest to synapse
* Random forest classifier

</div>
</div>


<!-- --- -->

<!-- Import the component
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.0.0/model-viewer.min.js"></script>

<style>
model-viewer {
  width: 100%;
  height: 100%;
  background-color: #000;
  color: #3d3d3d
}
</style>

<model-viewer alt="A neuron" src="https://raw.githubusercontent.com/bdpedigo/talks/refs/heads/main/docs/slides/2025-03-25-brain-science-seminar/models/864691135855890478.gltf" camera-controls touch-action="pan-y"
auto-rotate rotation-per-second="150%" camera-target="0m 0m 0m" min-field-of-view="0.25deg" field-of-view="auto" max-field-of-view="6deg"> -->

<!--
<model-viewer alt="A neuron" src="http://localhost:9001/864691135855890478.gltf" camera-controls touch-action="pan-y"
auto-rotate rotation-per-second="150%" camera-target="0m 0m 0m" min-field-of-view="0.25deg" field-of-view="auto" max-field-of-view="6deg"> -->

<!--
<model-viewer alt="Neil Armstrong's Spacesuit from the Smithsonian Digitization Programs Office and National Air and Space Museum" src="shared-assets/models/NeilArmstrong.glb" ar environment-image="shared-assets/environments/moon_1k.hdr" poster="shared-assets/models/NeilArmstrong.webp" shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer>
-->

---

# <!-- fit --> Random forest on HKS is an accurate classifier

Train test split over _neurons_
<div class="columns">
<div>

![h:500 center](./images/model_comparison/metrics-Heat-RF-NEURD.svg)

</div>
<div>

![h:500 center](./images/model_comparison/metrics-Heat-RF.svg)

</div>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div>
<embed src="./images/boosted_model_posteriors/864691135182486274_posterior.svg" width="96%" height="600px" name="864691135182486274_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135182486274_posterior.html" target="864691135182486274_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div>
<embed src="./images/boosted_model_posteriors/864691135361404743_posterior.svg" width="96%" height="600px" name="864691135361404743_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135361404743_posterior.html" target="864691135361404743_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div>
<embed src="./images/boosted_model_posteriors/864691135416507322_posterior.svg" width="96%" height="600px" name="864691135416507322_posterior"></embed>

<a href="./images/boosted_model_posteriors/864691135416507322_posterior.html" target="864691135416507322_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

---

# Excitatory neurons

<div style="font-size:20px; padding: 0px; position: absolute; top: 0.6in; right: 0.7in;">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div class="columns">
<div>

<!-- ![](./images/new_posterior_plots/864691135119068125-23P.svg) -->

<figure class="fig">
<img src="./images/new_posterior_plots/864691135119068125-23P.svg" />
<figcaption >
23P
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691136067090584-4P.svg" />
<figcaption >
4P
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135388264577-5P-IT.svg" />
<figcaption >
5P-IT
</figcaption>
</figure>

</div>
</div>

<div class="columns">
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691136362746082-5P-NP.svg" />
<figcaption >
5P-NP
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691136362774498-5P-PT.svg" />
<figcaption >
5P-ET
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135688407776-6P-CT.svg" />
<figcaption >
6P-CT
</figcaption>
</figure>

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press) -->

---

# Excitatory or inhibitory?

<style scoped>
a {
  position: relative;
}
img {

}
img:hover {
  box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}
</style>

<div class="columns">
<div>

##### A) <a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4927362740256768"><img src="./images/e_vs_i_spines/state=4927362740256768.png"></img></a>


</div>
<div>

##### B)

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5018403698900992"><img src="./images/e_vs_i_spines/state=5018403698900992.png"></img></a>


</div>
<div>

##### C)

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5294319914188800"><img src="./images/e_vs_i_spines/state=5294319914188800.png"></img></a>

</div>
</div>

<div class="columns">
<div>

##### D)

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4938240147587072"><img src="./images/e_vs_i_spines/state=4938240147587072.png"></img></a>


</div>
<div>

##### E)

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5256989132193792"><img src="./images/e_vs_i_spines/state=5256989132193792.png"></img></a>

</div>
<div>

##### F)

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6342512605134848"><img src="./images/e_vs_i_spines/state=6342512605134848.png"></img></a>

</div>
</div>

---

# Excitatory or inhibitory?

<style scoped>
a {
  position: relative;
}
img {

}
img:hover {
  box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
}
</style>

<div class="columns">
<div>

##### Inhibitory <a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4927362740256768"><img src="./images/e_vs_i_spines/state=4927362740256768.png"></img></a>


</div>
<div>

##### Excitatory

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5018403698900992"><img src="./images/e_vs_i_spines/state=5018403698900992.png"></img></a>


</div>
<div>

##### Inhibitory

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5294319914188800"><img src="./images/e_vs_i_spines/state=5294319914188800.png"></img></a>

</div>
</div>

<div class="columns">
<div>

##### Excitatory

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4938240147587072"><img src="./images/e_vs_i_spines/state=4938240147587072.png"></img></a>


</div>
<div>

##### Inhibitory

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/5256989132193792"><img src="./images/e_vs_i_spines/state=5256989132193792.png"></img></a>

</div>
<div>

##### Excitatory

<a href="https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6342512605134848"><img src="./images/e_vs_i_spines/state=6342512605134848.png"></img></a>

</div>
</div>

---

# Inhibitory neurons

<div style="font-size:20px; padding: 0px; position: absolute; top: 0.6in; right: 0.7in;">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div class="columns">
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135082840567-BC.svg" />
<figcaption >
Basket
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135865240702-BC.svg" />
<figcaption >
Basket
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135339516390-MC.svg" />
<figcaption >
Martinotti
</figcaption>
</figure>

</div>
</div>

<div class="columns">
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135777888864-MC.svg"/>
<figcaption >
Martinotti
</figcaption>
</figure>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135976155459-NGC.svg"/>
<figcaption >
Neurogliaform
</figcaption>
</figure>

<!-- cover some axon that didn't get pruned -->
<div style="position: absolute; top: 6.25in; left: 8.25in; background-color: white; width:10px; height:10px; border-width: 0px; border-color: black; border-style: solid;"></div>

</div>
<div>

<figure class="fig">
<img src="./images/new_posterior_plots/864691135386940245-BPC.svg"/>
<figcaption >
Bipolar
</figcaption>
</figure>

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press) -->

---

# Zero-shot prediction on a human neuron

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

<div>
<embed src="./images/h01/h01_posterior.svg" width="96%" height="520px" name="h01_posterior"></embed>

<a href="./images/h01/h01_posterior.html" target="h01_posterior">
<img src="./../../images/icons/search.svg"></img>
</a>
</div>

<!-- _footer: Shapson-Coe et al. _Science_ 2024  -->


---

![bg opacity:0.2](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

# Outline

- Motivation
- Intuition for heat kernel signatures
- **Computational pipeline for postsynaptic structure prediction**
- Postsynaptic structures in MICrONS

---

# Heat diffusion

* Evolution of heat $u$ is governed by the heat equation:
  $$\frac{\partial{u}}{\partial{t}} = \Delta u$$  
  where $\Delta$ is the Laplacian (2nd derivative) operator
* Heat remaining at $x$ after $t$ is:
  $$k_t(x) = \sum_{i=0}^{\infty} e^{-\lambda_i t} \phi_i(x)^2 \approx \sum_{i=0}^{K} e^{-\lambda_i t} \phi_i(x)^2 $$
  where $\lambda_i$ and $\phi_i$ are the eigenvalues and eigenvectors of the Laplacian operator
* <div id="highlightbox"> We just need these eigenvectors/eigenvalues to compute HKS </div>

<!-- _footer: https://en.wikipedia.org/wiki/Heat_kernel -->

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

<div>
<embed src="./images/show_heat_diffusion/eigenvector_on_mesh.html" width="96%" height="380px" name="eigenvector_on_mesh"></embed>

</div>

</div>
</div>

* Eigendecomposition allows you to compute HKS for every point simultaneously
* Takes several hours for a full neuron mesh

---

# Computational improvements

<div class="columns">
<div>

- Overlapping mesh subdivision
* Mesh simplification (Garland and Heckbert 1997)
* Band-by-band eigendecomposition (Vallet and Levy 2008)
* Robust laplacian (Sharp and Crane 2020)
* Mesh agglomeration (for compressed storage)

</div>
<div>

<figure class='fig'>
<img src="./images/show_mesh_splitting/submeshes.svg" height=260px/>
<figcaption>
Subdivided mesh
</figcaption>
</figure>

<figure class='fig'>
<img src="./images/show_mesh_splitting/submeshes_overlapped.svg" height=260px/>
<figcaption>
Subdivided mesh with overlap
</figcaption>
</figure>

</div>
</div>

---

# Timing and compute

<!-- TODO SCI compare to the version without these speedups -->

<div class="columns">
<div>

- Deployed on Google Kubernetes Engine
- ~20 minutes per neuron per CPU
  - ~2 minutes on your laptop
- Mean cost **~0.5 cents per neuron**

<!-- ![center h:420](./images/timing/timing_n_vertices_vs_wall_time.svg) -->

</div>
<div>

![center](./images/timing_foggy_forest_call/effective_time_scatter_by_size.svg)

<!-- ![center h:420](./images/timing/timing_n_vertices_vs_wall_time_per_root.svg) -->

</div>
</div>

---

# Run on MICrONS

<div class="columns">
<div>

- Ran on ~72,000 putative neurons
- ~204 million synapses classified into &nbsp; { <span style="color: rgb(0, 227, 255);">soma</span> <span style="color: rgb(239, 230, 69);">shaft</span> <span style="color: rgb(233, 53, 161);">spine</span> }
- ~$500 in cloud compute cost

</div>
<div>

<figure class="fig">
<img src="./images/synapse_spatial/synapse_cloud_layered.svg" height=500px/>
<belowcaption>

_~1 million (0.5%) of classified synapses_

</belowcaption>
</figure>

</div>
</div>

---

![bg opacity:0.2](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

# Outline

- Motivation
- Intuition for heat kernel signatures
- Computational pipeline for postsynaptic structure prediction
- **Postsynaptic structures in MICrONS**

---

<!-- NOTE at a high level, we can look at things in terms of their laminar distribution -->
<!-- NOTE there is an abundance of synapses onto spines in upper layers  -->

# Spatial distribution of synapses

<div class="columns">
<div>

<div style="font-size:16px">
<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span>
</div>

![center h:520](./images/synapse_spatial/synapse_cloud_layered.svg)

<!-- 1.3M synapses (= .63% of classified) -->

</div>
<div>

![center h:500](./images/synapse_spatial/synapse_spatial_kde.svg)

</div>
</div>

---

<div class="columns-br">
<div>

# Synapses by E/I

Synapses from cleaned axons where pre- and post- have E/I classifications (1.3M synapses total)

</div>
<div>

![h:600 center](./images/tabulation_by_type/empty.svg)

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press), Elabbady et al. Nature (In press) -->

---

# Multi-input spines

<!-- TODO EXP add a nice image here of more than one axon onto a spine -->

<div class="columns">
<div>

* Most (>90%) excitatory spines receive a single excitatory input
* Some excitatory spines receive two
  - Specifically one E, one I
  - Enriched for thalamic input
  - More stable
* Multi-input spines common for inhibitory neurons

</div>
<div>

![](./images/double-contact.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6025508249665536 -->

</div>
</div>

<!-- _footer: Kubota et al _J. Neuroscience_ (2007), Villa et al _Neuron_ (2016), Hwang et al _Cerebral Cortex_ (2021) -->

---

# Finding multi-input spines

<div class="columns">
<div>

<span style="color: var(--soma);">soma</span> <span style="color: var(--shaft);">shaft</span> <span style="color: var(--spine);">spine</span> &nbsp;&nbsp;&nbsp; :black_circle: synapse detection

![](./images/new_posterior_plots/zoom_posterior_colors.svg)

</div>
<div>

Connected components sharing a label

![](./images/new_posterior_plots/zoom_component_colors.svg)

<div style="position: absolute; top: 1.8in; left: 9.5in;">Multi-input</div>
<div style="position: absolute; top: 2.2in; left: 9.5in; width: 140px; height: 140px; background-color: none; border-radius: 70px; border-width: 3px; border-color: black; border-style: solid;"></div>

<div style="position: absolute; top: 4.1in; left: 10.8in;">Single-input</div>
<div style="position: absolute; top: 4.5in; left: 10.8in; width: 140px; height: 140px; background-color: none; border-radius: 70px; border-width: 3px; border-color: black; border-style: solid;"></div>

</div>
</div>

---

# <!-- fit --> A triple-input spine onto an excitatory cell

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6077690223263744 -->

![h:525 center](./images/triple-spine.png)

---

<div class="columns-br">
<div>

# Synapses by E/I

Synapses from cleaned axons where pre- and post- have E/I classifications (1.3M synapses total)

</div>
<div>

![h:600 center](./images/tabulation_by_type/ei_synapse_proportions_w_multi_just_e_e.svg)

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press), Elabbady et al. Nature (In press) -->

---

<div class="columns-br">
<div>

# Synapses by E/I

Synapses from cleaned axons where pre- and post- have E/I classifications (1.3M synapses total)

</div>
<div>

![h:600 center](./images/tabulation_by_type/ei_synapse_proportions_w_multi.svg)

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press), Elabbady et al. Nature (In press) -->

---

<!-- NOTE because microns also has some cell type information, we can also look at a similar plot but now broken out by cell type
-->
<!-- NOTE a lot going on here, but going to draw your attention to just a few things -->

<div class="columns-br">
<div>

# Synapses by cell type

</div>
<div>

![h:600 center](./images/tabulation_by_type/cell_type_synapse_proportions_w_multi.svg)

</div>
</div>

<!-- _footer: Cell types from Schneider-Mizell et al. Nature (In press) -->

---

# Basket cells target somas, even of inhibitory cells

![](./images/tabulation_by_type/bc_targets.svg)

<div class="columns">
<div>

![center](./images/example_contacts/bc_to_inhibitory/state=4910284205457408.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4910284205457408 -->

<span style="color: #e1562c">Basket </span> $\rightarrow$ <span style="color: #00cb85"> Basket</span>

</div>
<div>

![center](./images/example_contacts/bc_to_inhibitory/state=6700069303615488.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6700069303615488 -->

<span style="color: #e1562c">Basket</span> $\rightarrow$ <span style="color: #00cb85"> Bipolar </span>

</div>
<div>

![center](./images/example_contacts/bc_to_inhibitory/state=6074562245558272.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6074562245558272 -->

<span style="color: #e1562c">Basket</span> $\rightarrow$ <span style="color: #00cb85"> Martinotti </span>

</div>
</div>

---

# L6 CT cells target shafts of other excitatory cells

![](./images/tabulation_by_type/6pct_targets.svg)

<div class="columns">
<div>

![center](./images/example_contacts/6ct_to_e_shaft/state=4808939033067520.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4808939033067520 -->

<span style="color: #e1562c">6P-CT </span> $\rightarrow$ <span style="color: #00cb85"> 4P</span>

</div>
<div>

![center](./images/example_contacts/6ct_to_e_shaft/state=6560729223135232.png)

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6560729223135232 -->

<span style="color: #e1562c">6P-CT </span> $\rightarrow$ <span style="color: #00cb85"> 5P-ET</span>

</div>
<div>

![center](./images/example_contacts/6ct_to_e_shaft/state=4835245372211200.png)

<span style="color: #e1562c">6P-CT </span> $\rightarrow$ <span style="color: #00cb85"> 5P-IT</span>

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/4835245372211200 -->

</div>
</div>

---

# 5P-ET to Martinotti spines

<!-- TODO add text to this slide -->

<!-- __backgroundImage: ../themes/aibs-backgrounds/blank.png -->

<div class="columns">
<div>

![h:550](./images/tabulation_by_type/cell_type_synapse_proportions_w_multi.svg)

<!-- add an absolute position white box without text, with black border -->

<!-- block out upper left corner -->
<div style="position: absolute; bottom: 5.26in; right: 7.76in; width: 4.4in; height: .94in; background-color: white; opacity:0.9; border: 0px solid black;"></div>

<!-- block out lower left corner -->
<div style="position: absolute; top:2.7in; right: 7.76in; width: 4.4in; height: 4.2in; background-color: white; opacity:0.9; border: 0px solid black;"></div>

<!-- block out upper right corner -->
<div style="position: absolute; bottom: 5.26in; left: 6.05in; width: .6in; height: .94in; background-color: white; opacity:0.9; border: 0px solid black;"></div>

<!-- block out lower right corner -->
<div style="position: absolute; top:2.7in; left: 6.05in; width: .6in; height: 4.2in; background-color: white; opacity:0.9; border: 0px solid black;"></div>

<!-- red block in the gap between the above -->
<div style="position: absolute; top: 2.35in; left: 5.7in; width: 0.4in; height: .5in; backbround-color: none; border: 3px solid red; border-radius:20px"></div>

</div>
<div>

<div class="columns-br-tight">
<div>

<span style="color: #e1562c">5P-ET </span> $\rightarrow$ <span style="color: #00cb85"> Martinotti</span>

</div>
<div>

![center](./images/example_contacts/5et_to_mc/state=6128785033265152.png)

</div>
</div>

<div class="columns-br-tight">
<div>

<span style="color: #e1562c">5P-ET </span> $\rightarrow$ <span style="color: #00cb85"> Martinotti</span>

</div>
<div>

![center](./images/example_contacts/5et_to_mc/state=6310820913872896.png)

</div>
</div>


<!-- 

![center h:200](./images/example_contacts/5et_to_mc/state=6128785033265152.png) -->

<!-- ![center h:200](./images/example_contacts/5et_to_mc/state=6310820913872896.png) -->

<!-- <figure class='fig'>
<img src="./images/example_contacts/5et_to_mc/state=6310820913872896.png" />
</figure> -->

</div>
</div>

<!-- _footer: Bodor et al. Nature Neuroscience (In press) -->

---

# Variability within type

![center h:550](./images/projection_by_cell_scatters/cell_type_scatter_no_auto.svg)

<!-- add an span with absolute positioning above the figure -->
<!-- 
<span style="position: absolute; top: 4in; left: 8in; font-size: 15px; background-color: white; padding: 5px; border-radius: 5px; color: red">Manually classified (Schneider-Mizell et al. Nature 2025)</span>

<span style="position: absolute; top: 4.25in; left: 8in; font-size: 15px; background-color: white; padding: 5px; border-radius: 5px; color: #1f77b4">Automatically classified (Elabbady et al. Nature 2025)</span> -->

<!-- _footer: Cells types from Schneider-Mizell et al. Nature (In press) -->

---

# Perisomatic targeting cells

![h:500 center](./images/basket-cell-spineyness.png)

<div class="columns">
<div>

<span style="color:#4da0ff; text-align: right; display: block">~1% inputs onto spines</span>

</div>
<div>

<span style="color: #FFA94D">~23% inputs onto spines</span>

</div>
</div>

<!-- https://spelunker.cave-explorer.org/#!middleauth+https://global.daf-apis.com/nglstate/api/v1/6748095493701632 -->


--- 

# Variability within type

![center h:550](./images/projection_by_cell_scatters/cell_type_scatter_with_auto.svg)


<span style="position: absolute; top: 4in; left: 8in; font-size: 15px; background-color: white; padding: 5px; border-radius: 5px; color: red">Manually classified (Schneider-Mizell et al. Nature 2025)</span>

<span style="position: absolute; top: 4.25in; left: 8in; font-size: 15px; background-color: white; padding: 5px; border-radius: 5px; color:rgb(83, 83, 83)">Automatically classified (Elabbady et al. Nature 2025)</span>

<!-- _footer: Cells types from Schneider-Mizell et al. Nature (In press), Elabbady et al. Nature (In press) -->

---

# Accessing the data

* Cafe in AM
* Available in the **C**onnectome **A**nnotation and **V**ersioning **E**ngine (CAVE):
  ```python
  from caveclient import CAVEclient
  client = CAVEclient("minnie65_public", version=1300)
  client.materialize.query_table(
      "synapse_target_predictions_ssa",
      limit=2,
      select_columns=["target_id", "pre_pt_root_id", "post_pt_root_id", "tag", "size"],
  )
  ```

  ```plaintext
  pre_pt_root_id	        post_pt_root_id	        size	target_id	tag
  864691135468221308	864691135383487706	4284	306517361	spine
  864691135979239816	864691135383487706	1620	285512620	shaft
  ```

<!-- _footer: CAVE: Dorkenwald, Schneider-Mizell et al Nature Methods (In press) -->

---

# Summary

* Developed a method based on spectral shape analysis (HKS) for classifying postsynaptic structures based on mesh alone
* Scaled this system to robustly classify >200M synapses in MICrONS
* Described initial findings on how postsynaptic structure targeting varies by cell type

---

# Future directions

<div class="columns">
<div>

- Other classification/segmentation tasks (e.g. axonal boutons)
* Add morphometry (e.g. compute spine volumes, surface area, etc.)
* Study spatial distribution of spine densities on individual neurons
* Deploy on more datasets

</div>
<div>

![h:500](./images/boutons/boutons.png)
_Segmenting thalamic axon boutons_

</div>
</div>

---

# Acknowledgements

<style scoped>
p {
    font-size: 10px;
}
h6 {
  font-size: 14px;
}

</style>

<div class="columns">
<div>

<ins>_Network Anatomy_</ins>
**Forrest Collman**
**Bethanny Danskin**
**Casey M. Schneider-Mizell**
**Erika Neace**
**Rachel Swanstrom**
Adam Bleckert
Agnes Bodor
Derrick Brittain
JoAnn Buchanan
Dan Bumbarger
Steven Cook
Nuno da Costa
Cameron Devine
Sven Dorkenwald
Leila Elabbady
Elizabeth Guadarrama
Kim Gruver
Emily Joyce
Dan Kapner
Sam Kinn
Cheryl Lea
Xiaoyu Lu
Gayathri Mahalingam
Sid Rath
Clay Reid
Jenna Schardt
Sharmi Seshamani
Marc Takeno
Russel Torres
Keith Wiley
Wenjing Yin
Chi Zhang

</div>
<div>

<ins>_PM_</ins>
Lynne Becker
Florence D'Orazi 
Melissa Lerch
Sarah Naylor
Shelby Suckow
Susan Sunkin
David Vumbaco

<ins>_Morphology and 3D Reconstruction_</ins>
Rachel Dalley
Clare Gamlin
Staci Sorensen
Grace Williams

<ins>_Modeling & Simulation_</ins>
Ani Nandi
Tom Chartrand
Anatoly Buchin
Yina Wei
Soo Yeun Lee
Costas Anastassiou

<ins>_Technology_</ins>
Tim Fliss
Rob Young
And others

<ins>_IT_</ins>
Brian Youngstrom
Stuart Kendrick
Scott Harrison
Nathaniel Middleton
And others

</div>
<div>

<ins>_MPE_</ins>
Jay Borseth
Collin Farrell
And others

<ins>_MindScope_</ins>
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

<ins>_Alen Institute for Brain Science_</ins>
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

<ins>_Princeton_</ins>
Sven Dorkenwald
Tommy Macrina
Sebastian Seung
Nick Turner
And team

<ins>_Baylor_</ins>
Jake Riemer
Andreas Tolias
And team

<ins>_Harvard Medical School_</ins>
Brett Graham
Wei-Chung Lee
And team

<ins>_Janelia_</ins>
Khaled Khairy
Stephan Saalfeld
Carolyn Ott
Jennifer Lippincott-Schwartz
And others

<ins>_JHU_</ins>
Jenna Glatzer
Dwight Bergles

<ins>_APL_</ins>
Brock Wester
And team

</div>
<div>

<ins>_Neuro Surgery and Behavior_</ins>
<ins>_Lab Animal Services_</ins>
<ins>_Transgenic Colony Management_</ins>
<ins>_Finance_</ins>
<ins>_Legal_</ins>

<ins>_Computing Resources_</ins>
BBP5 Supercomputing Resources
National Energy Research Computing Center
AI HPC
Google Cloud

<ins>_Funding_</ins>
IARPA - MICRONS
NSF - NeuroNex
NIH – BICCN

</div>
</div>

###### We wish to thank the Allen Institute founder, Paul G. Allen, for his vision, encouragement, and support.


---

# Questions?

<!-- _backgroundImage: ../themes/aibs-backgrounds/blank.png -->

![bg opacity:0.4](./images/boosted_model_posteriors/864691135361404743_posterior.svg)

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

---

# Variability within type - outputs 

![h:550 center](./images/projection_by_cell_scatters/cell_type_scatter_outputs.svg)

---

# An aside...

<div class="columns">
<div>

Many generalizations/extensions of HKS:

- Alternative computational schemes:
  <span style="font-size: 14px">Nasikun et al. 2018; Nasikun et al. 2022; Magnet and Ovsjanikov 2023, Hammond et al. 2009; Shuman et al. 2011; Huang et al. 2020 </span>
- Volumetric HKS:
  <span style="font-size: 14px">Raviv et al. 2010; Rustamov et al. 2009; Rustamov 2011</span>

</div>
<div>

HKS features:

$$h_t(x) = \sum_{i=0}^{D} e^{-\lambda_i t} \phi_i(x)^2$$

Learned spectral features (Litman & Bronstein 2014):

$$x_t(x) = \sum_{i=0}^{D} \textcolor{red}{f_t(\lambda)} \phi_i(x)^2$$

<!-- Spectral graph neural network layer (add citation): -->

</div>
</div>
