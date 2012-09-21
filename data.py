import csv

class Data(object):
   def __init__(self, string, isTrue):
      self.string = string
      self.isTrue = isTrue
   def __str__(self):
      if self.isTrue:
         return "Truth: \"%s\"" % self.string
      else:
         return "Lie: \"%s\"" % self.string

class DataSet(list):
   def __init__(self, items = []):
      for item in items:
         assert(isinstance(item, Data))
      super(DataSet, self).__init__(items)

class FilesDataSet(DataSet):
   def __init__(self, files):
      items = []
      for (f in files):
         reader = csv.reader(f)
         for line in reader:
            items.append(Data(line[0].strip(), line[1].strip() == "True")
      super(FilesDataSet, self).__init__(items)

