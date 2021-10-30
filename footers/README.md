## Footers

This is a simple script to add footers to SEMDIAL's PDFs.

### Requirements

You must have [pdftk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)
installed.

### Adding footers to the PDFs of a new year

Make sure that `semdial-proceedings/footers/pdfs` and `semdial-proceedings/footers/pdfs_footers`
are empty.

Put all new PDFS (front matter, invited talks, papers, posters) in `semdial-proceedings/footers/pdfs`.

Then, open the .tex file `footer/footer_page.tex`, edit the necessary
information (edition, date and location) about the new SEMDIAL and compile it.
This will generate a blank page with the footer.

Finally, run:

`sh add_footers.sh`

The PDFs with the footers will be on the directory `semdial-proceedings/footers/pdfs_footers`.

You can use them to build the website (see README on `semdial-proceedings/`).

### Proceedings

The full proceedings PDF should have the same footer. You can add it to the LaTeX
file using the following commands:

```
\usepackage{fancyhdr}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[CO]{\thepage \\ \textit{\small Proceedings of the XXth Workshop on the Semantics and Pragmatics of Dialogue, Month, XX–XX, YEAR, PLACE.}}
\pagestyle{fancy}
```
(adapted from [here](https://askubuntu.com/questions/712691/batch-add-header-footer-to-pdf-files)).
