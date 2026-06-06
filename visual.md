# Inputting
============================
1. Math
2. Biology
Choose which subject to study or create a new one
(input)
============================
# How the report may look like
================ STUDY REPORT ================

Subjects         : 2
Total Sessions   : 6
Total Study Time : 3h 18m

Math
==================================================
Sessions         : 3
Total Time Spent : 1h 42m
Average Session  : 34 Min

Study Log
--------------------------------------------------
2026-06-01  | 30 Min
2026-06-03  | 60 Min
2026-06-05  | 12 Min


Biology
==================================================
Sessions         : 3
Total Time Spent : 1h 36m
Average Session  : 32 Min

Study Log
--------------------------------------------------
2026-06-02  | 44 Min
2026-06-04  | 22 Min
2026-06-05  | 30 Min



# How the variable sessions value should probably look like:
report = [
    {
        "subject" : "math",
        "minute" : [30, 12, 33, 44, 31]
    },
    {
        "subject" : "biology",
        "minute" : [44, 73, 12, 43]
    }
]
