# Assignment Summary

The final project was to implement a console application for managing pizza shops and answering spatial queries using manually implemented data structures in C++.

## Required Operations

- `Add-N`: add a rectangular neighborhood by name and corner coordinates.
- `Add-P`: add a main pizza shop at a unique point.
- `Add-Br`: add a branch associated with a main pizza shop.
- `Del-Br`: delete a branch by coordinates while preventing deletion of a main shop.
- `List-P`: list every pizza shop located inside a named neighborhood.
- `List-Brs`: list the coordinates of every branch belonging to a named main shop.
- `Near-P`: find the nearest pizza shop to a supplied point.
- `Near-Br`: find the nearest branch of a selected pizza shop.
- `Avail-P`: list all pizza shops within radius `R` of a supplied point.
- `Most-Brs`: report the main pizza shop with the greatest number of branches.

## Data-Structure Requirements

- Implement a two-dimensional KD-tree for spatial organization and queries.
- Use an efficient custom hash structure for name-based lookup.
- Follow object-oriented and multi-file C++ design.
- Avoid ready-made algorithmic and data-structure implementations for the core solution.
- Keep the console application reasonably efficient and understandable for an in-person project demonstration.

## Optional Extension

The bonus `Undo` command would restore application state to a selected earlier command, including commands entered together using `&&`. The assignment suggested a hash structure with linked-list chaining for this extension.

Groups were limited to two students. The original Persian specification is preserved in `reference-material/assignment-specification-fa.pdf`.
