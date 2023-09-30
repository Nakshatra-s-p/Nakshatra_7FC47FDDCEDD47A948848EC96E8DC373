def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
products =["shoes","boot","loafer","shoes","sandles","shoes"]
target = "shoes"
target2 ='orange'
result = linearSearchProduct(products,target)
print(result)