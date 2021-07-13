# Arabic Error Type Annotation

## Description
The Arabic Error Type Annotation tool aims to annotate Arabic error types following the [ALC](https://www.arabiclearnercorpus.com/) tagset annotation.
## Installation
You will need Python 3.6 and above (64-bit).

1. Install [CamelTools](https://github.com/CAMeL-Lab/camel_tools#install-using-pip).
2. Install requirements.
```
pip install requirements
```

## Usage
### Error Type Annotation:
```
Usage: annotate_err_type_ar.py [OPTIONS] system reference 
where
    system - the system output
    reference - the reference file
OPTIONS
    -o output file location; default is standard output.
    
```

Example:

```
python annotate_err_type_ar.py sample/sys_sample.txt sample/ref_sample.txt
```

The output lists triplets of system, reference and error types for the complete list of error types (see table of error types below).

Example of a sentence of 5 words 

System sentence:  إن أمتحان الاستاذة صعبة

Reference sentence: إن إمتحان الأستاذ صعب

Annotation result:

|      System    |   Reference      |  Error type     | 
|----------|---------|-------| 
| إن       | إن      | UC    | 
| أمتحان   | إمتحان  | OH    | 
| الاستاذة | الأستاذ | OH+XG | 
| صعبة     | صعب     | XG    | 

 

### Annotation and evaluation using m2 files (Command Line):
```
Usage: annotate_eval_ar.py [OPTIONS] system source_reference 
where
    system - the system output
    source_reference - source sentences with gold token edits (.m2 file)
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
  "mle_top": ""
}
```

## Table of Error Types

|               |           |                                                     |                            |                            | 
|---------------|-----------|-----------------------------------------------------|----------------------------|----------------------------| 
| **Class**         | **Sub-class** | **Description**                                         | **Arabic Example**             | **Buckwalter Transliteration** | 
| **Orthographic**  | OH        | Hamza error                                         | اكثر← أكثر                 | Akvr → >kvr                | 
|               | OT        | Confusion in Ha and Ta Mutadarrifatin               | مشاركه ← مشاركة            | m$Arkh → m$Arkp            | 
|               | OA        | Confusuion in Alif and Ya Mutadarrifatin            | علي ← على                  | Ely → ElY                  | 
|               | OW        | Confusion in Alif Fariqa                            | وكانو ←  وكانوا            | wkAnw→ wkAnwA              | 
|               | ON        | Confusion Between Nun and Tanwin                    | ثوبن ← ثوبٌ                | vwbn → vwbN                | 
|               | OS        | Shortening the long vowels                          | أوقت ← أوقات               | >wqt → >wqAt               | 
|               | OG        | Lengthening the short vowels                        | نقيمو ← نقيم               | nqymw → nqym               | 
|               | OC        | Wrong order of word characters                      | تبرينا ← تربينا            | tbrynA → trbynA            | 
|               | OR        | Replacement in word character(s)                    | مصلنا ← وصلنا              | mSlnA → wSlnA              | 
|               | OD        | Additional character(s)                             | يعدوم ← يدوم               | yEdwm → ydwm               | 
|               | OM        | Missing character(s)                                | سالين ← سائلين             | sAlyn → sA}lyn             | 
|               | OO        | Other orthographic errors                           | -                          | -                          | 
| **Morphological** | MI        | Word inflection                                     | معروف ← عارف               | mErwf → EArf               | 
|               | MT        | Verb tense                                          | تفرحني ← أفرحتني           | tfrHny → >frHtny           | 
|               | MO        | Other morphological errors                          | -                          | -                          | 
| **Syntax**        | XC        | Case                                                | رائع ← رائعاً              | rA}E → rA}EAF              | 
|               | XF        | Definiteness                                        | السن ← سن                  | Alsn → sn                  | 
|               | XG        | Gender                                              | الغربي ← الغربية           | Algrby → Algrbyp           | 
|               | XN        | Number                                              | فكرتي ← أفكاري             | fkrty → >fkAry             | 
|               | XT        | Unnecessary word                                    | على ←Null                  | ElY →Null                  | 
|               | XM        | Missing word                                        | Null ← على                 | Null → ElY                 | 
|               | XO        | Other syntactic errors                              | -                          | -                          | 
| **Semantic**      | SW        | Word selection error                                | من ← عن                    | mn → En                    | 
|               | SF        | Fasl wa wasl (confusion in conjunction use/non-use) | سبحان ← فسبحان             | sbHAn → fsbHAn             | 
|               | SO        | Other semantic errors                               | -                          | -                          | 
| **Punctuation**   | PC        | Punctuation confusion                               | المتوسط. ← المتوسط،        | AlmtwsT. → AlmtwsT،        | 
|               | PT        | Unnecessary punctuation                             | العام,  ← العام            | AlEAm,  → AlEAm            | 
|               | PM        | Missing punctuation                                 | العظيم ←  العظيم،          | AlEZym →  AlEZym،          | 
|               | PO        | Other errors in punctuation                         | -                          | -                          | 
|               |           |                                                     |                            |                            | 
| **Merge**         | MG        | Words are merged                                    | ذهبتالبارحة ← ذهبت البارحة | *hbtAlbArHp → *hbt AlbArHp | 
| **Split**         | SP        | Words are split                                     | المحا دثات ← المحادثات     | AlmHA dvAt → AlmHAdvAt     | 

## License

## Contribute

## Contributors


