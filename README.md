# In-Silico PCR (isPCR) Pipeline
A lightweight Python workflow for simulating PCR amplification on a reference genome/assembly.
This pipeline (created as a part of **BIOL 7200** at Georgia Tech) identifies primer binding sites, validates primer pairs, and extracts predicted amplicon sequences directly from an assembly.

---
## ⚡ Features
- 🔍 Primer search using `blastn -task` `blastn-short`

- 🧷 Pairing algorithm to find valid forward/reverse primer pairs

- 📜 Amplicon extraction with `seqtk subseq`

- ✂️ Configurable trimming to remove primer sequences from output

- 💻 Simple and portable

---
## 🛠️ Requirements
- Python 3.9+
- NCBI BLAST+ (for `blastn`)
- seqtk (for subsequence extraction)

Install on macOS/Linux:
```
conda install -c bioconda blast seqtk
```
---
## 🚀 Usage
First, clone the repo: 
```
git clone https://github.com/<your-username>/isPCR_implementation.git
cd isPCR
```
Next, run all three steps:
```
from pipeline import step_one, step_two, step_three

# Input files
primers = "primers.fa"
assembly = "assembly.fa"

# Step 1: BLAST hits
hits = step_one(primers, assembly)

# Step 2: Primer pairs
pairs = step_two(hits, max_amplicon_size=1500)

# Step 3: Extract amplicons
amplicons = step_three(pairs, assembly)

print(amplicons)
```
--- 
## 📖 Output
- Coordinates are BED-like; check whether you need 0-based vs 1-based offsets depending on intended use.



