---
marp: true
theme: aibs
size: 16:9
paginate: true
math: true
backgroundImage: url(../themes/aibs-backgrounds/default.png)
transition: fade 0.1s
---

# Capocaccia

---

# MICrONS dataset

---

# Neural activity

---

# Morphology

---

# Cell types

---

# Connectivity

---

## Key concepts in CAVE data: segmentation

- Segmentation is _dynamic_
- Smallest segmentation object that is tracked is a **supervoxel**
- Supervoxels are aggregated in a hierarchy (octree), so you can have level 2 IDs (made up of supervoxels), level 3 IDs (made up of level 2 IDs), etc., all the way up to a **root ID**
- If an object is edited, Level 2 - root IDs are created or destroyed
   - Keeping track of objects over time is important
- Data we'll work with will be a fixed slice in time (version 1300), but you'll see supervoxel/root ID nomenclature a lot

---

## Key concepts in CAVE data: annotations
