# KD-Tree Pizza-Shop Locator

A console-based spatial search application developed for the final project of the Data Structures course at Isfahan University of Technology. The project was completed during the 2023-2024 academic year.

## Academic Context

The assignment required students to implement the core data structures manually in C++, without using ready-made algorithmic or data-structure libraries for the main solution.

This was a two-member group project with equal participation. Both members contributed across the design and implementation of the complete project rather than owning isolated components.

## Implemented Concepts

- A two-dimensional KD-tree built by alternating the x and y axes
- Recursive nearest-neighbor search
- Name-based lookup using a fixed-size custom hash table with collision probing
- Object-oriented models for main shops, branches, points, and neighborhoods
- Geometric checks for listing shops located inside a neighborhood
- Radius-based availability queries
- Branch creation, deletion, listing, and maximum-branch queries

## Supported Operations

- Add a neighborhood
- Add a main pizza shop or a branch
- Delete a branch by coordinates
- List shops inside a neighborhood
- List every branch associated with a main shop
- Find the nearest shop
- Find the nearest branch of a selected shop
- List shops within a requested radius
- Report the shop with the largest number of branches

## Repository Layout

- `original-submission/` contains the original multi-file C++ and Visual Studio project files.
- `prompt.md` provides an English summary of the assignment.
- `reference-material/` contains the original Persian assignment specification.
- `archival-build-fix.patch` contains one documented forward-declaration fix used only to verify compilation during archival.

The machine-specific Visual Studio `.vcxproj.user` file was intentionally omitted.

## Building

The original project targets Visual Studio and the v143 platform toolset. The submitted source is preserved unchanged, including one missing forward declaration. To reproduce the portable archival build without editing the archived file manually, work on a copy of `original-submission/` and apply the supplied patch:

```bash
patch --binary -p1 < ../archival-build-fix.patch

g++ -std=c++17 \
  P_DS.cpp point.cpp \
  pizza_shop_main.cpp pizza_shop_branch.cpp \
  neighbourhood.cpp tree.cpp \
  -o ds_project
```

The patched source was successfully compiled with GCC 13 during archival. Compiler warnings remain, and the historical feature behavior has not been comprehensively revalidated with an automated test suite.

## Archive Notes

This is an early undergraduate submission and is intentionally preserved without algorithmic modernization. The optional `Undo` extension described in the assignment was not implemented. The project should be read as evidence of coursework and the progression of data-structure and C++ experience, not as production-ready software.
