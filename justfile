set shell := ["nu", "-c"]

env:
  nu --config env.nu

install:
  pip install watchfiles
