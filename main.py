from fastaParser import FastaParser
from fastaWriter import FastaFileWriter

TEST_DNA = "ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT"

if __name__ == '__main__':
    parser = FastaParser("./FASTA-1.fasta")
    parser.parse_file()

    writer = FastaFileWriter("test.fasta")
    writer.write("test_id", "test_description", TEST_DNA)
