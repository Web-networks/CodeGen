import argparse
import sys

import ng_bus
import ng_input
import train

bus = ng_bus.NeurogenBus('train')
io = ng_input.NeurogenIO(bus)
train = train.TrainController(bus)

cli_vars = []
cli_vars += ng_io.get_vars()
cli_vars += train.get_vars()

parser = argparse.ArgumentParser()

for cli_var in cli_vars:
  parser.add_argument('--' + cli_var)

print('args:', parser.parse_args(sys.argv))

ng_io.read_inputs()
X_train, y_train = ng_io.get_train_xy()

# надо бы как-то чтобы пробрасывалось компонентно число эпох
train.do_train(X_train, y_train)
