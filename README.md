# MONAI BraTS 3D Segmentation on Amazon SageMaker
## Overview
This repository is a portfolio project based on the MONAI BraTS 3D Segmentation workflow,
focused on experimentation, reproducibility, and structured ML workflows
using Amazon SageMaker Training Jobs.

Rather than simply running a notebook, this project focuses on:
- Converting notebook workflows into SageMaker Training Jobs
- Reproducible experiment management
- Refactoring notebook code into reusable Python modules
- Visualization and comparison of experiment results
- Operational considerations using CloudWatch and Amazon S3
- Handling GPU memory limitations


## Tech Stack
- Python
- PyTorch
- MONAI
- AWS SageMaker
- Jupyter Notebook
- Amazon S3
- Amazon CloudWatch


## Experiments
The following comparison experiments were conducted.
Experiment / Baseline / Compare
1) Loss Function / DiceLoss / DiceCELoss
2) Image Spacing / pixdim=(1.0,1.0,1.0) / pixdim=(1.5,1.5,1.5)
3) Interpolation Strategy / nearest / linear

The following comparison experiments were conducted.

| Experiment | Baseline | Compare |
|---|---|---|
| Loss Function | DiceLoss | DiceCELoss |
| Image Spacing | pixdim=(1.0,1.0,1.0) | pixdim=(1.5,1.5,1.5) |
| Interpolation Strategy | linear | nearest |


## Repository Structure

- src/  
  Python modules for training, preprocessing, and evaluation

- configs/  
  Configuration files for comparison experiments

- results/  
  Training curves, inference outputs, and comparison figures

- scripts/  
  Scripts for SageMaker Training Jobs


## Implementation Policy
This project is based on the MONAI BraTS segmentation workflow
and extended for SageMaker-based experimentation and reproducibility.
The implementation focuses on:
- Experiment management
- Code organization
- SageMaker Training Job workflows
- Reproducible ML pipelines


## Key Points
- GPU training on SageMaker Training Jobs
- Artifact management using `/opt/ml/model`
- Monitoring with CloudWatch logs
- Structured experiment comparison workflow
- Balance between notebook experimentation and production-style organization
- Running 3D segmentation workloads under GPU memory constraints


## Future Improvements
- Hydra-based configuration management
- Dockerization
- CI/CD integration
- Inference pipeline implementation
- Distributed training support


## References
- MONAI
- BraTS Dataset
- AWS SageMaker Documentation
