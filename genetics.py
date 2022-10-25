"""
Purpose: manipulates strings of 'A', 'C', 'U', 'T', and 'G' letters
representing DNA and RNA base pairs.
"""

def templateBase(base):
    """
    Given an RNA base ('A', 'U', 'G', or 'C') this function returns the
    DNA base that serves as a template for that base ('T' for 'A', 'A'
    for 'U', 'C' for 'G', and 'G' for 'C').
    """
    if base == 'A':
        return 'T'
    elif base == 'U':
        return 'A'
    elif base == 'G':
        return 'C'
    elif base == 'C':
        return 'G'
    else:
        raise ValueError("{} is not a valid RNA base!".format(repr(base)))


def countOtherBases(seq, exbase):
    '''counts the number of bases excluding a specific base'''
    count=0
    for base in seq:
        if base!=exbase:
            count+=1
    return count

def templateSequence(rna):
    '''returns  sequence with corresponding bases in RNA'''
    newseq=""
    for base in rna:
        newseq+=templateBase(base)
    return newseq

def onlyAU(seq):
    '''returns only A or U bases'''
    newseq=""
    for base in seq:
        if base=="A":
            newseq+=base
        elif base=="U":
            newseq+=base
    return newseq

def transcriptionErrors(rna, dna):
    '''counts number of errors in transcription'''
    count=0
    trna = templateSequence(rna)
    a= min(len(trna), len(dna))
    for i in range(a):
            if trna[i]!=dna[i]:
                count+=1
    count+=abs(len(dna)-len(rna))
    return count

def hasCGBlock(rna):
    '''determines if sequence of CG is longer than 5'''
    cgseq=""
    for base in rna:
        if base=="C" or base=="G":
            cgseq+=base
        else:
            cgseq=""
        if len(cgseq)>=5:
            return True
    return len(cgseq)>5

