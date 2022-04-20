#!/bin/bash

# using Korolos' reply on this forum:
# https://superuser.com/questions/384967/add-a-header-to-every-page-in-a-pdf

for filename in ./pdfs/*.pdf; do
    pdftk $filename background ./footer/footer_page.pdf output ./pdfs_footers/`basename "$filename"`
done
