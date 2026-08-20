# Credit Risk Classification

This three-person final course project explores whether a loan applicant is likely to default. The intended use case is preliminary credit-risk analysis for banks and financial institutions. The project was presented in class through a Jupyter Notebook containing code, explanations, plots, and saved model outputs.

## Archived deliverables

- `notebook/credit-risk-classification.ipynb`: original submitted analysis with saved outputs
- `documentation/presentation-feedback-response-fa.pdf`: Persian response to presentation feedback and requested revisions
- `data/README.md`: record of the missing source dataset
- `requirements.txt`: reconstructed list of the main Python dependencies; original versions were not recorded

## Dataset recorded by the notebook

The missing file was named `credit_risk_dataset.csv`. Saved notebook outputs describe it as containing 32,581 rows and 12 columns, including applicant age and income, home ownership, employment length, loan purpose and grade, amount and interest rate, loan-to-income percentage, credit history, prior default status, and the binary `loan_status` target.

The target distribution is imbalanced: approximately 21.8% of records belong to the default class. This makes metrics beyond raw accuracy important.

## Workflow

1. Inspect dimensions, data types, descriptive statistics, missing values, and categorical distributions.
2. Visualize numeric relationships, feature distributions, and box plots.
3. Fill missing employment length with the median and missing interest rate with the mean.
4. Encode categorical variables, remove duplicate records, and filter selected outliers.
5. Engineer age and income groups plus ratio-based features.
6. Train an unpruned Decision Tree and inspect feature importance.
7. Apply cost-complexity post-pruning and select a `ccp_alpha` value.
8. Train an RBF-kernel SVM while exploring `C` and `gamma` values.
9. Compare saved confusion matrices and accuracy visualizations.

## Saved results

These values are preserved outputs from the submitted notebook; they were not independently reproduced because the CSV file is missing.

| Model | Training accuracy | Test accuracy |
| --- | ---: | ---: |
| Unpruned Decision Tree | 99.63% | 88.42% |
| Pruned Decision Tree | 92.65% | 91.99% |
| RBF SVM (`C=4`, `gamma=0.1`) | 91.61% | 84.76% |

The saved Decision Tree confusion matrix is `[[7501, 106], [673, 1440]]`; the saved SVM confusion matrix is `[[7268, 339], [1142, 971]]`. On these outputs, the pruned Decision Tree detects substantially more positive default cases than the SVM.

## Archival verification

- The source ZIP passed integrity testing.
- The notebook is valid JSON and contains 71 cells: 46 code cells and 25 Markdown cells.
- It preserves 23 embedded PNG plots and contains no stored exception outputs.
- The feedback PDF rendered successfully and was visually inspected.
- The notebook was not re-executed because its required CSV dataset was not supplied.

## Known limitations

- The dataset file, original source URL, and license are unknown, so an external substitute was not added.
- The notebook loads the data from an absolute Windows path and is not portable as submitted.
- Cell execution counts are out of order, and at least one missing-value output is inconsistent with the preceding cells, indicating stale or selectively rerun outputs.
- Hyperparameters are selected using test-set accuracy rather than a validation split or cross-validation, which leaks test information into model selection.
- Nominal categories are label-encoded, and numeric inputs are not scaled before SVM training.
- The class distribution is imbalanced, but the comparison emphasizes accuracy and does not report precision, recall, F1 score, ROC-AUC, or PR-AUC.
- The final comparison cell manually embeds confusion-matrix values instead of deriving them from the model variables.
- Several outlier thresholds and feature removals are heuristic and not fully justified.
- `loan_to_income_ratio` largely duplicates the existing `loan_percent_income` feature.
- The plotted Decision Tree uses the full DataFrame column list instead of `X.columns`, so displayed split labels may be incorrect.

## Team attribution and portfolio guidance

- **Work type:** Collaborative, three-person project
- **Presentation:** Delivered in class and revised in response to feedback
- **Individual contribution:** Not documented in the supplied files

This project is appropriate for a coursework archive and can support claims of introductory classification, visualization, and group-presentation experience. It should not be described as sole work or used as the primary machine-learning project in a portfolio without a reproducible dataset and methodological revision.
