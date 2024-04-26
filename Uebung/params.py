class Parameters:
  
  def __init__(self, filename) -> None:
    with open(filename) as f:
      content = f.read().splitlines()

    for idx, line in enumerate(content):
      line_split = line.split()
      if (line_split[0] == "ini_temp"):
        self.ini_temp = float(line_split[1])
      if (line_split[0] == "final_temp"):
        self.final_temp = float(line_split[1])
      if (line_split[0] == "n_step"):
        self.n_step = int(line_split[1])
      if (line_split[0] == "x_ini"):
        x_ini = line_split[1].split(',')
        for idx, x_i in enumerate(x_ini):
          x_ini[idx] = float(x_i)
        self.x_ini = x_ini
      if (line_split[0] == "x_delta"):
        self.x_delta = float(line_split[1])
      if (line_split[0] == "seed"):
        self.seed = int(line_split[1])
      if (line_split[0] == "foutname"):
        self.foutname = line_split[1]
