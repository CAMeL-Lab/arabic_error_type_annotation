from scripts.annotation.an_annotate_error_type import annotate
from scripts.alignment.al_align_input_system import align_ref_system_basic
import os

def annote_ref_sys(ref_path, sys_path, show_paths=False):

    if not os.path.isdir('output'):
        os.mkdir('output')

    # Aligned files
    out_align_sys_ref = "output/align_sys_ref.tsv"

    # Annotated files
    out_annot_sys_ref = "output/annot_sys_ref.tsv"

    # Alignment process
    align_ref_system_basic(sys_path, ref_path, out_align_sys_ref)

    # Annotation process
    annotation_lines = annotate(out_align_sys_ref, out_annot_sys_ref,
                                show_paths=show_paths)

    return annotation_lines
