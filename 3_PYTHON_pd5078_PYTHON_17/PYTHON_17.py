from Bio import Entrez
from Bio import SeqIO
from Bio.Align import PairwiseAligner

# Ustawienie adresu email
Entrez.email = "pd5078@pjwstk.edu.pl"
genbank_ids = ["JX669568", "JX669571"]
output_fasta = "sekwencje.fasta"

# Pobierz dwie sekwencje nukleotydowe z bazy danych GenBank za pomocą identyfikatorów JX669568
# oraz JX669571

handle = Entrez.efetch(db="nucleotide", id=genbank_ids, rettype="gb", retmode="text")
records = list(SeqIO.parse(handle, "genbank"))
handle.close()
record1, record2 = records

# Zapisz obie sekwencje do pliku w formacie FASTA.
SeqIO.write(records, output_fasta, "fasta")


#  Wczytaj zapisany plik FASTA i porównaj obie sekwencje ze sobą, używając algorytmu
# Needleman-Wunsch do dopasowania globalneg

sequences = [record1.seq, record2.seq]

aligner = PairwiseAligner()
aligner.mode = 'global'
alignments = aligner.align(sequences[0], sequences[1])
best_alignment = alignments[0]

# Wyświetl wynik najlepszego dopasowania oraz jego punktację.

print("\nNajlepsze dopasowanie:")
print(best_alignment)      
print("Wynik dopasowania:", best_alignment.score)