
!/usr/bin/env python3
import numpy as np
import argparse
import os




def exec_shell(input_mlir):
    os.system()


def cmp_tensor(arg):
   ref = np.load(arg.ref);
   res = np.load(arg.res);
   size = ref[arg.tensor].size
   shape = ref[arg.tensor].shape
   index = np.arange(0, size).reshape(shape)
   print(index[ref[arg.tensor] != res[arg.tensor]])


def dump_input(file_name, tensor, output_name):
   data = {}
   ref = np.load(file_name);
   data[tensor] = ref[tensor]
   data[tensor] = np.array(data[tensor], dtype='float32')
   np.savez(output_name, **data)


def dump_data(file_name, tensor):
   data = {}
   ref = np.load(file_name);
   data[tensor] = ref[tensor]
   print (data[tensor].shape)
   print (data[tensor][0, 0, 0, 52:])


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--ref', required=True, help='name of input file name')
  parser.add_argument('--res', required=True, help='name of input file name')
  parser.add_argument('--tensor', required=True, help='name of tensor')
  parser.add_argument('--name', required=False, help='name of output file')
  parser.add_argument("--dump", action='store_true', default=False,
                        help="dump data")
  parser.add_argument("--cmp", action='store_true', default=False,
                        help="dump data")
  parser.add_argument("--save", action='store_true', default=False,
                        help="dump data")


  arg = parser.parse_args()
  if arg.dump:
    dump_data(arg.ref, arg.tensor)
    dump_data(arg.res, arg.tensor)
  if arg.save:
    dump_input(arg.res, arg.tensor, arg.name)
  if arg.cmp:
    cmp_tensor(arg)


