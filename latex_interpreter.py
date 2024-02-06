def create_out_doc(out_name: str) -> None:
    out_file = open("out_name.txt", "w")
    out_file.write("\\documentclass{article}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{bm}\n\\begin{document}")

    return


def output_and_log():
    pass