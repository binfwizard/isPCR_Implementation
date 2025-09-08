#! /usr/bin/env python3

import subprocess
import csv

def run_blastn(primer_file, assembly_file):
    cmd = [
        "blastn",
        "-query", primer_file,
        "-subject", assembly_file,
        "-task", "blastn-short",
        "-outfmt", "6 std qlen"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def filter_blast_hits(blast_output, min_identity=80):
    filtered_hits = []
    for line in blast_output.strip().split('\n'):
        fields = line.split('\t')
        qlen = int(fields[-1])
        length = int(fields[3])
        pident = float(fields[2])

        if length == qlen and pident >= min_identity:
            filtered_hits.append(fields)

    return filtered_hits

def step_one(primer_file: str, assembly_file: str) -> list[list[str]]:
    blast_output = run_blastn(primer_file, assembly_file)
    filtered_hits = filter_blast_hits(blast_output)

    # Convert all fields to strings
    return [[str(field) for field in hit] for hit in filtered_hits]

