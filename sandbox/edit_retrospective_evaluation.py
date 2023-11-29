# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# plt.xkcd(randomness=10, scale=1, length=150)

plt.xkcd()


rows = []

rows.append(
    {
        "name": "Connectivity\nsensitivity",
        "Enthusiasm": 5,
        "Enthusiasm variance": 0.5,
        "Significance": 3.5,
        "Significance variance": 0.75,
        "Feasibility": 4,
        "Feasibility variance": 1,
    }
)

rows.append(
    {
        "name": "Morphology\nresampling",
        "Enthusiasm": 3,
        "Enthusiasm variance": 0.25,
        "Significance": 2,
        "Significance variance": 1,
        "Feasibility": 4.5,
        "Feasibility variance": 0.25,
    }
)

rows.append(
    {
        "name": "Guided\nproofreading",
        "Enthusiasm": 4,
        "Enthusiasm variance": 1,
        "Significance": 4,
        "Significance variance": 1,
        "Feasibility": 3,
        "Feasibility variance": 2,
    }
)

df = pd.DataFrame(rows)

# make 3 subplots, one for each axis of evaluation
# for each subplot, plot points and error bars for each project idea row
# color the points according to the project idea

fig, ax = plt.subplots(1, 3, figsize=(10, 5), constrained_layout=True)

colors = sns.color_palette("deep", 3)

for i, axis in enumerate(["Enthusiasm", "Significance", "Feasibility"]):
    for j, row in df.iterrows():
        ax[i].errorbar(
            row["name"],
            row[axis],
            yerr=row[axis + " variance"],
            fmt="o",
            capsize=5,
            color=colors[j],
        )

    ax[i].set_ylabel(axis)
    ax[i].set_xlabel("Project family")
    # set horizontal alignment for x-axis labels
    ax[i].set_xticklabels(
        ax[i].get_xticklabels(), horizontalalignment="right", rotation=45
    )
    ax[i].set_ylim(0, 6)
    ax[i].set_yticks([1, 2, 3, 4, 5])
    ax[i].set_xlim([-0.5, 2.5])

fig.suptitle("Qualitative evaluation of project ideas")
fig.savefig(
    "results/figs/edit_retrospective_evaluation/retrospective_evaluation.png", dpi=300
)

# %%

