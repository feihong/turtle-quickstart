def r [file] {
  print $"python ($file)"
  python $file
}

def w [file] {
  print $"python watch.py ($file)"
  python watch.py $file
}

alias q = exit 0
