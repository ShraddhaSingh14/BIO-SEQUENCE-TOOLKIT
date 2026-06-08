
# BIO-SEQUENCE-TOOLKIT

## Overview
BIO-SEQUENCE-TOOLKIT is a Python-based bioinformatics toolkit developed for DNA and protein sequence analysis using Biopython.

## Features
- FASTA File Reading
- DNA Sequence Analysis
- Nucleotide Counting
- GC Content Calculation
- DNA to RNA Transcription
- DNA to Protein Translation
- Reverse Complement Generation
- Codon Extraction
- Motif Detection
- Mutation Detection
- Report Generation
- Exception Handling

## Requirements
- Python 3.x
- Biopython

## Installation

```bash
pip install biopython

## Usage

Run the toolkit using:

```bash
python bioseq_toolkit.py
```

Or analyze a FASTA file:

```bash
python bioseq_toolkit.py sample.fasta
```

## Sample Input

Example FASTA file:

```fasta
>DNA_Sequence
ATGCGTACGTAGCTAGCTAGCTAGC
```

## Sample Output

Sequence Length: 25
GC Content: 52.0%
Transcribed RNA: AUGCGUACGUAGCUAGCUAGCUAGC
Protein Sequence: MRT...

- ## Protein Analysis Features

- Protein Translation
- Amino Acid Sequence Generation

