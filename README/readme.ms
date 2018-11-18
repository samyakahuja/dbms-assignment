.TL
Database Programs Using Python
.AU
Samyak Ahuja
.AI
University of Delhi

.NH
Introduction
.PP
List of Programs are as follows :
.RS
.IP \[bu]
.B Closure 
of an attribute given a set of Functional Dependencies
.IP \[bu]
.B Candidate\ key s
given a Relation and a set of Functional Dependencies
.IP \[bu]
.B Equivalence
between 2 sets of Functional Dependencies given a Relation
.IP \[bu]
.B Minimal\ Cover
given a set of Functional Dependencies
.IP \[bu]
Find the highest
.B Normal\ Form
given a Relation and a set of Functional Dependencies
.RE

.QP
.B Note
.R T
Definition of Minimal Cover is often contrieved and confused with Canonical Cover
Let's clear that up once and for all. 
A canonical cover is "allowed" to have more than one attribute on the right hand side.
A minimal cover cannot. As an example, the canonical cover may be "A -> BC" where the
minimal cover would be "A -> B, A -> C". That is the only difference.


.NH
Program Structure
.PP
Programs are divided into 3 files each having a purpose of its own.

.RS
.SH
Helper File
.LP
.I helpers.py 
is a file that contians helper functions namely,
.IP Every 
- Returns True if every member of the list when called with function callback return True.
.IP Some 
- Returns True if any member of the list when called with function callback returns True.
.RE

.RS
.SH
Driver File
.LP
.I driver.py
is used for interacting with the user. It reads the relation and the set of 
functional dependencies from the user and the displays the menu and the result to the user.
.RE

.RS
.SH
DBMS File
.LP
.I dbms.py
file defines 2 different Classes and all the functions listed above.
.LP
The 2 classes are:

.RS
.IP FunctionalDependencySet
.RS
.LP
This Class is used to define all the functional dependencies(fd) in a set of fds called
.I __items__
where each fd is a tuple of the form 
.I
(lhs_of_fd, rhs_of_fd).
.LP
The Class defines functions to add, remove, replace functional dependencies. It
also includes a function to calculate the closure of any attribute for given set of
functional dependencies.
.RE

.IP Relation
.RS
.LP
Any object of this class consists of 2 attributes. First is the attributes/features
in the database. Second is an instance of FunctionalDependecySet describing the fds
of this relation.
.LP
The methods included are:
.RS
.IP closureSet
Calculates the closure of an attribute given the fds.
.IP validKey
Returns True if given attribute is a super key of the given relation.
.IP candidateKeys
Returns the set of all the candidate keys for the given relation.
.RE
.RE

.RE

.LP
The functions provided are:

.RS
.IP "cover(fd1, fd2)"
Returns True if fd1 is covered by fd2.
.IP "equivalence(fd1, fd2)"
Returns True if fd1 and fd2 are equivalent functional dependencies.
.IP "isPartialDependency(fdItem, candidates, nonPrimes)"
Returns True if fdItem is a partial functional dependency.
.IP "hasPartialDependency(relation)"
Returns True if given relation has a partial dependency
.IP "isFirstNF(relation)"
Always returns True, It has been assumed that a relation is always in 1NF.
.IP "isSecondNF(relation)"
Returns True if given relation is in 2NF. It does so by checking 2 things.
.RS
.IP \[bu]
Given relation in in 1NF (always true)
.IP \[bu]
Given relation does not have any partial dependency
.RE
.IP "isThirdNF(relation)"
Return True if given relation is in 3NF. It does so by checking 2 things.
.RS
.IP \[bu]
Given relation is in 2NF.
.IP \[bu]
For every functional dependency, Any of following is True.
.RS
.IP \[bu]
RHS is subset of LHS, i.e. it is a trivial functional dependency.
.IP \[bu]
LHS is a valid super-key
.IP \[bu]
RHS is a subset of the prime attributes.
.RE
.RE
.IP "isBCNF(relation)"
Return True if given relation is in BCNF. It does so by checking 2 things.
.RS
.IP \[bu]
Given relation is in 3NF.
.IP \[bu]
For every functional dependency LHS is a valid super-key.
.RE
.IP "minimalCover(attributes, fdString)"
Return an instance of FunctionalDependencySet that is the minimal Cover given
the functional dependencies. It forms the minimal cover by doing 3 steps:
.RS
.IP \[bu]
Reduce the RHS by using decomposition rule so that RHS only contains 1 attribute.
.IP \[bu]
Remove any Functional Dependency if cover of LHS when removed and when 
isn't are equal.
.IP \[bu]
Check for Redundancy in the LHS of the functional dependency.
.RE
.RE
.RE

.NH
Ouput examples
.PSPIC image.eps
