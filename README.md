## SEMDIAL


### Adding new a new year's proceedings

To prepare your environment for compiling the proceedings, follow the [ACL Anthology README](https://github.com/acl-org/acl-anthology) to install python requirements, and Hugo. If you are using be sure to use the extended version. On Linux, the .deb install doesn't work, so you'll need to download the [Hugh extended tar](https://github.com/gohugoio/hugo/releases/download/v0.88.1/hugo_extended_0.88.1_Linux-64bit.tar.gz) then point your PATH variable to the folder.

Clone this repository `git clone https://github.com/semdial/semdial.github.io`
Clone the proceedings compiler repository `git clone https://github.com/semdial/semdial-proceedings`

Direct your console to the `semdial-proceedings` folder.

You need to create an appropriate .xml file that contains all of the metadata and pointers to each paper. Open data/xml/Z19.xml. This is the metadata file for the 2019 SEMDIAL Workshop. There are four sections: Front Matter, Invited Talks, Full Papers, and Poster Abstracts. For example:

```
  <volume id="1">
    <meta>
      <booktitle>Proceedings of the 23rd Workshop on the Semantics and Pragmatics of Dialogue - Front Matter</booktitle>
      <editor><first>Christine</first><last>Howes</last></editor>
      <editor><first>Julian</first><last>Hough</last></editor>
       <editor><first>Casey</first><last>Kennington</last></editor>
      <publisher>SEMDIAL</publisher>
      <address>London, United Kingdom</address>
      <month>September</month>
      <year>2019</year>
    </meta>

    ...

  </volume>
```
Note that each of these has a different volume ID.

Each paper is part of a volume. Each paper has an ID, title, authors, url (and `<pages></pages>` if you have that information). For example:

```
<paper id="1"><title>Questions and Answers in Suicide Risk Assessment: A Conversation Analytic Perspective</title><author><first>Rose</first><last>McCabe</last></author><url>Z19-McCabe_semdial_0001.pdf</url></paper>
```

Please follow the url paper naming convention, which is neccesary for indexing: `Z[year]-[Last name of first author]_semdial_[paper ID].pdf`

The exception is the front matter PDF file which has the naming convention `semdial[year]_[name]_front_matter.pdf`

To add a year's proceedings, simply copy the most recent year's proceedings, rename and edit the file. For exmaple, if you are adding proceedings for 2020, you can take the Z19.xml file, copy it and rename it to Z20.xml, then make changes directly to that file. Be sure to change the collection ID, the information in the volumes, and add the paper information. Save the file in the data/xml folder along with the other .xml files.

Now, navigate back to the root `semdial-proceedings` folder.

First, add the new .xml file to the repository:

`git add .`
`git commit -m "added[year]"`
`git push origin master`

Then,

run `make clean && make`

(You may get an error like `ERROR 2019/08/30 08:57:47 [en] REF_NOT_FOUND: Ref "/volumes/W18-50.md" from page "sigs/sigdial.md": page not found`. That's because this package was copied from the ACL Anthology and some artifacts are required for this to compile, but it stops short of compiling other venue information because it doesn't exist.)

You can test your build by running `make serve` then navigating to `localhost:8000` in a browser. Your newly added year should appear under the SEMDIAL venue. However, the links to the PDFs won't work.

### Adding the PDFs

Each new PDF should correspond to the naming convention explained above.

Follow the instructions on the directory `footers/` to add footers to all new PDFs, including the full proceedings PDF.

Then, copy all of the pdf files into the newly built anthology folder in `semdial-proceedings/build/anthology` 

Navigate to the cloned `semdial.github.io` folder. Navigate further into the `anthology` folder. Move all of the PDFs out of that folder and into the newly build anthology folder (e.g., `mv *.pdf ../../semdial-proceedings/build/anthology`)

Now all of the old and the new PDFs should be in the `semdial-proceedings/build/anthology` folder.

### Updating the proceedings website

Now navigate to the `semdial.github.io` folder. Delete *all* of the folders (i.e., do not delete the files in the root folder). Now copy all of the folders from `semdial-proceedings/build` into the `semdial.github.io` folder.

From `semdial.github.io`:

`git add .`
`git commit -m "adding [year]'s proceedings"`
`git push origin master`

It will take a few minutes to compile the new website, but check `sigdial.org` to make sure your new proceedings show up and that the links to the PDFs are all in order.

### Additional files

For years 2013-2019, the SEMDIAL organizers used a .tex template for generating a PDF with the complete proceedings. The template can be found in the `semdial_proceedings_code` folder. The Makefil can be used to compile the full proceedings.

**We recommend that you compile the full proceedings using the `semdial_proceedings_code`, then use the `semdial_to_act.py` script to convert from that .tex file to the XML (in the std out) and renames the PDF files, and derive the front matter PDF.
