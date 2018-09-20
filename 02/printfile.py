#Printing test files to .tst and output to .out 

fout = open('ALU-nostat.tst', 'w')
hdr = """load ALU.hdl,
output-file ALU.out,
compare-to ALU-nostat.cmp,
output-list in%B2.8.2out%B2.1.2;
"""

fout.write(hdr)
for i in range(256):
    fout.write('setin '+str(i)+',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')
fout.close()

fout = open('ALU.out', 'w')
fout.write('|    in    | out | \n')
for i in range(256):
    fout.write('|  '+format(i,'08b')+'  |  0  |\n')
fout.write('|  '+format(255,'08b')+'  |  1  |\n')
fout.close()

##########################################################

fout = open('ALU.tst', 'w')
hdr = """load ALU.hdl,
output-file ALU2.out,
compare-to ALU.cmp,
output-list in%B2.8.2out%B2.1.2;
"""

fout.write(hdr)
for i in range(512):
    fout.write('setin '+str(i)+',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')
fout.close()

fout = open('ALU.out2', 'w')
fout.write('|    in    | out | \n')
for i in range(512):
    fout.write('|  '+format(i,'08b')+'  |  0  |\n')
fout.write('|  '+format(255,'08b')+'  |  1  |\n')
fout.close()

