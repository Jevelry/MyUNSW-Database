# MyUNSW-Database
<h3>Introduction</h3>

<p>
All Universities require a significant information infrastructure in order
to manage their affairs. This typically involves a large commercial DBMS
installation.
UNSW's student information system sits behind the MyUNSW web site.
MyUNSW provides an interface to a PeopleSoft enterprise management
system with an underlying Oracle database. This back-end system
(Peoplesoft/Oracle) is sometimes called NSS. The specific version of
PeopleSoft that we use is called Campus Solutions. There is also a
system called SiMS, which can be used to access the data.
</p>
<p>
UNSW has spent a considerable amount of money ($100M+) on the MyUNSW/NSS
system, and it handles much of the educational administration plausibly
well. Most people gripe about the quality of the MyUNSW interface, but
the system does allow you to carry out most basic enrolment tasks online.
</p>
<p>
Despite its successes, however, MyUNSW/NSS still has a number of
deficiencies, including:
<ul>
<li> no usable representation for degree program structures
<li> minimal integration with the UNSW Online Handbook
</ul>
<p>
The first point prevents MyUNSW/NSS from being used for three
important operations that would be extremely helpful to students
in managing their enrolment:
</p>
<ul>
<li> finding out how far they have progressed through their degree
	program, and what remains to be completed
<li> checking what are their enrolment options for next semester
	(e.g.,  get a list of <q>suggested</q> courses)
<li> determining when they have completed all of the requirements
	of their degree program and are eligible to graduate
</ul>
<p>
The second point allows for inconsistencies between the Handbook
and the system that manages enrolment.
</p>
<p>
NSS contains data about students, courses, classes, pre-requisites,
quotas, etc. but does not contain any representation of UNSW's
degree program structures.
Without such information in the NSS database, it is not possible
to do any of the above three.
So, in 2007 the COMP3311 class devised a data model that
could represent program requirements and rules for UNSW degrees.
This was built on top of an existing schema that represented all
of the core NSS data (students, staff, courses, classes, etc.).
The enhanced data model was named the <q>MyMyUNSW</q> schema.
</p>
<p>
The MyMyUNSW database includes information that encompasses the
functionality of NSS, the UNSW Online Handbook, and the CATS
(room allocation) database.
The MyMyUNSW data model, schema and database are
described in a <a href="schema.php">separate document</a>.
Note that, while the <em>schema</em> is the complete one we developed
in 2007, the <em>data</em> for this database has been trimmed to the
absolute minimum to do this assignment; many tables and
columns are empty.
</p>
<h3>Q1 <span class='marks'>(6 marks)</span></h3>

<p>
Write a Python script called <tt>trans</tt>, that takes
a command-line argument giving a student ID, and prints
a transcript for that student.
The template script already checks the command line argument.
<p>
<h3>Q2 <span class='marks'>(6 marks)</span></h3>

<p>
Write a Python script that takes a program code or a stream code
and produces a readable list of rules for that program or stream.
</p>
<h3>Q3 <span class='marks'>(8 marks)</span></h3>

<p>
Write a Python script to show a student's progression through their
program/stream, and what they still need to do to complete their
degree.
The script takes three command line parameters:
</p>
