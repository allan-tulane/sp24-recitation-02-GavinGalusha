from main import *


def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(40, 5, 2) == 5390
  assert simple_work_calc(50, 6, 2) == 13592
  assert simple_work_calc(60, 7, 2) == 27416


""" done. """

def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(40, 4, 2, lambda n: n * n * n) == 123072
  assert work_calc(40, 3, 6, lambda n: 3) == 39
  assert work_calc(32, 3, 5, lambda n: 7) == 91


def test_compare_work():
  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work

  # create work_fn1
  # create work_fn2
  def work_fn1(n):
    return work_calc(n, 2, 2, lambda n: n)

  def work_fn2(n):
    return work_calc(n, 2, 2, lambda n: n * n)

  res = compare_work(work_fn1, work_fn2)
  print(res)


def test_compare_span():

  def span_fn1(n):
    return span_calc(n, 2, 2, lambda n: n)

  def span_fn2(n):
    return span_calc(n, 2, 2, lambda n: n * n)


# TODO
