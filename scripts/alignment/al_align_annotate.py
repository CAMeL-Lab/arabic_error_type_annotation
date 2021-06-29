from scripts.annotation.an_annotate_error_type import annotate
from scripts.alignment.al_align_input_reference import align_input_reference
from scripts.alignment.al_align_input_system import align_input_system
from scripts.evaluation.eval_functions import eval_multi_label_subclasses


def process_align_annot_eval(ref_path, sys_path, uc):
    # System submission file
    exp_name = sys_path.split("/")[-1]

    # Aligned files
    out_align_input_ref = "output/align_input_ref.tsv"
    out_align_input_sys = "output/align_input_sys.tsv"

    # Annotated files
    out_annot_input_ref = "output/annot_input_ref.tsv"
    out_annot_input_sys = "output/annot_input_sys.tsv"

    # Alignment process
    align_input_reference(ref_path, out_align_input_ref)
    align_input_system(sys_path, out_align_input_sys)

    # Annotation process
    annotate(out_align_input_ref, out_annot_input_ref)
    annotate(out_align_input_sys, out_annot_input_sys)

    # Evaluation process
    eval_multi_label_subclasses(uc, exp_name)



