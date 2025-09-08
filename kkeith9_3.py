import subprocess
import tempfile
import os


def create_bed_file(hit_pairs, trim_start=18, trim_end=20):
    bed_content = ""
    for pair in hit_pairs:
        chrom = pair[0][1]
        start = min(int(pair[0][8]), int(pair[0][9]), int(pair[1][8]), int(pair[1][9])) + trim_start
        end = max(int(pair[0][8]), int(pair[0][9]), int(pair[1][8]), int(pair[1][9])) - trim_end
        bed_content += f"{chrom}\t{start}\t{end}\n"
    return bed_content


def step_three(hit_pairs: list[tuple[list[str]]], assembly_file: str) -> str:
    bed_content = create_bed_file(hit_pairs)

    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_bed:
        temp_bed.write(bed_content)
        temp_bed_path = temp_bed.name

    cmd = ["seqtk", "subseq", assembly_file, temp_bed_path]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    os.unlink(temp_bed_path)
    return result.stdout



