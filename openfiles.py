"""Example to show Julie how to open files from a list."""

# Instead of:
# gbk_filename = "NC_005213.gbk"
# faa_filename = "NC_005213_converted.fna"
# input_handle  = open(gbk_filename, "r")
# output_handle = open(faa_filename, "w")

# We do:
fname = 'filenames.txt'
with open(fname) as f:
    filenames = f.readlines()
filenames = [x.strip() for x in filenames] # remove newlines

print(filenames)

# Now loop through every filename in filenames to do what you what to each:
for filename in filenames:
    filename = filename + '.gbk'
    print('I am working on:', filename)
    # blah blah...
