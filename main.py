import argparse
from function import convert_pdf
print("import done")


#Argument Paser construction
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--pdf", type=str, required=True,help="path to input pdf")
args = vars(ap.parse_args())


convert_pdf(args["pdf"])

print("Extraction has been completed")
