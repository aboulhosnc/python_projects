


def dna_to_rna(dna):
    # str1 = "ATGC"
    # str2 = "UACG"
    # str3 = ""
    table = dna.maketrans("ATGC","UACG")
    mrna = dna.translate(table)
    print(mrna)

    return dna.translate(table)
	

def main():
    print("hello world")
    print("dna_to_mNRA")
    dna_to_rna("GCGTAC")



# Test.assert_equals(dna_to_rna("GCGTAC"), "CGCAUG")
# Test.assert_equals(dna_to_rna("ATTAGCGCGATATACGCGTAC"), "UAAUCGCGCUAUAUGCGCAUG")
# Test.assert_equals(dna_to_rna("CAGTATGCTGCAT"), "GUCAUACGACGUA")
# Test.assert_equals(dna_to_rna("CGATATA"), "GCUAUAU")
# Test.assert_equals(dna_to_rna("GCAGCTACA"), "CGUCGAUGU")



if __name__ == "__main__":
    main()