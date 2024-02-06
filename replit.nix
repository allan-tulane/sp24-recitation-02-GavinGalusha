{ pkgs }: {
  deps = [
    pkgs.run
    pkgs.ngn-k
    pkgs.pytest test_main.py::test_wor
    pkgs.import time
  ];
}