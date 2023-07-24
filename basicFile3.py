def file_long(filename):
      longest=""
      for line in open(filename) :
        if len(line) > len(longest):
            
