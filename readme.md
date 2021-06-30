# Arabic Error Type Annotation

## Description
Arabic Error Type Annotation tool aims to annotate Arabic error types following the ALC tagset annotation.
## Installation
You will need Python 3.6 and above (64-bit).

1. Install [CamelTools](https://github.com/CAMeL-Lab/camel_tools#install-using-pip).
2. Install requirements.
```
pip install requirements
```

## Run the code

Annotation Command Line:
```
Usage: annotate_ar.py [OPTIONS] source target
where
    source - the source input (.m2 file)
    target - the system output
OPTIONS
```

Example:

```
python annotate_ar.py sample/QALB-Test2014.m2 sample/CLMB-1
```

This generates:
1. ```annot_input_ref.tsv``` file in the ```output``` folder that contains  the error types annotation between the input and the reference.
2. ```annot_input_sys.tsv``` file in the ```output``` folder that contains the error types annotation between the input and the system.
3.  ```subclasses_results_CLMB-1.tsv``` file in the ```results``` folder. This file contains the results of the evaluation of the system's output against the reference.
## License

## Contribute

## Contributors


