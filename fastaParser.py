from sequence import Description, Sequence, COMMENT_CHAR


class FastaItem:
    def __init__(self, description: str):
        self.description = Description(description)
        self.sequences = []

    def add_sequence(self, seq: str):
        self.sequences.append(seq)

    def get_sequence(self) -> str:
        return "".join(self.sequences)


class FastaParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_file(self):
        fasta_record = None
        with open(self.file_path, "r") as f:
            for line in f:
                if line.startswith(COMMENT_CHAR):
                    # print("description of file", line)
                    fasta_record = FastaItem(line)
                else:
                    # print("dna", line)
                    fasta_record.add_sequence(line)
        return Sequence(fasta_record.get_sequence())


