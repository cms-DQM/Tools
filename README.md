# Tools
A repo for random DQM related tools

### compareDQMTrees.py

This tool prints paths to monitor elements that exist in one file but not in the other.

```console
foo@bar:~$ compareDQMTrees.py file1.root file2.root
Monitor elements that are in first file but are not in the second one:
path/to/monitor/element1
path/to/monitor/element2
Monitor elements that are in second file but are not in the first one:
path/to/monitor/element3
```
