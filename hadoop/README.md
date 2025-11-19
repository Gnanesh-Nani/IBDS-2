Great — since your Hadoop setup is **already installed**, we will **not reinstall anything**.
I’ll guide you through **exactly what you asked**:

 Use the existing Hadoop
 Create a directory in HDFS
 Upload a sample file
 Write a MapReduce program (Java **or** Python Streaming — I’ll give both options)
 Run it
 View output
 Explain how Mapper + Reducer processed it

---

#  **PART 1 — Create HDFS directory and upload sample text**

### 1 Start Hadoop (DFS + YARN)

```bash
start-dfs.sh
start-yarn.sh
```

Make sure `jps` shows:

* NameNode
* DataNode
* ResourceManager
* NodeManager
* SecondaryNameNode

---

### 2 Create a directory in HDFS

```bash
hdfs dfs -mkdir /input
```

---

### 3 Create a sample text file locally

```bash
echo "hello hadoop hello mapreduce hello world" > sample.txt
```

---

### 4 Upload it to HDFS

```bash
hdfs dfs -put sample.txt /input/
```

Verify:

```bash
hdfs dfs -ls /input
```

---

#  **PART 2 — Choose MapReduce Type**

You can choose **Java MapReduce** (classic) or **Python Streaming** (simpler).

Below I give **both**.

---

# OPTION A — **Python Streaming (very easy)**

---

### 1 Create mapper.py

```bash
nano mapper.py
```

Paste:

```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(f"{word}\t1")
```

---

### 2 Create reducer.py

```bash
nano reducer.py
```

Paste:

```python
#!/usr/bin/env python3
import sys

current_word = None
count = 0

for line in sys.stdin:
    word, val = line.strip().split("\t")
    val = int(val)

    if current_word == word:
        count += val
    else:
        if current_word:
            print(f"{current_word}\t{count}")
        current_word = word
        count = val

if current_word:
    print(f"{current_word}\t{count}")
```

---

### 3 Add execute permission

```bash
chmod +x mapper.py reducer.py
```

---

### 4 Run MapReduce using Hadoop Streaming

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /input/sample.txt \
  -output /output_wordcount \
  -mapper mapper.py \
  -reducer reducer.py
```

---

### 5 View output

```bash
hdfs dfs -cat /output_wordcount/part-00000
```

Expected output:

```
hadoop 1
hello 3
mapreduce 1
world 1
```

---

# OPTION B — **Java MapReduce (classic Hadoop)**

(*Use this only if you want the Java version for your assignment.*)

If you want, I’ll give you a full Maven project with `WordCount.java`.

Just tell me:

 "Give Java MapReduce code also."

---

#  **PART 3 — Explanation (for your assignment write-up)**

### 🔹 Mapper Role

* Reads each line from input
* Splits into words
* Emits each word as a key with value `1`

Example emission:

```
hello    1
hadoop   1
hello    1
world    1
```

---

### 🔹 Shuffle & Sort Phase (Hadoop internal)

Hadoop groups values by key:

```
hello → [1,1,1]
hadoop → [1]
world → [1]
mapreduce → [1]
```

---

### 🔹 Reducer Role

Reducer sums all counts for each word:

```
hello → 1+1+1 = 3
hadoop → 1
world → 1
mapreduce → 1
```

---

### 🔹 Final Output Location

Stored in:

```
/output_wordcount/part-00000
```

In HDFS.

---

#  YOUR NEXT STEP

Tell me which version you want to continue with:

###  **Python Streaming (easier) — already complete**

###  **Java MapReduce full Maven project (I can generate for you)**

Just reply:

 “Give me Java MapReduce version”
or
 “Python version is enough”
