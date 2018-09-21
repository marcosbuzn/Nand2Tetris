#Printing test files to .tst and output to .out
#Team Members: Jared Orange, Ed Huang, Marcos Buznego


fout = open('ALU-nostat.tst', 'w')
hdr = """load ALU.hdl,
output-file ALU.out,
compare-to ALU-nostat.cmp,
output-list x%B1.16.1 y%B1.16.1 zx%B1.1.1 nx%B1.1.1 zy%B1.1.1 
            ny%B1.1.1 f%B1.1.1 no%B1.1.1 out%B1.16.1;
set x %B0000000000000000,
set y %B1111111111111111;
"""

fout.write(hdr)
for i in range(256):
    #fout.write('set '+str(i)+',\n') #setin
    #0
    fout.write('// Test'+str(i)+',\n')
    fout.write('set zx '+str(1)+',\n') #setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x&y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #x | y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    fout.write('set x %B000000000010001, \n')
    fout.write('set y %B000000000000011; \n')

    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # 1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x&y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x | y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

fout.close()

fout = open('ALU.out2', 'w')
fout.write('|    in    | out | \n')
for i in range(256):
    fout.write('|  '+format(i,'08b')+'  |  0  |\n')
fout.write('|  '+format(255,'08b')+'  |  1  |\n')
fout.close()

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

fout = open('ALU.tst', 'w')
hdr = """load ALU.hdl,
output-file ALU2.out,
compare-to ALU.cmp,
output-list x%B1.16.1 y%B1.16.1 zx%B1.1.1 nx%B1.1.1 zy%B1.1.1 
            ny%B1.1.1 f%B1.1.1 no%B1.1.1 out%B1.16.1 zr%B1.1.1
            ng%B1.1.1;
set x %B0000000000000000,  // x = 0
set y %B1111111111111111;  // y = -1
"""

fout.write(hdr)
for i in range(512):
    #fout.write('set '+str(i)+',\n') #setin
    #0
    fout.write('// Test'+str(i)+',\n')
    fout.write('set zx '+str(1)+',\n') #setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x&y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    #x | y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    fout.write('set x %B000000000010001, \n')
    fout.write('set y %B000000000000011; \n')

    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # 1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # !y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # -y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y+1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(1) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-1
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(1) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x+y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x-y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # y-x
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(1) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x&y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(0) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(0) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(0) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

    # x | y
    fout.write('// Test' + str(i) + ',\n')
    fout.write('set zx ' + str(0) + ',\n')  # setin
    fout.write('set nx ' + str(1) + ',\n')  # setin
    fout.write('set zy ' + str(0) + ',\n')
    fout.write('set ny ' + str(1) + ',\n')
    fout.write('set f ' + str(0) + ',\n')
    fout.write('set no ' + str(1) + ',\n')
    fout.write('eval,\n')
    fout.write('output;\n\n')

fout.close()

fout = open('ALU.out2', 'w')
fout.write('|    in    | out | \n')
for i in range(512):
    fout.write('|  '+format(i,'08b')+'  |  0  |\n')
fout.write('|  '+format(511,'08b')+'  |  1  |\n')
fout.close()

