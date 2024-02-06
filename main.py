from read_definitions import read_in
from proving import do_proof

if __name__ == "__main__":
    """ question = input("Input question in the form of \"if... then...\"\n") """
    all_defs = read_in()
    # test = "if S = {1+2x+5x^2, 1+x+x^2, 1+2x+3x^2} in P2 then S is linearly independent"
    # test = "if /set(W,/a1/x+/a2/x^2,{a1,a2\in \R})"
    test = "if f:S->T is a function and has an inverse function then f is bijective"
    # test = "if f:S->T is a function and is bijective then f has an inverse function"

    do_proof(test, all_defs)
    