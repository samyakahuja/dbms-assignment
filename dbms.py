from itertools import combinations
from helpers import every
from helpers import some
class FunctionalDependencySet:
    __items__ = set()

    def __init__(self, iterable = []):
        self.__items__ = set( (lhs,rhs) for lhs, rhs in map(lambda x: x.split('->'), iterable) )

    def __len__(self):
        return len(self.__items__)

    def __iter__(self):
        return iter(self.__items__)
    
    def __next__(self):
        return 

    def add(self, lhs, rhs):
        self.__items__.add((lhs,rhs))

    def remove(self, lhs, rhs):
        self.__items__.remove((lhs, rhs))

    def leftSideSet(self):
        return set(lhs for lhs, rhs in self.__items__)
    
    def rightSideSet(self):
        return set(rhs for lhs, rhs in self.__items__)

    def closureSet(self, attributes):
        closure = set(attributes)

        for _ in range(0, len(self.__items__)):
            for lhs, rhs in self.__items__:
                if set(lhs).issubset(closure): 
                    closure.update(rhs)

        return closure

    def toString(self):
        return "FD = {\n\t" + "\n\t".join([ " -> ".join(item) for item in self.__items__]) + "\n}"

class Relation:
    def __init__(self, attributes, fdSet = FunctionalDependencySet() ):
        self.__attributes__ = set(attributes)
        self.fdSet = fdSet

    def attributes(self):
        return self.__attributes__

    def closureSet(self, attributes):
        return self.fdSet.closureSet(attributes)

    def validKey(self, attribute):
        return self.closureSet(attribute) == self.__attributes__

    def candidateKeys(self):
        #generating all possible combinations of attributes
        keys = []
        for i in range(1, len(self.fdSet)):
            possibilities = combinations(self.__attributes__, i)
            keys += [item for item in possibilities if self.validKey(item) and  every(keys, lambda key: not set(key).issubset(item))]

        return keys

    def toString(self):
        return "R(" + ", ".join(self.__attributes__) + "):\n" + self.fdSet.toString()

def cover(fd1, fd2):
    return every( lambda item: fd1.closureSet(item).issubset(fd2.closureSet(item)), fd1.leftSideSet() )

def equivalence(fd1,fd2):
    #fd2 covers fd1 and fd1 covers fd2
    return cover(fd1,fd2) and cover(fd2,fd1)

def isPartialDependency(fdItem, candidates, nonPrimes):
    lhs, rhs = fdItem

    if( not set(rhs).intersection(nonPrimes) ):
        return False

    return some( candidates, lambda key: not(set(key) == set(lhs)) and set(lhs).intersection(key) )

def hasPartialDependency(relation):
    candidates = relation.candidateKeys()
    primes = set( attr for key in candidates for attr in key)
    nonPrimes = relation.attributes().difference(primes)

    return some(relation.fdSet, lambda fdItem: isPartialDependency(fdItem, candidates, nonPrimes) )

def isFirstNF(relation):
    return True

def isSecondNF(relation): 
    return isFirstNF(relation) and not hasPartialDependency(relation)

def isThirdNF(relation):
    primes = set( attr for key in relation.candidateKeys() for attr in key)

    if(not isSecondNF(relation)):
        return False

    return not every(relation.fdSet, lambda fdItem: set(fdItem[0]).issubset(fdItem[1]) or relation.validKey(fdItem[1]) or set(fdItem[0]).issubset(primes) )

def isBCNF(relation):
    if(not isThirdNF(relation)):
        return False

    return every(relation.fdSet.leftSideSet(), lambda lhs: relation.validKey(lhs) )