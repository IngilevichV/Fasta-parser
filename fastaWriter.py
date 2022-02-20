from sequence import  Sequence, COMMENT_CHAR


class FastaFileWriter:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def write(self, id: str, info: str, dna: str):
        sequence_item = Sequence(dna)
        with open(self.file_name, 'w') as f:
            f.write(f'{COMMENT_CHAR}{id} {info}\n')
            for chunk in sequence_item.split_into_chunks():
                f.write(f'{chunk}\n')
