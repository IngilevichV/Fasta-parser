from typing import List

COMMENT_CHAR = ">"
DNA_LINE_LENGTH = 80
COMPLEMENTARY_BASE_IN = "ATUGCatugc"
COMPLEMENTARY_BASE_OUT = "TAACGtaagc"


class Sequence:
    def __init__(self, sequence: str):
        self.sequence = sequence

    def split_into_chunks(self) -> List[str]:
        return [self.sequence[i:i + DNA_LINE_LENGTH] for i in range(0, len(self.sequence), DNA_LINE_LENGTH)]

    def get_forward_strand_sequence(self) -> str:
        return self.sequence

    def get_reverse_strand_sequence(self) -> str:
        forward_strand = self.get_forward_strand_sequence()
        return forward_strand[::-1]

    def get_complement_forward_sequence(self) -> str:
        forward_strand = self.get_forward_strand_sequence()
        translator = str.maketrans(COMPLEMENTARY_BASE_IN, COMPLEMENTARY_BASE_OUT)
        return forward_strand.translate(translator)

    def get_complement_reverse_sequence(self) -> str:
        reverse_strand = self.get_reverse_strand_sequence()
        translator = str.maketrans(COMPLEMENTARY_BASE_IN, COMPLEMENTARY_BASE_OUT)
        return reverse_strand.translate(translator)


class Description:
    def __init__(self, description: str):
        self.description = description
        parsed_description = description[1:].split(" ")
        self.id = parsed_description[0]
        self.info = " ".join(parsed_description[1:])

    def id(self) -> str:
        return self.id

    def info(self) -> str:
        return self.info
