# Experimental Summary

## Evaluation Results

| Experiment | Mean Dice | TC | WT | ET |
|---|---:|---:|---:|---:|
| Baseline | 0.7553 | 0.8044 | 0.9006 | 0.5610 |
| DiceCELoss | 0.7564 | 0.8057 | 0.8950 | 0.5686 |
| pixdim=(1.5,1.5,1.5) | 0.6870 | 0.7083 | 0.8663 | 0.4862 |
| nearest | 0.7521 | 0.7983 | 0.8999 | 0.5582 |

---

## Key Findings

Among the evaluated parameters,
voxel spacing had the largest impact
on segmentation performance.

Increasing pixdim from (1.0,1.0,1.0)
to (1.5,1.5,1.5) significantly degraded
all segmentation metrics,
especially for smaller tumor regions.

DiceCELoss produced modest improvements,
mainly for ET segmentation,
while interpolation mode changes showed
limited impact under the current configuration.

---

## Observations

### DiceCELoss

DiceCELoss slightly improved ET segmentation
compared with the baseline configuration.

This suggests that adding CrossEntropy supervision
may help optimization for small and difficult regions.

However, the overall improvement magnitude remained limited.

---

### Spacing Comparison

Increasing voxel spacing caused the largest degradation
among all evaluated parameters.

Performance degradation was especially large for:

- TC (Tumor Core)
- ET (Enhancing Tumor)

This suggests that preserving spatial detail
is critical for small tumor structure segmentation.

---

### Interpolation Comparison

Changing interpolation mode from linear to nearest
produced only minor differences.

Compared with spacing changes,
the effect size was relatively small.

This suggests segmentation quality was more sensitive
to voxel spacing than interpolation details
under the current configuration.

---

## Detailed Reports

- experiments/01_loss_comparison.md
- experiments/02_spacing_comparison.md
- experiments/03_interpolation_comparison.md

---

## Figures

Training curves and visualization results are available in:

- figures/
