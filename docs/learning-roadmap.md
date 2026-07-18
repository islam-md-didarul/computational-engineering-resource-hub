# Computational Engineering Learning Roadmap

This roadmap is a suggested sequence rather than a rigid curriculum.

## Stage 1 — Computing foundations

Learn one scientific programming language well, preferably Python for rapid scientific work or C++ for high-performance software. Practice Git, the shell, debugging, notebooks, and project organization.

**Milestone:** build a small repository that reads data, performs a calculation, creates a figure, and includes reproducible instructions.

## Stage 2 — Mathematical foundations

Develop working knowledge of calculus, linear algebra, ordinary differential equations, probability, and numerical error. Focus on translating equations into algorithms and interpreting conditioning and stability.

**Milestone:** implement and compare direct and iterative methods for a small linear system or ODE problem.

## Stage 3 — Numerical methods

Study interpolation, quadrature, root finding, time integration, discretization, and the finite-difference, finite-volume, or finite-element method. Learn verification before moving to complex applications.

**Milestone:** solve a canonical diffusion, advection, or Poisson problem and perform a grid-convergence study.

## Stage 4 — Domain simulation

Choose a domain such as CFD, solid mechanics, heat transfer, electromagnetics, or multiphysics. Learn geometry preparation, mesh quality, boundary conditions, solver controls, validation, and post-processing.

**Milestone:** reproduce a published benchmark with documented assumptions and error measures.

## Stage 5 — Scale and acceleration

Learn profiling, vectorization, sparse storage, preconditioning, MPI, OpenMP, GPUs, and performance portability. Optimize only after measuring bottlenecks.

**Milestone:** parallelize a solver or post-processing workflow and report strong or weak scaling.

## Stage 6 — Optimization and scientific AI

Add design optimization, uncertainty quantification, reduced-order modeling, system identification, physics-informed learning, or operator learning. Maintain physical constraints and independent validation.

**Milestone:** compare a data-driven surrogate against a trusted numerical baseline on unseen cases.

## Stage 7 — Reproducible research

Package data, scripts, environments, figures, and documentation so another person can reproduce the result. Use version control, automated checks, persistent identifiers, and clear licensing.

**Milestone:** publish a complete computational study with a release, citation file, and archived dataset.
