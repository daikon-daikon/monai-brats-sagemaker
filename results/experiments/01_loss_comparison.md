# Experiment 01 — DiceLoss vs DiceCELoss

## Objective

Evaluate the impact of loss function selection
on segmentation performance.

---

## Compared Settings

| Setting | Loss |
|---|---|
| Baseline | DiceLoss |
| Compare | DiceCELoss |

---

## Results

| Loss | Mean Dice | TC | WT | ET |
|---|---:|---:|---:|---:|
| DiceLoss | 0.7553 | 0.8044 | 0.9006 | 0.5610 |
| DiceCELoss | 0.7564 | 0.8057 | 0.8950 | 0.5686 |

---

## Discussion

DiceCELoss produced modest improvements,
especially for ET segmentation.

Possible interpretation:

- CrossEntropy provides voxel-wise supervision
- Small tumor regions may benefit from
  stronger classification gradients

However, the overall improvement was limited,
suggesting that preprocessing configuration
had larger influence than loss selection alone.

---

## Conclusion

Loss function changes slightly improved
optimization behavior,
but the overall effect size remained modest.
