import json
import os


  


class jsonfileclass():

  def __init__(self, filedir : str):
    if os.path.exists(filedir):
      self.filedir = filedir
    else:
      raise Exception("file does not exist")
    
    
  def __iter__(self):

    self.openfile()
    self.n=0
    return self
    
  def __next__(self):
    if self.n == len(self.dict):
      raise StopIteration
      
    else:
      key = list(self.dict)[self.n]
      thing = self.dict[key]
      self.n +=1
      return [thing, key]
       
    
  def openfile(self):
    f = open(self.filedir, "r")
    self.dict = json.load(f)
    return self.dict
    f.close()
  def overwrite(self, dict):
    self.dict = dict
    f = open(self.filedir, "w")
    json.dump(dict, f)

    f.close()
  
    
  def __str__(self):
    self.openfile()
    return str(self.dict)
  def get(self ,keys : list):
    self.openfile()
    part = self.dict
    for i in keys:
      part = part[i]
    return(part)
  def set(self ,keys : list, value):
    keys2 = keys
    self.openfile()
    
    for i in keys:
      part = self.dict
      print(keys2[:-1])
      for i in keys2[:-1]:
        part = part[i]
      if keys2[-1] == keys[-1]:
        print(keys2[-1])
        part[keys2[-1]] = value
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]

    
    self.overwrite(part)
    
    
  @classmethod
  def hi(cself):
    print(print(cself))
  def __getitem__(self, item):
    return jsonpart(self.filedir, [item])
  def __setitem__(self, item, value):
    self.openfile()
    print("set")
    
    self.dict[item] = value
    self.overwrite(self.dict)

  def test(self, file):

    def a(*args, **kargs):
      print(args)
      

class jsonpart(jsonfileclass):
  def __init__(self, filedir, index:list):
    self.keys = index
    super().__init__(filedir)
  def openfile(self):
    f = open(self.filedir, "r")
    part = json.load(f)
    for i in self.keys:
      part = part[i]
    self.dict = part
    f.close()
  def overwrite(self, value):
    
    
    print(self.keys[:-1])
    keys2 = self.keys
    for i in self.keys:
      f = open(self.filedir, "r")
      part = json.load(f)
      f.close()
      for i in keys2[:-1]:
        part = part[i]
      if keys2[-1] == self.keys[-1]:
        print(keys2[-1])
        part[keys2[-1]] = value
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]
      

    f = open(self.filedir, "w")
    print(part2)
    json.dump(part, f)
    f.close()
  def __getitem__(self, item):
    indexitems= self.keys
    indexitems.append(item)
    print(indexitems)
    return jsonpart(self.filedir, indexitems)
  def __setitem__(self, item, value):
    self.openfile()
    print("set")
    
    self.dict[item] = value
    self.overwrite(self.dict)
     
  
  
