from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import re

_LINE_SEP_DASHED = '-' * 50
_TRACEBACK_END_RGX = re.compile(r'\w+\:\s.+', re.IGNORECASE)


def read_multiline_input():
  line_chunks = []
  ip = str(input())
  try:
    while ip:  # (ip != '' or ip != '\n'):
      ip = ip.rstrip('\n')
      line_chunks.append(ip)
      ip = str(input())
  except (KeyboardInterrupt, EOFError):
    pass
  return line_chunks


def trace_log(chunk):
  lines = []
  line_pos = 0
  err_line = None
  capture = False
  end_capture = True
  pos = 0
  for line in chunk:
    line_pos = line.find('Traceback')
    if line.startswith(r'Traceback', line_pos):
      capture = True
      end_capture = False
      pos = line_pos
    if capture and not end_capture:
      err_line = line[pos:]
      lines.append(err_line)
    if err_line and _TRACEBACK_END_RGX.match(err_line):
      end_capture = True
      err_line = None
      lines.append(_LINE_SEP_DASHED)
  return '\n'.join(lines)


if __name__ == '__main__':
  print(trace_log(read_multiline_input()))
