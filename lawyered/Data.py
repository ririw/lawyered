import csv

class Data(object):
   """A data point. The string can be accessed through Data.string and the
   truthfulness through Data.isTrue"""
   def __init__(self, string, tag):
      self.string = string
      self.tag = tag
   def __str__(self):
      return str(self.tag) + " | " + str(self.string)

class DataSet(list):
   """DataSets extend list, so access them in the obvious way"""
   def __init__(self, items = []):
      for item in items:
         assert(isinstance(item, Data))
      super(DataSet, self).__init__(items)

class FilesDataSet(DataSet):
   """A FileDataSet is a data set that is built from a list of CSV
   files. These must be file objects"""
   def __init__(self, files):
      items = []
      for f in files:
         reader = csv.reader(f)
         for line in reader:
            items.append(Data(line[0].strip(), line[1].strip() == "True"))
      super(FilesDataSet, self).__init__(items)

