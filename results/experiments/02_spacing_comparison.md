# Experiment 02 — Spacing Comparison

## Objective

Evaluate the impact of voxel spacing
on segmentation performance.

---

## Compared Settings

| Setting | pixdim |
|---|---|
| Baseline | (1.0,1.0,1.0) |
| Compare | (1.5,1.5,1.5) |

---

## Results

| pixdim | Mean Dice | TC | WT | ET |
|---|---:|---:|---:|---:|
| 1.0mm | 0.7553 | 0.8044 | 0.9006 | 0.5610 |
| 1.5mm | 0.6870 | 0.7083 | 0.8663 | 0.4862 |

---

## Discussion

Increasing voxel spacing significantly degraded
all segmentation metrics.

The degradation was especially large
for ET and TC regions.

Possible interpretation:

- Larger spacing reduced spatial detail
- Small tumor structures became harder to preserve
- Boundary information was partially lost

Validation stability also became worse,
suggesting that coarse spatial resolution
increased prediction instability.

---

## Conclusion

Voxel spacing had the largest impact
among all evaluated parameters.

This experiment demonstrates the importance
of preserving spatial detail
in 3D medical image segmentation.
