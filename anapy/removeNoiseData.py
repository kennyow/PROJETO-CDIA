
## Corrigir

def removeNoiseData(df , column , rwidth):
  plt.hist(x = column , rwidth = rwidth)
  column_data = {
    "mode" : column.mode() ,
    "mean" : column.mean() ,
    "median" : column.median()
}
  if(column_data["mode"] == 0 and column_data["mean"] == 0 and column_data["median"] == 0):
    df = df(column , axis = "columns")
  return plt.hist(x = column , rwidth = rwidth) , column_data
