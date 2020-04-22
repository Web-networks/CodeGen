import argparse
import sys
import numpy as np

import ng_bus
import ng_input
import train

from sklearn.metrics import classification_report

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
X_test, y_test = ng_io.get_test_xy()

# надо бы как-то чтобы пробрасывалось компонентно число эпох
# пока количество эпох чисто захардкожено
train.do_compile()
result_of_train = train.do_train(X_train, y_train, X_test, y_test)
#оценка работы модели
print (np.mean(result_of_train.history["val_acc"]))
