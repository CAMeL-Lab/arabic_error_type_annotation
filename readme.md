# Arabic Error Type Annotation

## Description
The Arabic Error Type Annotation tool aims to annotate Arabic error types following the ALC tagset annotation.
## Installation
You will need Python 3.6 and above (64-bit).

1. Install [CamelTools](https://github.com/CAMeL-Lab/camel_tools#install-using-pip).
2. Install requirements.
```
pip install requirements
```

## Usage
### Annotation:
```
Usage: annotate_err_type.py [OPTIONS] reference target
where
    reference - the reference file
    target - the system output
OPTIONS
```

Example:

```
python annotate_err_type.py sample/ref_sample.txt sample/sys_sample.txt
```
This generates a file with the name ```annot_sys_ref.tsv``` in the ```output``` folder. This file contains all the ```<sys,ref>``` pairs with the error types.

### Annotation and evaluation using m2 files (Command Line):
```
Usage: annotate_eval_ar.py [OPTIONS] source target
where
    source - the source input (.m2 file)
    target - the system output
OPTIONS
```

Example:

```
python annotate_eval_ar.py sample/QALB-Test2014.m2 sample/CLMB-1
```

This generates:
1. ```annot_input_ref.tsv``` file in the ```output``` folder that contains  the error types annotation between the input and the reference.
2. ```annot_input_sys.tsv``` file in the ```output``` folder that contains the error types annotation between the input and the system.
3.  ```subclasses_results_CLMB-1.tsv``` file in the ```results``` folder. This file contains the results of the evaluation of the system's output against the reference.

## Configuration
In the configuration file ```config.json```, the user should specify the mode of the morphological analyser. The default value is ```analyser``` in which all the analyses are considered. The second option is 
```mle``` and in this case, we need to specify the parameter ```mle_top``` which represents the maximum number of analyses to be considered. The ```uc``` parameter takes the values 0 or 1. 0 to indicate that we do not consider the unchanged error types, 1 otherwise.  

```
{
  "mode": "analyser",
  "mle_top": "",
  "uc": 0
}
```


## License

## Contribute

## Contributors


