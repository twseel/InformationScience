# Chapter 2: Definition


![](images/text_data_mining.jpg)

Credit: Davide Bonazzi

## Definition

### Information Science, Retrieval or Theory?

While this course is officially called Information *Science*, it was originally presented to me as Information *Retrieval*, which is rather different. And then you might also have heard about Information *Theory*. So let's have a look at these disciplines and how they relate to each other.

#### Information Theory

[Wikipedia](https://en.wikipedia.org/wiki/Information_theory) says:

>Information theory studies the quantification, storage, and communication of information. It was originally proposed by Claude Shannon in 1948 to find fundamental limits on signal processing and communication operations such as data compression, in a landmark paper titled "A Mathematical Theory of Communication". Its impact has been crucial to the success of the Voyager missions to deep space, the invention of the compact disc, the feasibility of mobile phones, the development of the Internet, the study of linguistics and of human perception, the understanding of black holes, and numerous other fields.

>The field is at the intersection of mathematics, statistics, computer science, physics, neurobiology, information engineering, and electrical engineering. The theory has also found applications in other areas, including statistical inference, natural language processing, cryptography, neurobiology, human vision, the evolution and function of molecular codes (bioinformatics), model selection in statistics, thermal physics, quantum computing, linguistics, plagiarism detection, pattern recognition, and anomaly detection. Important sub-fields of information theory include source coding, algorithmic complexity theory, algorithmic information theory, information-theoretic security, Grey system theory and measures of information.

>Applications of fundamental topics of information theory include lossless data compression (e.g. ZIP files), lossy data compression (e.g. MP3s and JPEGs), and channel coding (e.g. for DSL). Information theory is used in information retrieval, intelligence gathering, gambling, and even in musical composition.

>A key measure in information theory is entropy. Entropy quantifies the amount of uncertainty involved in the value of a random variable or the outcome of a random process. For example, identifying the outcome of a fair coin flip (with two equally likely outcomes) provides less information (lower entropy) than specifying the outcome from a roll of a die (with six equally likely outcomes). Some other important measures in information theory are mutual information, channel capacity, error exponents, and relative entropy.

#### Information Retrieval

Information Retrieval relies on information theory for its methods, but it is a much more applied discipline. [Wikipedia](https://en.wikipedia.org/wiki/Information_retrieval) says: 

>Information retrieval (IR) is the activity of obtaining information system resources that are relevant to an information need from a collection of those resources. Searches can be based on full-text or other content-based indexing. Information retrieval is the science of searching for information in a document, searching for documents themselves, and also searching for the metadata that describes data, and for databases of texts, images or sounds.

>Automated information retrieval systems are used to reduce what has been called information overload. An IR system is a software system that provides access to books, journals and other documents; stores and manages those documents. Web search engines are the most visible IR applications.

>An information retrieval process begins when a user enters a query into the system. Queries are formal statements of information needs, for example search strings in web search engines. In information retrieval a query does not uniquely identify a single object in the collection. Instead, several objects may match the query, perhaps with different degrees of relevancy.

>An object is an entity that is represented by information in a content collection or database. User queries are matched against the database information. However, as opposed to classical SQL queries of a database, in information retrieval the results returned may or may not match the query, so results are typically ranked. This ranking of results is a key difference of information retrieval searching compared to database searching.

>Depending on the application the data objects may be, for example, text documents, images, audio, mind maps or videos. Often the documents themselves are not kept or stored directly in the IR system, but are instead represented in the system by document surrogates or metadata.

>Most IR systems compute a numeric score on how well each object in the database matches the query, and rank the objects according to this value. The top ranking objects are then shown to the user. The process may then be iterated if the user wishes to refine the query.

#### Information Science

Finally, Information Science is introduced on [Wikipedia](https://en.wikipedia.org/wiki/Information_science) as:

>Information science (also known as information studies) is an academic field which is primarily concerned with analysis, collection, classification, manipulation, storage, retrieval, movement, dissemination, and protection of information. Practitioners within and outside the field study the application and the usage of knowledge in organizations along with the interaction between people, organizations, and any existing information systems with the aim of creating, replacing, improving, or understanding information systems. Historically, information science is associated with computer science, psychology, technology and intelligence agencies. However, information science also incorporates aspects of diverse fields such as archival science, cognitive science, commerce, law, linguistics, museology, management, mathematics, philosophy, public policy, and social sciences.


## History

In a way, all of these approaches are a way of dealing with **information overload**, which has a very long history. In a sense we might trace it back to Antiquity with Seneca the Elder (1st c. AD) who commented that "the abundance of books is distraction" or with Ecclesiastes 12:12: "of making books there is no end". Indeed, compendia, anthologies, abbreviations and such became very popular in the Middle Ages as a way to manage information. However, with the arrival of the printing press information overload became truly problematic. We see people like Erasmus complaining about the swarms of new books and looking for ways to further organize, compile, index, ... information in thesauri, encyclopaedias, etcetera. Of course, the arrival of digital carriers and finally the Internet are the apex of this evolution.

If your interested in reading more about this, have a look at the [Wikipedia](https://en.wikipedia.org/wiki/Information_overload) article on the topic, or for Early Modern times specifically:

- Ann Blair, [Information overload, the early years](http://archive.boston.com/bostonglobe/ideas/articles/2010/11/28/information_overload_the_early_years/?page=full)
- Ann Blair, Reading Strategies for Coping with Information Overload ca. 1550-
1700, in: Journal of the History of Ideas, 64 (2003), 11-28.


## Ethics

Something else which is beyond the scope of this course, is information ethics. Still, we cannot go by without at least briefly touching the topic.

Living in the [Information Age](https://en.wikipedia.org/wiki/Information_Age) is of course a wonderful thing. Most vital aspects of our life, health, work, communication, travel, ... all rely on information. It started with newspapers, radio and TV. Then came computers, the Internet and mobile phones. Today, all of these media are interconnected in our smartphones, tablets and laptops. They are fed by big data and increasingly able through the use of artificial intelligence and machine learning.

While the possibilities of the Information Age can be immensely empowering, it is also clear that **great power comes with great responsiblity**. The flipside of our dependency of information are phenomena like computer crime, digital dark age, cyberterrorism, digital divide, child pornography on the Dark Web, and many, many more. 

Often information technologies are very ambivalent, and it is not easy to see when they cross the line. Two examples.

1. A South-Korean TV documentary gave a mother the opportunity to meet a digital version of her dead daughter after her body, voice and face were recreated using virtual reality technology. You can read more about it in these sources and also watch the footage on YouTube (which I recommend). Do you find the story beautiful or heartbreaking?

- https://www.telegraph.co.uk/technology/2020/02/11/virtual-reality-used-reunite-grieving-mother-avatar-dead-child/
- https://futurism.com/watch-mother-reunion-deceased-child-vr
- https://youtu.be/uflTK8c4w0c

2. You probably know about [GPT-3](https://en.wikipedia.org/wiki/GPT-3), Generative Pre-trained Transformer 3, which is a language model — a program that is, given an input text, trained to predict the next word or words. GPT-3 is one of the largest such models, having been trained on about 45 terabytes of text data, taken from thousands of web sites such as Wikipedia, plus online books and many other sources (definition from [this](https://medium.com/@melaniemitchell.me/can-gpt-3-make-analogies-16436605c446) Medium article). The quality of the text generated by GPT-3 is so high that it is difficult to distinguish from that written by a human, which has both benefits and risks. One of the risks is that if there is a certain bias (eurocentric, sexist, racist, ...) present in the data the model is trained on, this trend will be reflected in the texts produced by the model. Some concrete examples can be found in: 

- https://techcrunch.com/2020/08/07/here-are-a-few-ways-gpt-3-can-go-wrong/
- https://medium.com/fair-bytes/how-biased-is-gpt-3-5b2b91f1177
- https://twitter.com/Abebab/status/1309137018404958215?s=09

The recent Netflix documentary [The Social Dilemma](https://www.netflix.com/be/title/81254224) undoubtedly touches this subject too.