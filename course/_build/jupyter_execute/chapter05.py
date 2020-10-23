# Chapter 5: Metadata

![](images/metadata.png)

Credit: [Shelby HIST 390 blog](http://swilsonhistory.com/2020/02/27/lets-talk-about-metadata/)

## Metadata

In the previous chapter I consciously steered the discussion away from information models to data models. Now, we are going to do the same with information and data, or better said, metadata. A lot of what happens in information science does not have to do with information, but information *about* information, or metadata:

[Wikipedia](https://en.wikipedia.org/wiki/Metadata) says:

> Metadata is "data that provides information about other data". In other words, it is "data about data." Many distinct types of metadata exist, including descriptive metadata, structural metadata, (...)

Descriptive metadata, for instance, is descriptive information about a resource. It is used for discovery and identification. If we think about books, for example, descriptive metadata would include elements such as title, author, date of publication, etcetera. Or, Exif (Exchangeable image file format) is a metadata standard that specifies the formats for images, sound, and ancillary tags used by digital cameras (including smartphones), scanners and other systems handling image and sound files recorded by digital cameras.

## Metadata is important!

Metadata might seem trivial -- in fact, I don't like the word *ancillary* in the previous paragraph -- or non-essential. However, metadata performs a huge and crucial role in information science and software development as a whole. As a rule, applications will strictly separate the business logic of the application (e.g. invoice system) and the metadata the application uses (e.g. database of clients, suppliers, etc.), but without the latter, the former is doomed. 

Consider, as an illustration, this story about the [Samsung Blu Ray player](https://www.theregister.com/2020/07/18/samsung_bluray_mass_dieoff_explained/)!

## It's complicated

However, this definition of metadata as "data about data" somewhat misses the mark. In order to illustrate that, we need to take a look at a concrete example of metadata.

Have a look at this title page:

![](images/Lipsius.jpg)

Credit: photo: [STCV catalogue](https://anet.be/record/stcvopac/c:stcv:7081813/E), copy: [UA-CST MAG-P 13.74](https://anet.be/record/opacuantwerpen/c:lvd:452568/E) (f. *1 recto)


The STCV catalogue, which we have already mentioned a few times, catalogues this book as follows ([permalink](https://anet.be/record/stcvopac/c:stcv:7081813/E)):

Category | Metadata
--- | ---
Title |	Title page: Poliorceticωn sive De machinis. Tormentis. Telis. Libri qvinqve
Author | Title page: Ivstus Lipsius \[Lipsius, Justus]
. | External: van Veen, Otto \[Illustrator]
. | External: van der Borcht, Pieter I \[Illustrator]
Publication	| Title page: ex officina Plantiniana, apud viduam, & Ioannem Moretum \[Rivière, Jeanne & Jan I Moretus]
. | Title page: Antverpiæ \[Antwerp]
. | 1596
Language | Latin \[Target language]

Now let's compare this to the title page.

- For instance, we see that the difference between lower case, upper case and small caps has disappeared. This might seem trivial, but did you realise that in Renaissance Latin a capitalized final "I" stands for "ii"? So the full title is actually, "Ivsti Lipsii..." Or, suppose that someone is studying the use of capitalization in title layout as a marketing means. This is vital information that is missing.

- Moreover, when we focus on the title, we see small changes. Whereas the title page does not have a space between "Tormentis.Telis", the transcription does. And it also leaves out the italic parts (another piece of layout info missing!) "Ad Historiarum lucem" (In light of History) and "Cum Privilegiis Caesareo & Regio" (With Imperial and Royal Privilege). Again, such information could be very interesting to book historians.

- Also, when we look at the date, we notice this has been interpreted rather than transcribed. The Roman numeral (with the typical dots) has been silently turned into '1596'.

- Furthermore, we see that copy specific information, such as the stamp in the upper right corner and the pasted on inscription on the bottom have also been left out. 

- On the other hand, there is also more information in the descriptive metadata than is on the title page. The names of the illustrators, for instance, and the name of Christopher Plantin's widow are added.

Let's compare this with the entry in [Worldcat](http://www.worldcat.org/oclc/79260741):

Category | Metadata
--- | ---
Title | Ivsti LipsI Poliorcetic\[o]n, sive, De machinis, tormentis, telis, libri qvinqve : ad historiarum lucem.
Author | Justus Lipsius; Petrus van der Borcht
Publisher |	Antverpiæ : Ex Officina Plantiniana, apud Viduam, & Ioannem Moretum, M.D. XCVI \[1596]

The information is pretty similar, but now that we are tuned into some of the subtleties we notice the differences. "Ad historiarum lucem" is present, for instance. On the other hand, Worldcat has different capitalization and provides only one illustrator, without specifying that this is external information (i.e. not included in the title page).

This example shows that different catalogues adhere to different cataloguing rules. It is impossible to simply catalogue at book title (or indeed any item, be it physical or digital) "as is". However diplomatic and inclusive you try to be when cataloguing, you will always have to make hard decisions about how to handle layout, how to transcribe characters, whether or not to standardize spelling, punctuation, etcetera. 

All of this is perfectly understandable and in general (good) catalogues will be explicit and very scrupulous in the cataloguing rules they follow. The danger is that when we leave the cataloguing context and, for instance, acquire catalogue information in a data dump (STCV is freely available [here](https://www.uantwerpen.be/nl/projecten/anet/open-data/)) we tend to forget this and take the metadata at face value.

Imagine, for a minute, that you hadn't seen the above title page, but merely got the STCV metadata from a SQL query. How accurate would your understanding of this title page actually be? And what happens when, as good DH research is bound to do, you break open metadata containers and aggregate metadata, for instance merging several of the national "short-title catalogue" initiatives (STCV, STCN, ESTC, USTC, ...), which all adhere to different rules?

To make matters worse, our example was a very simple one really. There are many, many more complex metadata problems. Just to give you a taste:

- How would you catalogue one of those toddler squeeky books that feature not a single word of text?
- When in 1993 Princed changed his stage name to the unpronounceable symbol ![Prince](images/prince.png) (known to fans as the "Love Symbol"), and was sometimes referred to as the Artist Formerly Known as Prince or simply the Artist, how were record shops supposed to catalogue his albums? Remember, in those days, most people would go up to the "P" section and browse for "Prince"!
- Or what about the IMDB website listing the actors of the Blair Witch Project as "missing, presumed dead" in the first year of the film's availability (see [this](https://web.archive.org/web/20170109185339/http://www.telegraph.co.uk/films/2016/07/25/why-did-the-world-think-the-blair-witch-project-really-happened/) article)?


## Metadata 101

We now have a better understanding of metadat. As a former student of mine [@Karolingva]() once tweeted from a [RightsCon](https://www.rightscon.org/) conference: metadata is not data about data, but

- created data about data
- by humans
- with a purpose
- according to certain standards

This means than when working with metadata we need to be acutely aware of this context.

In short, that means having an understanding of cataloguing standards, metadata standards and exports.

### Cataloguing standards

As we saw in the case of STCV or WorldCat books were catalogued following certain rules. The same holds true for all sorts of physical or digital items. So if you are working with metadata you'll do well to have at least a basic understanding of the cataloguing standards that were used to create this metadata.

As for [book cataloguing standards](https://en.wikipedia.org/wiki/Cataloging#Cataloging_standards), for instance, we can mention

1. RDA (Resource Description and Access)

- http://access.rdatoolkit.org/ (subscription needed)
- E.g. Names with articles = ‘The Hague’ NOT ‘Hague, the’

2. DCRM(B) (Descriptive Cataloging of Rare Materials - Books)

- http://rbms.info/dcrm/dcrmb/ (open source)
- E.g. no spaces for abbreviations = ‘Ad S.R.E. Cardinalem...’, EXCEPT multiple letter-abbreviations = ‘Ad Ph. D. Jacobum..’


### Metadata standards

Once metadata has been produced according to certain cataloguing rules, we can also define a [metadata standard](https://en.wikipedia.org/wiki/Metadata_standard), i.e. 

> a requirement which is intended to establish a common understanding of the meaning or semantics of the data, to ensure correct and proper use and interpretation of the data by its owners and users.

Some of the most common metadata standards in the world of [GLAM](https://en.wikipedia.org/wiki/GLAM_(industry_sector)) (galleries, libraries, archives, and museums) are:

1. Books: MARC

- Machine-Readable Cataloging (MARC21)
- https://www.loc.gov/marc/ 
- e.g. field 245 = title

2. Archives: EAD

- Encoded Archival Description (XML standard)
- http://www.loc.gov/ead/ 

3. Objects: Dublin Core

- Dublin Core Metadata Initiative
- http://www.dublincore.org/ 

### Exports

Working with metadata one is quickly faced with the issue of data or [information silos](https://en.wikipedia.org/wiki/Information_silo):

>  an insular management system in which one information system or subsystem is incapable of reciprocal operation with others that are, or should be, related. Thus information is not adequately shared but rather remains sequestered within each system or subsystem, figuratively trapped within a container like grain is trapped within a silo: there may be much of it, and it may be stacked quite high and freely available within those limits, but it has no effect outside those limits. Such data silos are proving to be an obstacle for businesses wishing to use data mining to make productive use of their data.

Luckily many information systems, for instance for GLAM institutions, are paying increasing attention to providing open access metadata exports, which in turn allows to aggregate it (for further information retrieval, research purposes, etcetera). 

Such exports will make metadata available in all sorts of standards (see above) and formats, such as data dumps in .txt or .tab, structured formats like .csv, document databases like .xml or .json, or linked data. As we have seen in chapter 04 with Europeana, some institutions even provide an API.

#### Examples for book history

Some time ago I collected some examples of useful metadata exports in the field of book history. They might be worthwhile if you are looking for a research project.

1. Biographic databases

- [VIAF](https://platform.worldcat.org/api-explorer/apis/VIAF) (Virtual International Authority File) (SRU protocol)

- [DBpedia](https://wiki.dbpedia.org/OnlineAccess) (SPARQL endpoint, REST API, Lookup API)

- [CERL thesaurus](https://data.cerl.org/thesaurus/_sru) (place name and personal names in Europe in the period of hand press printing, c. 1450 - c. 1830)  (linked data in XML/RDF, SRU protocol)

- [Europeana Entities](https://pro.europeana.eu/page/entity) (named entities) (API)

- [RKDArtists](https://rkd.nl/en/collections/services-tools/rkdartists-as-linked-open-data/open-search-artists) (biographical data about artists, companies and institutes of various disciplines of visual arts, applied arts and architecture from both the Netherlands as abroad) (API with Lucene query syntax)


2. Bibliographic databases

- [Worldcat](https://platform.worldcat.org/api-explorer/apis) (wide range of exports, plugins, APIs)

- [Anet open data](https://www.uantwerpen.be/nl/projecten/anet/open-data/) (including STCV, downloads in MARXML or SQLite)

- [HPB](https://www.cerl.org/resources/hpb/technical/modes_of_access_to_the_hpb_database) (paywall) (SRU)

- [TW](http://tw.staatsbibliothek-berlin.de/) (Typenrepertorium der Wiegendrucke) (XML exports)

- [VD16/VD17](http://www.gateway-bayern.de/index_vd16.html) (download up to 999 records as CSV and HTML)

## Excursus: DH example

As an example of the kind of DH research you could do using library metadata, I refer to a proof-of-concept paper of mine on [arXive](https://arxiv.org/abs/1706.09406v2): 

[A Datamining Approach to the Short Title Catalogue Flanders: the Case of Early Modern Quiring Practices](https://arxiv.org/abs/1706.09406v2), submitted on 28 Jun 2017 (v1), last revised 19 Nov 2018 (v2).

This paper contains a data mining approach to the Short Title Catalogue Flanders, which aims to record all books printed in Flanders up to 1801 (24.850 editions, per 31/08/2018). More specifically, it aims to analyse the Early Modern practice of 'quiring' gatherings in handpress book production

### Disclaimer

This research was done well before my days as a professional software engineer. So while you may find the research and its results interesting, I'm sure the code itself leaves a lot to be desired!

## Assignment: MARC21 to Dublin Core for OAI

[The Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH)](https://www.openarchives.org/pmh/) or OAI for short:

> is a low-barrier mechanism for repository interoperability. Data Providers are repositories that expose structured metadata via OAI-PMH. Service Providers then make OAI-PMH service requests to harvest that metadata. OAI-PMH is a set of six verbs or services that are invoked within HTTP.

At Anet, for instance, we provide full OAI access to our complete database of books. Like so:

https://anet.be/oai/catgeneric/server.phtml?verb=GetRecord&metadataPrefix=marc21&identifier=c:lvd:123456 (MARC21)

https://anet.be/oai/catgeneric/server.phtml?verb=GetRecord&metadataPrefix=mods&identifier=c:lvd:123456 ([MODS](https://en.wikipedia.org/wiki/Metadata_Object_Description_Schema))

In these examples, the trailing "c:lvd:" number is a unique Library Object Identifier (LOI) used by [Brocade](https://en.wikipedia.org/wiki/Brocade_Library_Services)

Typically, libraries will use the OAI protocol to import/export metadata in different formats. So when setting up an OAI server, one of the main tasks is coding software that converts data from one standard to another. Libraries management systems, for instance, need such conversions both to be able to feed an OAI server from their own database respository, or, vice versa, to harvest data from external repositories and convert it to the standard(s) they use.

According to the standards specifications, all implementations of OAI-PMH must support representing metadata in Dublin Core, so your assignment will be to write a metadata converter that is able to harvest MARC21 metadata (XML) and convert that to Dublin Core (XML). It should be a Python command line application that asks for a LOI number (e.g. `c:lvd:123456`), uses OAI to harvest the MARC21 metadata and then writes the Dublin Core conversion to a file (e.g. `123456.xml`).

### Tips

- You can use the Library of Congress [MARC to Dublin Core Crosswalk](https://www.loc.gov/marc/marc2dc.html). You can limit yourself to the fields mentioned in the "unqualified" table and skip the "Leader" field. You will find the meaning of the various codes (`a`, `c`, etcetera) in the MARC specification, but you can limit yourself to code `a`, unless the crosswalk explicitly mentions other codes (e.g. `260` = `Publisher`)
- The Python `lxml` library is well-suited to both parse (MARC21) and generate (Dublin Core) XML.
- Read about XML namespaces: https://www.w3schools.com/xml/xml_namespaces.asp and https://lxml.de/tutorial.html#namespaces


