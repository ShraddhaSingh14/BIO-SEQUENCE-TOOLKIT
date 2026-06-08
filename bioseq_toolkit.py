# ==========================================
# BioSeq Toolkit
# Python-Based DNA & Protein Analysis Tool
# Author: Shraddha Singh
# ==========================================

from Bio import SeqIO
from Bio.Seq import Seq


# -------------------------------
# Read FASTA File
# -------------------------------
def read_fasta(file_path):
    record = SeqIO.read(file_path, "fasta")
    return record.id, str(record.seq)


# -------------------------------
# Sequence Statistics
# -------------------------------
def sequence_analysis(seq):
    seq = seq.upper()

    length = len(seq)
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")

    gc_content = ((g + c) / length) * 100

    print("\n===== DNA ANALYSIS =====")
    print("Length :", length)
    print("A :", a)
    print("T :", t)
    print("G :", g)
    print("C :", c)
    print(f"GC Content : {gc_content:.2f}%")

    return gc_content


# -------------------------------
# Reverse Complement
# -------------------------------
def reverse_complement(seq):
    rc = str(Seq(seq).reverse_complement())
    print("\nReverse Complement:")
    print(rc)
    return rc


# -------------------------------
# DNA → RNA
# -------------------------------
def transcription(seq):
    rna = str(Seq(seq).transcribe())
    print("\nRNA Sequence:")
    print(rna)
    return rna


# -------------------------------
# DNA → Protein
# -------------------------------
def translation(seq):
    protein = str(Seq(seq).translate())
    print("\nProtein Sequence:")
    print(protein)
    return protein


# -------------------------------
# Codon Extraction
# -------------------------------
def codons(seq):
    codon_list = [seq[i:i+3] for i in range(0, len(seq), 3)]

    print("\nCodons:")
    print(codon_list)

    return codon_list


# -------------------------------
# Motif Search
# -------------------------------
def find_motif(seq, motif):
    positions = []

    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i)

    print("\nMotif Search")
    print("Motif:", motif)
    print("Positions:", positions)

    return positions


# -------------------------------
# Mutation Detection
# -------------------------------
def mutation_detection(seq1, seq2):

    mutations = []

    for i, (a, b) in enumerate(zip(seq1, seq2)):
        if a != b:
            mutations.append((i + 1, a, b))

    print("\nMutation Report")
    print("Total Mutations:", len(mutations))

    for m in mutations:
        print(
            f"Position {m[0]} : {m[1]} -> {m[2]}"
        )

    return mutations


# -------------------------------
# Save Report
# -------------------------------
def save_report(filename, text):
    with open(filename, "w") as file:
        file.write(text)

    print("\nReport saved as", filename)


# =====================================
# MAIN PROGRAM
# =====================================

try:

    fasta_file = "sample.fasta"

    seq_id, dna = read_fasta(fasta_file)

    print("Sequence ID:", seq_id)
    print("DNA Sequence:", dna)

    gc = sequence_analysis(dna)

    rna = transcription(dna)

    protein = translation(dna)

    rc = reverse_complement(dna)

    codon_data = codons(dna)

    motif_positions = find_motif(dna, "ATG")

    mutation_detection(
        "ATGCGT",
        "ATGAGT"
    )

    report = f"""
BIOSEQ TOOLKIT REPORT

Sequence ID : {seq_id}

DNA Sequence:
{dna}

Length : {len(dna)}

GC Content : {gc:.2f}%

RNA Sequence:
{rna}

Protein Sequence:
{protein}

Reverse Complement:
{rc}

Motif Positions:
{motif_positions}
"""

    save_report(
        "BioSeq_Report.txt",
        report
    )

except FileNotFoundError:
    print("FASTA file not found!")

except Exception as e:
    print("Error:", e)
  
