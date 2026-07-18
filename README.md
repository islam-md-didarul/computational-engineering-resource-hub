<div align="center">

# Computational Engineering Resource Hub

**A curated, repository-first learning hub for computational engineering.**

Programming · Numerical methods · Mathematics · CFD · FEA · HPC · Scientific AI · Optimization · Research

[![Resources](https://img.shields.io/badge/resources-58-0969da?style=for-the-badge)](#resource-library)
[![Categories](https://img.shields.io/badge/categories-10-8250df?style=for-the-badge)](#explore-by-category)
[![License: MIT](https://img.shields.io/badge/license-MIT-1f883d?style=for-the-badge)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-f59e0b?style=for-the-badge)](CONTRIBUTING.md)

</div>

> [!NOTE]
> This repository is designed to be read directly on GitHub. No separate GitHub Pages website is required.

## Overview

Computational engineering combines mathematical modeling, numerical algorithms, scientific software, high-performance computing, and domain knowledge. This repository organizes reliable learning materials into a practical path from foundations to advanced simulation and scientific AI.

**Use it to:**

- build a structured self-study plan;
- locate official courses, books, documentation, and tutorials;
- strengthen CFD, FEA, numerical methods, HPC, optimization, and research skills;
- suggest or review new resources through issues and pull requests.

## Quick navigation

| Start here | Explore | Contribute |
|---|---|---|
| [Learning roadmap](#learning-roadmap) | [Resource library](#resource-library) | [Contribution guide](CONTRIBUTING.md) |
| [Featured resources](#featured-starting-points) | [Categories](#explore-by-category) | [Suggest a resource](https://github.com/islam-md-didarul/computational-engineering-resource-hub/issues/new?template=resource-suggestion.yml) |
| [Repository structure](#repository-structure) | [Selection criteria](docs/resource-guidelines.md) | [Report a problem](https://github.com/islam-md-didarul/computational-engineering-resource-hub/issues/new) |

## Featured starting points

- **[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)** — Practical command-line, shell, Git, editor, debugging, and automation skills that engineering courses often assume.
- **[Python Programming and Numerical Methods](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html)** — Engineering-oriented Python examples covering numerical differentiation, integration, roots, linear algebra, and differential equations.
- **[Fundamentals of Numerical Computation](https://fncbook.com/)** — An open text combining numerical analysis, computational experiments, and implementations in multiple languages.
- **[Essence of Calculus](https://www.3blue1brown.com/topics/calculus)** — Visual intuition for derivatives, integrals, limits, Taylor series, and the fundamental theorem of calculus.
- **[Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)** — A geometric introduction to vectors, matrices, determinants, eigenvectors, and changes of basis.
- **[MIT Fluid Dynamics](https://ocw.mit.edu/courses/2-06-fluid-dynamics-spring-2013/)** — Core fluid dynamics topics including conservation laws, dimensional analysis, viscous flow, boundary layers, and waves.
- **[CFD Direct: Notes on CFD](https://doc.cfd.direct/notes/cfd-general-principles/)** — A compact treatment of finite-volume discretization, transport equations, solution algorithms, and practical CFD principles.
- **[OpenFOAM Documentation](https://doc.openfoam.com/)** — User guides, solver references, models, boundary conditions, meshing workflows, and tutorials for OpenFOAM.

## Learning roadmap

| Stage | Focus | Practical milestone |
|---:|---|---|
| **1** | Computing foundations | Create a reproducible repository that reads data, performs a calculation, and produces a figure. |
| **2** | Mathematical foundations | Implement and compare methods for a linear system or ordinary differential equation. |
| **3** | Numerical methods | Solve a canonical diffusion, advection, or Poisson problem and perform grid convergence. |
| **4** | Domain simulation | Reproduce a published CFD, FEA, heat-transfer, or multiphysics benchmark. |
| **5** | Scale and acceleration | Profile and parallelize a solver or post-processing workflow; report scaling. |
| **6** | Optimization and scientific AI | Compare an optimized design or data-driven surrogate against a trusted numerical baseline. |
| **7** | Reproducible research | Publish data, code, environment details, figures, documentation, and a citable release. |

Read the expanded guide: **[Computational Engineering Learning Roadmap](docs/learning-roadmap.md)**.

## Resource library

Each section can be expanded independently. Access labels reflect the information stored in [`data/resources.json`](data/resources.json).

<!-- RESOURCE_LIBRARY_START -->

<a id="programming-tools"></a>
<details>
<summary><strong>🧰 Programming & Tools</strong> — 8 resources</summary>

Scientific programming, version control, Linux, debugging, and developer workflows.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[The Missing Semester of Your CS Education](https://missing.csail.mit.edu/)** ⭐ | Beginner | Course | ✅ Free | Practical command-line, shell, Git, editor, debugging, and automation skills that engineering courses often assume. |
| **[Learn Git Branching](https://learngitbranching.js.org/)** | Beginner | Interactive | ✅ Free | A visual, browser-based way to practice commits, branches, merging, rebasing, and remote workflows. |
| **[Pro Git](https://git-scm.com/book/en/v2)** | Intermediate | Book | ✅ Free | The comprehensive reference for Git concepts, collaboration patterns, internals, and advanced workflows. |
| **[Official Python Tutorial](https://docs.python.org/3/tutorial/)** | Beginner | Documentation | ✅ Free | A direct introduction to Python syntax, data structures, modules, classes, errors, and standard-library fundamentals. |
| **[LearnCpp](https://www.learncpp.com/)** | Beginner | Tutorial | ✅ Free | A structured path through modern C++ for students preparing for simulation software and high-performance computing. |
| **[MATLAB Onramp](https://matlabacademy.mathworks.com/details/matlab-onramp/gettingstarted)** | Beginner | Interactive | ✅ Free | A short interactive introduction to MATLAB arrays, scripts, plotting, data import, and basic programming. |
| **[Visual Studio Code Documentation](https://code.visualstudio.com/docs)** | Beginner | Documentation | ✅ Free | Setup and workflow guidance for editing, debugging, remote development, notebooks, terminals, and extensions. |
| **[Project Jupyter](https://jupyter.org/try)** | Beginner | Interactive | ✅ Free | Try notebook-based scientific computing in the browser and learn reproducible computational narratives. |

</details>

<a id="numerical-methods"></a>
<details>
<summary><strong>🔢 Numerical Methods</strong> — 4 resources</summary>

Algorithms for solving equations, ODEs, PDEs, interpolation, integration, and numerical error.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[Python Programming and Numerical Methods](https://pythonnumericalmethods.studentorg.berkeley.edu/notebooks/Index.html)** ⭐ | Beginner | Book | ✅ Free | Engineering-oriented Python examples covering numerical differentiation, integration, roots, linear algebra, and differential equations. |
| **[Fundamentals of Numerical Computation](https://fncbook.com/)** ⭐ | Intermediate | Book | ✅ Free | An open text combining numerical analysis, computational experiments, and implementations in multiple languages. |
| **[Numerical Recipes Code Resources](https://numerical.recipes/)** | Advanced | Reference | ◐ Mixed/Paid | A broad map of classical numerical algorithms and implementation patterns for scientific applications. |
| **[SciPy Lecture Notes](https://scipy-lectures.org/)** | Intermediate | Course | ✅ Free | A practical scientific Python curriculum using NumPy, SciPy, Matplotlib, image processing, and optimization. |

</details>

<a id="mathematics"></a>
<details>
<summary><strong>📐 Mathematics</strong> — 6 resources</summary>

Calculus, linear algebra, differential equations, probability, and mathematical foundations.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[Essence of Calculus](https://www.3blue1brown.com/topics/calculus)** ⭐ | Beginner | Video Series | ✅ Free | Visual intuition for derivatives, integrals, limits, Taylor series, and the fundamental theorem of calculus. |
| **[Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)** ⭐ | Beginner | Video Series | ✅ Free | A geometric introduction to vectors, matrices, determinants, eigenvectors, and changes of basis. |
| **[MIT 18.06 Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)** | Intermediate | Course | ✅ Free | Gilbert Strang's complete course on vector spaces, factorization, least squares, eigenvalues, and applications. |
| **[Book of Proof](https://www.people.vcu.edu/~rhammack/BookOfProof/)** | Beginner | Book | ✅ Free | A freely available introduction to logic, sets, relations, functions, induction, and proof techniques. |
| **[Seeing Theory](https://seeing-theory.brown.edu/)** | Beginner | Interactive | ✅ Free | Interactive visual explanations of probability, distributions, inference, regression, and Bayesian ideas. |
| **[MIT Differential Equations](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/)** | Intermediate | Course | ✅ Free | A full course on ordinary differential equations, linear systems, Fourier methods, and modeling. |

</details>

<a id="physics-mechanics"></a>
<details>
<summary><strong>⚙️ Physics & Mechanics</strong> — 4 resources</summary>

Fluid dynamics, thermodynamics, statics, dynamics, and continuum-mechanics foundations.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[MIT Fluid Dynamics](https://ocw.mit.edu/courses/2-06-fluid-dynamics-spring-2013/)** ⭐ | Intermediate | Course | ✅ Free | Core fluid dynamics topics including conservation laws, dimensional analysis, viscous flow, boundary layers, and waves. |
| **[MIT Thermodynamics](https://ocw.mit.edu/courses/2-05-thermodynamics-fall-2013/)** | Intermediate | Course | ✅ Free | Engineering thermodynamics with property relations, cycles, entropy, equilibrium, and energy conversion. |
| **[Engineering Statics](https://engineeringstatics.org/)** | Beginner | Book | ✅ Free | An open mechanics text covering force systems, equilibrium, structures, friction, and centroids. |
| **[The Efficient Engineer: Stress and Strain](https://www.youtube.com/watch?v=KzZjcqj53o8)** | Beginner | Video | ✅ Free | A concise visual introduction to normal and shear stress, strain, constitutive behavior, and deformation. |

</details>

<a id="cfd-fluid-mechanics"></a>
<details>
<summary><strong>🌊 CFD & Fluid Mechanics</strong> — 7 resources</summary>

Finite-volume methods, CFD theory, OpenFOAM, SU2, verification, and turbulence modeling.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[CFD Direct: Notes on CFD](https://doc.cfd.direct/notes/cfd-general-principles/)** ⭐ | Intermediate | Notes | ✅ Free | A compact treatment of finite-volume discretization, transport equations, solution algorithms, and practical CFD principles. |
| **[OpenFOAM Documentation](https://doc.openfoam.com/)** ⭐ | Intermediate | Documentation | ✅ Free | User guides, solver references, models, boundary conditions, meshing workflows, and tutorials for OpenFOAM. |
| **[SU2 Documentation](https://su2code.github.io/docs/)** | Intermediate | Documentation | ✅ Free | Documentation and tutorials for open-source multiphysics simulation, CFD, adjoint methods, and design optimization. |
| **[NASA Turbulence Modeling Resource](https://turbmodels.larc.nasa.gov/)** ⭐ | Advanced | Reference | ✅ Free | Verified equations, implementation notes, and benchmark cases for widely used RANS turbulence models. |
| **[Gmsh Reference Manual](https://gmsh.info/doc/texinfo/gmsh.html)** | Intermediate | Documentation | ✅ Free | Geometry, mesh generation, scripting, field control, and API documentation for the Gmsh mesher. |
| **[ParaView Tutorials](https://docs.paraview.org/en/latest/Tutorials/index.html)** | Beginner | Tutorial | ✅ Free | Guided post-processing workflows for filters, slices, streamlines, plots, animation, and parallel visualization. |
| **[PyFR Documentation](https://pyfr.readthedocs.io/en/latest/)** | Advanced | Documentation | ✅ Free | High-order flux-reconstruction CFD workflows designed for modern CPUs, GPUs, and heterogeneous systems. |

</details>

<a id="fea-solid-mechanics"></a>
<details>
<summary><strong>🏗️ FEA & Solid Mechanics</strong> — 4 resources</summary>

Finite-element methods, structural mechanics, open-source solvers, and practical tutorials.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[FEniCSx Tutorial](https://jsdokken.com/dolfinx-tutorial/)** ⭐ | Intermediate | Tutorial | ✅ Free | Hands-on finite-element examples using DOLFINx, UFL, meshes, boundary conditions, solvers, and parallel execution. |
| **[deal.II Tutorial Programs](https://www.dealii.org/current/doxygen/deal.II/Tutorial.html)** | Advanced | Tutorial | ✅ Free | Progressive C++ examples for finite-element discretization, adaptivity, multiphysics, and scalable solvers. |
| **[MFEM Examples](https://mfem.org/examples/)** | Advanced | Examples | ✅ Free | Compact examples of high-order finite-element methods, parallel meshes, solvers, and multiphysics applications. |
| **[SfePy Documentation](https://sfepy.org/doc-devel/index.html)** | Intermediate | Documentation | ✅ Free | Python-based finite-element modeling for coupled PDEs, materials, boundary conditions, and custom weak forms. |

</details>

<a id="hpc-parallel-computing"></a>
<details>
<summary><strong>🚀 HPC & Parallel Computing</strong> — 6 resources</summary>

MPI, OpenMP, GPU programming, performance engineering, and scalable scientific computing.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[LLNL HPC Tutorials](https://hpc-tutorials.llnl.gov/)** ⭐ | Intermediate | Course | ✅ Free | Practical tutorials on MPI, OpenMP, pthreads, GPU programming, performance analysis, and parallel design. |
| **[MPI Tutorial](https://mpitutorial.com/tutorials/)** | Intermediate | Tutorial | ✅ Free | An approachable sequence covering point-to-point communication, collectives, groups, communicators, and examples. |
| **[OpenMP Tutorials and Articles](https://www.openmp.org/resources/tutorials-articles/)** | Intermediate | Tutorial | ✅ Free | Official learning resources for shared-memory parallelism, directives, tasks, offloading, and performance. |
| **[CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)** | Advanced | Documentation | ✅ Free | The core reference for CUDA execution, memory models, kernels, synchronization, optimization, and GPU features. |
| **[PETSc Documentation](https://petsc.org/release/)** ⭐ | Advanced | Documentation | ✅ Free | Scalable linear and nonlinear solvers, time integrators, optimization tools, and preconditioners for PDE applications. |
| **[Kokkos Core Documentation](https://kokkos.org/kokkos-core-wiki/)** | Advanced | Documentation | ✅ Free | Performance-portable C++ abstractions for parallel execution and memory across CPUs and GPUs. |

</details>

<a id="data-ml-scientific-ai"></a>
<details>
<summary><strong>🧠 Data, ML & Scientific AI</strong> — 8 resources</summary>

Scientific Python, machine learning, differentiable computing, PINNs, and operator learning.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[NumPy Learning Resources](https://numpy.org/learn/)** | Beginner | Tutorial | ✅ Free | Curated paths for array computing, vectorization, broadcasting, linear algebra, and scientific Python workflows. |
| **[PyTorch Tutorials](https://docs.pytorch.org/tutorials/)** ⭐ | Intermediate | Tutorial | ✅ Free | Official tutorials for tensors, neural networks, data pipelines, training, deployment, and distributed learning. |
| **[JAX Quickstart](https://docs.jax.dev/en/latest/notebooks/quickstart.html)** | Intermediate | Tutorial | ✅ Free | A compact introduction to accelerated NumPy-style computing, automatic differentiation, JIT compilation, and vectorization. |
| **[Physics-based Deep Learning](https://physicsbaseddeeplearning.org/)** ⭐ | Advanced | Book | ✅ Free | A broad guide to combining numerical simulation, differentiable physics, surrogate modeling, and deep learning. |
| **[NeuralOperator Documentation](https://neuraloperator.github.io/dev/)** | Advanced | Documentation | ✅ Free | Implementations and guides for Fourier neural operators and related operator-learning architectures. |
| **[DeepXDE Documentation](https://deepxde.readthedocs.io/)** | Advanced | Documentation | ✅ Free | Physics-informed and operator-learning workflows for differential equations, inverse problems, and uncertainty. |
| **[Data-Driven Science and Engineering](https://www.databookuw.com/)** ⭐ | Advanced | Book | ✅ Free | Resources on singular value decomposition, sparse modeling, dynamic mode decomposition, Koopman analysis, and control. |
| **[CS229 Machine Learning Lectures](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)** | Intermediate | Video Series | ✅ Free | A rigorous introduction to supervised learning, probabilistic models, kernels, neural networks, and learning theory. |

</details>

<a id="optimization-control"></a>
<details>
<summary><strong>🎯 Optimization & Control</strong> — 6 resources</summary>

Design optimization, convex methods, multidisciplinary optimization, and dynamical systems.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[Algorithms for Optimization](https://algorithmsbook.com/optimization/)** ⭐ | Intermediate | Book | ✅ Free | A readable introduction to derivative-based, derivative-free, stochastic, and constrained optimization methods. |
| **[Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/)** | Advanced | Book | ✅ Free | The standard open reference for convex sets, duality, optimality, numerical methods, and engineering applications. |
| **[OpenMDAO Documentation](https://openmdao.org/newdocs/versions/latest/main.html)** ⭐ | Advanced | Documentation | ✅ Free | A framework for multidisciplinary analysis and optimization with derivatives, coupled systems, and scalable workflows. |
| **[CasADi Documentation](https://web.casadi.org/docs/)** | Advanced | Documentation | ✅ Free | Symbolic-numeric tools for automatic differentiation, nonlinear optimization, and optimal control. |
| **[Underactuated Robotics](https://underactuated.csail.mit.edu/)** | Advanced | Course | ✅ Free | Nonlinear dynamics, planning, estimation, and control through robotics examples and computational exercises. |
| **[Python Control Systems Library](https://python-control.readthedocs.io/)** | Intermediate | Documentation | ✅ Free | Python tools for state-space models, transfer functions, frequency response, stability, estimation, and design. |

</details>

<a id="research-workflow"></a>
<details>
<summary><strong>🔬 Research Workflow</strong> — 5 resources</summary>

Reproducibility, scientific writing, data management, citation, and collaborative research practice.

| Resource | Level | Format | Access | Description |
|---|---|---|---|---|
| **[The Turing Way](https://book.the-turing-way.org/)** ⭐ | Beginner | Handbook | ✅ Free | A community handbook for reproducible, ethical, collaborative, and inclusive data-intensive research. |
| **[Software Carpentry Lessons](https://software-carpentry.org/lessons/)** | Beginner | Course | ✅ Free | Foundational lessons in shell use, version control, Python or R, and research-oriented data workflows. |
| **[Overleaf Learn](https://www.overleaf.com/learn)** | Beginner | Documentation | ✅ Free | Practical guidance for LaTeX documents, equations, references, figures, tables, and collaborative writing. |
| **[Zotero Documentation](https://www.zotero.org/support/)** | Beginner | Documentation | ✅ Free | Reference-management workflows for collecting papers, organizing libraries, annotating PDFs, and generating citations. |
| **[GitHub Skills](https://skills.github.com/)** | Beginner | Interactive | ✅ Free | Short hands-on courses for repositories, pull requests, Actions, Pages, Markdown, and collaborative development. |

</details>

<!-- RESOURCE_LIBRARY_END -->

## How resources are selected

Resources are prioritized when they are authoritative, educational, technically relevant, legally accessible, and reasonably maintained. Official documentation, university courses, open textbooks, and primary educational sources are preferred.

See **[Resource Guidelines](docs/resource-guidelines.md)** for the full review criteria.

## Contributing

New resources, corrections, and broken-link reports are welcome.

1. Open the **[resource suggestion form](https://github.com/islam-md-didarul/computational-engineering-resource-hub/issues/new?template=resource-suggestion.yml)**, or fork the repository.
2. Add or update the entry in [`data/resources.json`](data/resources.json).
3. Run the validation and README-generation scripts.
4. Submit a pull request explaining the value of the change.

```bash
python scripts/validate_resources.py
python scripts/generate_readme.py
```

Read **[CONTRIBUTING.md](CONTRIBUTING.md)** before submitting a pull request.

## Citation

Use the repository’s **Cite this repository** menu or the metadata in [`CITATION.cff`](CITATION.cff).

## License

Repository code and original documentation are released under the [MIT License](LICENSE). Linked external materials remain subject to the terms and licenses of their respective owners.

## Acknowledgment

This repository is an original GitHub-native implementation inspired by the category-based organization of [Computational Engineering Resources](https://yashj1579.github.io/blog/computational-engineering-resources/).

---

<div align="center">

**Maintained by [Md. Didarul Islam](https://github.com/islam-md-didarul)**

⭐ Star the repository if it supports your learning or research.

</div>
