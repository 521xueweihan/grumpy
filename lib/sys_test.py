# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=bare-except

import sys
import types

import weetest


def TestArgv():
  assert sys.argv


def TestMaxInt():
  assert sys.maxint > 2000000000


def TestSysModules():
  assert sys.modules['sys'] is not None


def TestExcInfoNoException():
  assert sys.exc_info() == (None, None, None)


def TestExcInfoWithException():
  try:
    raise RuntimeError
  except:
    t, e, tb = sys.exc_info()
  else:
    assert False
  assert t is RuntimeError
  assert isinstance(e, t)
  assert isinstance(tb, types.TracebackType)


def TestExitEmpty():
  try:
    sys.exit()
  except SystemExit as e:
    assert e.code == None, e.code  # pylint: disable=g-equals-none
  except:
    assert False


def TestExitCode():
  try:
    sys.exit(42)
  except SystemExit as e:
    assert e.code == 42, e.code
  except:
    assert False


def TestExitInvalidArgs():
  try:
    sys.exit(1, 2, 3)
  except TypeError as e:
    assert str(e) == 'exit() takes 1 arguments (3 given)', str(e)
  except:
    assert False


if __name__ == '__main__':
  # This call will incidentally test sys.exit().
  weetest.RunTests()
