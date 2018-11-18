# %%
import dbms
from dbms import Relation, FunctionalDependencySet

attributes = input("Enter Relation Attributes: ")
print(attributes)

fdString = input("Functional Dependencies (LHS and RHS seperated by '->' and each FD seperated by ','): ")
fd = FunctionalDependencySet([ fd for fd in fdString.split(',')])
relation = Relation(attributes, fd)
print("\n")
print(relation.toString())

print("\nMinimal Cover :")
minimalCover =  dbms.minimalCover(attributes, fdString)
print(minimalCover.toString())

print("\n")
print('Candidate Keys:', relation.candidateKeys())


closureAtrributes = input("Attributes to find Closure: ")
print("Closure of", closureAtrributes, ":", relation.closureSet(closureAtrributes))

print("Relation is 1NF?", 'Yes' if dbms.isFirstNF(relation) else 'No')
print("Relation is 2NF?", 'Yes' if dbms.isSecondNF(relation) else 'No')
print("Relation is 3NF?", 'Yes' if dbms.isThirdNF(relation) else 'No')
print("Relation is BCNF?", 'Yes' if dbms.isBCNF(relation) else 'No')


print("\nEquivalence Test")
fdString1 = input("Functional Dependencies (LHS and RHS seperated by '->' and each FD seperated by ','): ")
fd1 = FunctionalDependencySet([ fd for fd in fdString1.split(',')])
fdString2 = input("Functional Dependencies (LHS and RHS seperated by '->' and each FD seperated by ','): ")
fd2 = FunctionalDependencySet([ fd for fd in fdString2.split(',')])
print("\nFd1 is covered by Fd2?", 'Yes' if dbms.cover(fd1,fd2) else 'No')
print("\nFd2 is covered by Fd1?", 'Yes' if dbms.cover(fd2,fd1) else 'No')
print("\nFd1 is equivalent to Fd2?", 'Yes' if dbms.equivalence(fd1,fd2) else 'No')
