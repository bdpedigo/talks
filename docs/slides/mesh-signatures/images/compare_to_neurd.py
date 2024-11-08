# %%
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from caveclient import CAVEclient

client = CAVEclient("minnie65_phase3_v1")

vortex_targets = client.materialize.query_table(
    "vortex_compartment_targets", log_warning=False
)
vortex_targets.set_index("target_id", inplace=True)

# %%


def process_tag(tag):
    if tag in ["soma", "shaft", "spine"]:
        return tag
    elif tag in ["orphan", "other", "not_synapse", "uncertain"]:
        return None
    elif tag == "soma_spine":
        return "spine"


vortex_targets["label"] = vortex_targets["tag"].apply(process_tag)
vortex_targets = vortex_targets.query("label.notna()")

# %%

neurd_targets = client.materialize.query_table(
    "synapse_target_structure",
    filter_in_dict=dict(target_id=vortex_targets.index),
    log_warning=False,
)
neurd_targets.set_index("target_id", inplace=True)

# %%


def decode_value(value):
    """
    0 : Synapse onto spine head
    1 : Synapse onto spine neck
    2 : Synapse onto dendritic shaft
    3 : Synapse onto spine but no clear head/neck separation for spine.
    4 : Synapse onto axonal bouton
    5 : Synapse onto axonal structure other than a bouton
    6 : Synapse onto soma
    """
    if value == 0:  # map spine head to spine
        return "spine_head"
    elif value == 1:  # map spine neck to spine
        return "spine_neck"
    elif value == 2:  # map dendritic shaft to shaft
        return "shaft"
    elif value == 3:  # map spine with no clear neck to spine
        return "spine_no_neck"
    elif value == 4:  # map axonal bouton to axon
        return "axon_bouton"
    elif value == 5:  # map axonal structure other than bouton to axon
        return "axon_other"
    elif value == 6:  # map soma to soma
        return "soma"


def decode_tag(tag):
    if tag in ["spine_head", "spine_neck", "spine_no_neck"]:
        return "spine"
    elif tag == "soma":
        return "soma"
    elif tag == "shaft":
        return "shaft"
    else:
        return None


neurd_targets["tag"] = neurd_targets["value"].map(decode_value)
neurd_targets["label"] = neurd_targets["tag"].map(decode_tag)
# %%
target_table = vortex_targets[["label", "tag"]].join(
    neurd_targets[["label", "tag"]], rsuffix="_neurd", lsuffix="_vortex"
)

# %%
label_conf_mat = (
    target_table.groupby(["label_vortex", "label_neurd"], dropna=False)
    .size()
    .unstack()
    .fillna(0)
    .astype(int)
)

# %%
label_conf_mat_restricted = label_conf_mat[["soma", "shaft", "spine"]]
label_conf_mat_restricted = label_conf_mat_restricted.loc[["soma", "shaft", "spine"]]

FIG_PATH = Path("/Users/ben.pedigo/code/meshrep/meshrep/figures/compare_to_neurd")

sns.set_context("talk")
fig, ax = plt.subplots()
sns.heatmap(
    label_conf_mat_restricted,
    annot=True,
    fmt="d",
    cmap="Reds",
    cbar=False,
    square=True,
    ax=ax,
)

ax.set_xlabel("Neurd")
ax.set_ylabel("Vortex")
plt.savefig(
    FIG_PATH / "vortex_neurd_simple_confusion_matrix.svg",
    format="svg",
    bbox_inches="tight",
)

conf_mat_restricted_norm = label_conf_mat_restricted.div(
    label_conf_mat_restricted.sum(axis=1), axis=0
)

fig, ax = plt.subplots()
sns.heatmap(
    conf_mat_restricted_norm,
    annot=True,
    fmt=".2f",
    cmap="Reds",
    cbar=False,
    square=True,
    ax=ax,
)

ax.set_xlabel("Neurd")
ax.set_ylabel("Vortex")
plt.savefig(
    FIG_PATH / "vortex_neurd_simple_confusion_matrix_normalized.svg",
    format="svg",
    bbox_inches="tight",
)

# %%
tag_conf_mat = (
    target_table.groupby(["tag_vortex", "tag_neurd"])
    .size()
    .unstack()
    .fillna(0)
    .astype(int)
)
tag_conf_mat = tag_conf_mat[
    [
        "shaft",
        "soma",
        "spine_head",
        "spine_neck",
        "spine_no_neck",
        # "axon_bouton",
        # "axon_other",
    ]
]

# %%
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(
    tag_conf_mat,
    annot=True,
    fmt="d",
    cmap="Reds",
    cbar=False,
    square=True,
    ax=ax,
)

ax.set_xlabel("Neurd")
ax.set_ylabel("Vortex")

tag_conf_mat_norm = tag_conf_mat.div(tag_conf_mat.sum(axis=0), axis=1)

fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(
    tag_conf_mat_norm,
    annot=True,
    fmt=".2f",
    cmap="Reds",
    cbar=False,
    square=True,
    ax=ax,
)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_xlabel("Neurd")
ax.set_ylabel("Vortex")
plt.savefig(
    FIG_PATH / "vortex_neurd_tag_confusion_matrix.svg",
    format="svg",
    bbox_inches="tight",
)

# %%
