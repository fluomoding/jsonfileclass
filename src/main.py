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
      for i in keys2[:-1]:
        part = part[i]
      if keys2[-1] == keys[-1]:
        part[keys2[-1]] = value
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]
    self.overwrite(part)
  def __getitem__(self, item):
    return jsonpart(self.filedir, [item])
  def __setitem__(self, item, value):
    self.openfile()
    self.dict[item] = value
    self.overwrite(self.dict)
  def remove(self, keys):
    keys2 = keys
    self.openfile()
    for i in keys:
      part = self.dict
      for i in keys2[:-1]:
        part = part[i]
      if keys2[-1] == keys[-1]:
        del part[keys2[-1]]
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]
    self.overwrite(part)
  def __delitem__(self, item):
    self.openfile()
    del self.dict[item] 
    print(self.dict)
    self.overwrite(self.dict)
  def backup(self, backupfiledir):
    self.openfile()
    f = open(backupfiledir, "w")
    json.dump(self.dict, f)
    f.close()
  def revert(self, backupfiledir):
    f = open(backupfiledir, "r")
    file = json.load(f)
    f.overwrite(file)
    
    
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
    return(self.dict)
  def overwrite(self, value):
    keys2 = self.keys
    for i in self.keys:
      f = open(self.filedir, "r")
      part = json.load(f)
      f.close()
      for i in keys2[:-1]:
        part = part[i]
      if keys2[-1] == self.keys[-1]:
        part[keys2[-1]] = value
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]
    f = open(self.filedir, "w")
    json.dump(part, f)
    f.close()
  def __getitem__(self, item):
    indexitems= self.keys
    indexitems.append(item)
    return jsonpart(self.filedir, indexitems)
  def backup(self, backupfiledir):
    keys2 = self.keys
    print(keys2)
    self.openfile()
    f = open(backupfiledir, "r")
    backupdict= json.load(f)
    f.close()
    for i in self.keys:
      part = backupdict
      for i in keys2[:-1]:

        part = part[i]
      if keys2[-1] == self.keys[-1]:
        part[keys2[-1]] = self.openfile()
      else:
        part[keys2[-1]] = part2
      part2 = part
      keys2 = keys2[:-1]
    f = open(backupfiledir, "w")
    json.dump(part, f)
    f.close()
  def revert(self, backupfiledir):
    f = open(backupfiledir, "r")
    backupdict= json.load(f)
    f.close()
    part = backupdict
    for i in self.keys:
      part = part[i]
    self.overwrite(part)
