# Tracelogstotraining

## What is Tracelogstotraining?

Tracelogstotraining is a project that transforms trace logs into training sets for machine learning models. Our training sample sets will be used for the training of the microservice fault diagnosis model.

## How to use Tracelogstotraining？

* Import trace logs (.json)
* Setting parameters
    *  starttime: The earliest timestamp of the target trace logs
    *  endtime: The latest timestamp of target trace logs
    *  fstarttime: The start timestamp of faults injection
    *  fendtime: The end timestamp of faults injection
* Modify the value of fnum
* Select function (by modifying the ftype parameters)
    *  0: Generate the normal request training sets
    *  1: Generate the faults request training sets
    *  2: Filter original trace logs
* Get the training sets

## No trace logs？

We give a sample in the example/trace logs directory, you just need to move it to the root of the project.
