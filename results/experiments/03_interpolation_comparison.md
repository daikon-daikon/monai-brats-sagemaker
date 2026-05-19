# Experiment 03 — Interpolation Comparison

## Objective

Evaluate the impact of interpolation mode
on segmentation performance.

---

## Compared Settings

| Setting | Interpolation |
|---|---|
| Baseline | linear |
| Compare | nearest |

---

## Results

| Interpolation | Mean Dice | TC | WT | ET |
|---|---:|---:|---:|---:|
| linear | 0.7553 | 0.8044 | 0.9006 | 0.5610 |
| nearest | 0.7521 | 0.7983 | 0.8999 | 0.5582 |

---

## Discussion

Interpolation mode changes produced
only limited performance differences.

Possible interpretation:

- The preprocessing pipeline was already stable
- Segmentation quality was more sensitive
  to voxel spacing than interpolation details

Unlike the spacing experiment,
large degradation was not observed.

---

## Conclusion

Interpolation mode alone had relatively small impact
under the current configuration.
