import unittest
import csv
import Data
import random
import string
import StringIO

class TestData(unittest.TestCase):
   numTests = 100
   def test_DataSet(self):
      numItems = random.randint(1,TestData.numTests)
      ds = []
      for i in range(numItems):
         size = random.randint(0, 1000)
         s = ''.join(random.choice(string.printable) for x in range(size))
         t = random.randint(0,1) == 1
         ds.append(Data.Data(s,t))
      dataset = Data.DataSet(ds)
      for dd in zip(ds, dataset):
         assert(dd[0] == dd[1])
   def test_FilesDataSet(self):
      """Test files by making fake files that are comply with 
      the file interface that we use."""
      numFiles = random.randint(1, 10)
      files = []
      ds = []
      for i in range(numFiles):
         f = StringIO.StringIO()
         writer = csv.writer(f)
         files.append(f)
         numItems = random.randint(0,TestData.numTests)
         for i in range(numItems):
            size = random.randint(0, 1000)
            s = ''.join(random.choice(string.printable) for x in range(size))
            t = random.randint(0,1) == 1 
            ds.append((s,t))
            writer.writerow((s,t))
      fileDS = Data.FilesDataSet(files)
      for w in zip(fileDS, ds):
         assert(w[0].string == w[1][0])
         assert(w[1].isTrue == w[1][1])


if __name__=="__main__":
   unittest.main()
